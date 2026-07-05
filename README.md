
readme = '''# 🔍 Multi-Threaded Port Scanner

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Threads](https://img.shields.io/badge/Threads-100-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=for-the-badge)

> ⚡ A **professional Python port scanner** with multi-threading, result logging, and safe exception handling. Built for learning cybersecurity!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧵 **Multi-Threaded** | Scans up to 100 ports simultaneously |
| 📝 **Auto-Logging** | Saves results to `scan_results.txt` with timestamps |
| 🛡️ **Safe & Clean** | Handles errors gracefully (no crashes!) |
| 🎯 **Easy Input** | Choose single port, common range, or full scan |
| 🌐 **Domain Support** | Scan by IP *or* domain name (e.g., `scanme.nmap.org`) |
| 🔒 **Security Minded** | `.gitignore` keeps scan logs private |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/laiba-khan-13/port-scanner.git
cd port-scanner
```

### 2. Run the scanner
```bash
python port_scanner.py
```

### 3. Follow the prompts
```
🎯 Let's set up your scan!
Enter target IP or domain: 127.0.0.1
Choose an option (1/2/3): 1
Threads to use (press Enter): 
```

---

## 📸 Screenshot

![Scanner Running](screenshot.png)

*The scanner finding open ports on localhost with 100 threads!*

---

## 🛠️ How It Works

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   User Input    │────▶│  Port Queue     │────▶│ Worker Threads  │
│ (IP & Range)    │     │ (1 to 65535)    │     │ (100 threads)   │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                              ┌──────────────────────────┘
                              ▼
                    ┌─────────────────┐
                    │  Socket Connect │
                    │  (Open/Closed?) │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │   Port OPEN     │           │  Port CLOSED    │
    │  Print + Save   │           │    Ignore       │
    └─────────────────┘           └─────────────────┘
```

---

## 📋 Example Output

```
============================================================
🛡️  MULTI-THREADED PORT SCANNER 3000 PRO 🛡️
============================================================

🌐 Resolved '127.0.0.1' -> 127.0.0.1
📋 Scanning ports 1 to 1024
🧵 Using 100 threads
⏱️  Timeout: 1.0s per port
------------------------------------------------------------
🟢 Port   135 is OPEN  → MS RPC (Windows Internal)
🟢 Port   445 is OPEN  → SMB (File Sharing)
🟢 Port   623 is OPEN  → Intel AMT (Remote Management)
🟢 Port   903 is OPEN  → VMware/Java Console
🟢 Port  5040 is OPEN  → Windows Device Discovery
🟢 Port  5357 is OPEN  → WSDAPI (Network Devices)
------------------------------------------------------------
✅ Found 6 open port(s)!
⏱️  Scan completed in 12.13 seconds
============================================================

📝 Results saved to: scan_results.txt
```

---

## 🗂️ Project Structure

```
port-scanner/
├── 📄 port_scanner.py      # Main scanner code
├── 📄 README.md            # This file!
├── 📄 .gitignore           # Keeps scan_results.txt private
└── 🖼️ screenshot.png       # Screenshot of the tool running
```

---

## ⚠️ Legal Disclaimer

> **Only scan computers you OWN or have explicit PERMISSION to scan!**  
> Unauthorized scanning of networks you don't own may be illegal in your country. This tool is for **educational purposes only**.

---

## 🧰 Built With

- 🐍 **Python 3** — The core language
- 🔌 **socket** — Network connections
- 🧵 **threading** — Concurrent port scanning
- 📋 **queue** — Thread-safe port distribution
- 🕐 **datetime** — Timestamp logging


---

## 🙋‍♀️ Author

**Laiba Khan** — Aspiring Cybersecurity Enthusiast 🛡️

- GitHub: [@laiba-khan-13](https://github.com/laiba-khan-13)
- Project: [port-scanner](https://github.com/laiba-khan-13/port-scanner)

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and learn from it!

---

<p align="center">
  ⭐ Star this repo if you found it helpful!
</p>
'''



