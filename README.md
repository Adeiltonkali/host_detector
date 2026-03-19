# Active Host Scanner

**Active Host Scanner** is a simple Python tool that performs a ping sweep on a local network to detect which hosts are currently active.

---

## 📡 What it Does

This script scans the local network range (e.g., `192.168.1.0/24`) and sends a single ping to each IP address.  
If a device responds, it is marked as **active** and printed on the screen.

---

## ⚙ Requirements

- Python 3.x  
- Works on Windows and Linux  
- No external libraries needed (uses `subprocess` module)

---

## 🚀 How to Use

### 🔽 Clone the Repository

```bash
git clone https://github.com/Adeiltonkali/active-host-scanner.git
cd active-host-scanner
```

### ▶️ Run the Script

```bash
python active_host_scanner.py
```

---

## 📦 Example Output

```
Scanning 192.168.1.0/24...
Host 192.168.1.1 is active.
Host 192.168.1.4 is active.
Scan completed.
```

---

## 📜 License

This project is licensed under the MIT License.
