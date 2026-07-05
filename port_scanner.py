

# MULTI-THREADED PORT SCANNER
# A professional network scanning tool for learning purposes
# ============================================================

import socket
import threading
import queue
from datetime import datetime



# STEP 1: CONFIGURATION & DATA


# Common services that run on specific ports (like name tags on doors)
COMMON_SERVICES = {
    20: "FTP-Data",
    21: "FTP (File Transfer)",
    22: "SSH (Secure Login)",
    23: "Telnet",
    25: "SMTP (Email)",
    53: "DNS",
    67: "DHCP",
    68: "DHCP-Client",
    80: "HTTP (Website)",
    110: "POP3 (Email)",
    143: "IMAP (Email)",
    443: "HTTPS (Secure Website)",
    445: "SMB (File Sharing)",
    3306: "MySQL (Database)",
    3389: "RDP (Remote Desktop)",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy",
}

# How many threads (workers) to use at once
MAX_THREADS = 100

# Timeout for each connection attempt (in seconds)
TIMEOUT = 1.0

# File to save results
LOG_FILE = "scan_results.txt"



# STEP 2: THE SCANNER CLASS (The Professional Way!)


class MultiThreadedPortScanner:
    """
    This is a CLASS. Think of it like a blueprint for a robot.
    We create one robot, tell it what to do, and it does the work!
    """

    def __init__(self, target_host, start_port, end_port, thread_count=MAX_THREADS):
        self.target_host = target_host
        self.start_port = start_port
        self.end_port = end_port
        self.thread_count = thread_count
        
        # This is our "talking stick" for safe printing
        self.print_lock = threading.Lock()
        
        # This is our todo-list of ports
        self.port_queue = queue.Queue()
        
        # List to remember open ports
        self.open_ports = []
        
        # Will store the resolved IP address
        self.target_ip = None

    def _resolve_target(self):
        """
        STEP 2A: Turn a name like 'google.com' into an IP like '142.250.80.46'
        This is like looking up a phone number in a phone book.
        """
        try:
            self.target_ip = socket.gethostbyname(self.target_host)
            print(f"\n Resolved '{self.target_host}' -> {self.target_ip}")
        except socket.gaierror:
            print(f"\n❌ ERROR: Could not resolve '{self.target_host}'")
            print("   Make sure you typed the address correctly!")
            return False
        return True

    def _scan_single_port(self, port):
        """
        STEP 2B: Check ONE port.
        This is the same socket logic from your original file,
        but wrapped in a try-except so it never crashes!
        """
        try:
            # Create a "phone" (TCP socket)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)
            
            # Try to "call" the port (connect)
            result = sock.connect_ex((self.target_ip, port))
            
            if result == 0:
                # Port is OPEN! 
                service = COMMON_SERVICES.get(port, "Unknown Service")
                
                # Use the Lock so only one thread prints at a time
                with self.print_lock:
                    print(f"🟢 Port {port:>5} is OPEN  → {service}")
                
                self.open_ports.append((port, service))
            
            sock.close()
            
        except socket.error as e:
            # Something went wrong with the network
            pass  # We just ignore errors on closed ports
        except Exception as e:
            # Catch any other weird errors
            pass

    def _worker(self):
        """
        STEP 2C: The worker function.
        Each thread runs this. It keeps grabbing ports from the Queue
        until the Queue is empty.
        """
        while True:
            try:
                # Get a port from the todo-list (don't wait forever)
                port = self.port_queue.get(timeout=1)
                self._scan_single_port(port)
                self.port_queue.task_done()  # Mark this job as finished
            except queue.Empty:
                # No more ports left to check!
                break
            except Exception:
                break

    def run(self):
        """
        STEP 2D: The BOSS function.
        Sets up everything, hires workers, and waits for completion.
        """
        print("=" * 60)
        print("  MULTI-THREADED PORT SCANNER 3000 PRO ")
        print("=" * 60)
        
        # 1. Resolve the target to an IP
        if not self._resolve_target():
            return []
        
        print(f" Scanning ports {self.start_port} to {self.end_port}")
        print(f" Using {self.thread_count} threads")
        print(f"  Timeout: {TIMEOUT}s per port")
        print("-" * 60)
        
        # 2. Fill the Queue with all port numbers
        total_ports = self.end_port - self.start_port + 1
        for port in range(self.start_port, self.end_port + 1):
            self.port_queue.put(port)
        
        start_time = datetime.now()
        
        # 3. Hire our worker threads!
        threads = []
        for _ in range(self.thread_count):
            t = threading.Thread(target=self._worker)
            t.daemon = True  # Threads die when main program ends
            t.start()
            threads.append(t)
        
        # 4. Wait for all threads to finish
        # We show a progress indicator while waiting
        try:
            for t in threads:
                t.join()
        except KeyboardInterrupt:
            print("\n\n  Scan interrupted by user (Ctrl+C)")
            return self.open_ports
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # 5. Show results
        print("-" * 60)
        if self.open_ports:
            print(f" Found {len(self.open_ports)} open port(s)!")
        else:
            print(" No open ports found in this range.")
        print(f"  Scan completed in {duration:.2f} seconds")
        print("=" * 60)
        
        return self.open_ports

    def save_results(self):
        """
        STEP 2E: Write everything to a file.
        This is like writing a report card for the scan.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(LOG_FILE, "a") as f:  # "a" = append (add to end of file)
            f.write("\n" + "=" * 50 + "\n")
            f.write(f"SCAN REPORT - {timestamp}\n")
            f.write(f"Target Host: {self.target_host}\n")
            f.write(f"Target IP:   {self.target_ip}\n")
            f.write(f"Port Range:  {self.start_port}-{self.end_port}\n")
            f.write(f"Threads:     {self.thread_count}\n")
            f.write("-" * 50 + "\n")
            
            if self.open_ports:
                f.write("OPEN PORTS:\n")
                for port, service in sorted(self.open_ports):
                    f.write(f"  {port:>5}  {service}\n")
            else:
                f.write("No open ports found.\n")
            
            f.write("=" * 50 + "\n")
        
        print(f"\n Results saved to: {LOG_FILE}")



# STEP 3: USER INPUT & MAIN PROGRAM


def get_user_input():
    """
    Ask the user what they want to scan.
    We wrap this in a function to keep things organized!
    """
    print("\n Let's set up your scan!")
    
    # Get target
    target = input("Enter target IP or domain (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
    if not target:
        target = "127.0.0.1"
        print("   (Using default: 127.0.0.1)")
    
    # Get port range
    print("\n Port Range Options:")
    print("   1. Common ports (1-1024)")
    print("   2. Full range (1-65535)")
    print("   3. Custom range")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == "2":
        start, end = 1, 65535
    elif choice == "3":
        start = int(input("Start port: "))
        end = int(input("End port: "))
    else:
        start, end = 1, 1024  # Default: common ports
    
    # Get thread count (optional)
    threads_input = input(f"\n Threads to use (default {MAX_THREADS}, press Enter to skip): ").strip()
    threads = int(threads_input) if threads_input.isdigit() else MAX_THREADS
    
    return target, start, end, threads


def main():
    """
    This is the MAIN function. It's the starting point of our program.
    """
    try:
        # 1. Get settings from user
        target, start_port, end_port, threads = get_user_input()
        
        # 2. Create our scanner robot
        scanner = MultiThreadedPortScanner(target, start_port, end_port, threads)
        
        # 3. Run the scan!
        open_ports = scanner.run()
        
        # 4. Save results to file
        if open_ports is not None:
            scanner.save_results()
        
        print("\n Scan complete! Remember: Only scan computers you OWN or have PERMISSION to scan!")
        
    except ValueError as e:
        print(f"\n❌ Invalid input: {e}")
        print("  Make sure you enter numbers for ports and threads!")
    except KeyboardInterrupt:
        print("\n\n Done! Scan cancelled.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")



# STEP 4: RUN THE PROGRAM!

if __name__ == "__main__":
    main()