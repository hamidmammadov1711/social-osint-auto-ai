# 🚀 PROFESSIONAL OSINT SUITE v3.5 (Hacker Edition)

This project is a fully automated, professional OSINT (Open Source Intelligence) system designed for **Kali Linux**, **Windows**, and **macOS**.

---

## 📁 Project Structure
```text
social-osint-auto/
├── main.py                # Main Terminal UI
├── src/
│   ├── modules/           # OSINT Modules (IP, Email, Social)
│   ├── reports/           # HTML Report Generator
│   └── utils/             # I18N, Logger
└── README_EN.MD           # Documentation
```

## 🖥️ Terminal Interface (Preview)
```text
+------------------------------------------------------------+
|  ██████╗ ███████╗██╗███╗   ██╗████████╗    ██████╗ ██╗   ██╗ |
| ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝ |
| [ G O V E R N M E N T   G R A D E   O S I N T   S Y S T E M ] |
+------------------------------------------------------------+
[root@osint] # 04
[*] Initiating Cyber Reconnaissance...
  > Scanning Social Grid... [####################] 100%
  > Breached DB Lookup...   [####################] 100%
[✓] ACCESS SECURED: results/report_target.html
```

## 📄 Report Aesthetics (Premium HTML)
Reports are generated in a **High-End Hacker Theme (Matrix Edition)**:
- **Matrix Grid Background:** Professional green & black aesthetic.
- **Dynamic Data:** Geolocation mapping, breached email details, and social grid results.
- **Security Tags:** Each module output is tagged (e.g., [SIGINT], [BREACH_DB]) for a professional look.

---

## 💻 Installation (Universal)

### 1. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys:
Create a `.env` file in the root directory and add your keys:
```env
SHODAN_API_KEY=your_key
HIBP_API_KEY=your_key
```

---

## 🛠️ Multi-Platform Instructions

### 🟢 For Windows Users
The system is fully stable on Windows. Note that some Linux-specific anonymity tools (e.g., `macchanger`) are not available. The system automatically detects this and provides warnings while continuing other OSINT functions.
- **Run:** `python main.py`
- **Requirement:** Python 3.10+

### 🟣 For Kali Linux Users
On Kali Linux, the system runs in **Native Mode**, integrating directly with Kali's built-in tools.
- **Anonymity:** Full integration with `macchanger` and `tor` services.
- **Native Tools:** If `sherlock`, `holehe`, or `phoneinfoga` are installed as system packages, the suite uses them directly for maximum performance.
- **Run:** `sudo python3 main.py`

### ⚪ For macOS Users
Being Unix-based, the system runs extremely smoothly on macOS. For Tor proxy support, `brew install tor` is recommended.
- **Run:** `python3 main.py`

---

## 🎯 Key Features
- **Multi-language Support:** Choose between Azerbaijani and English at startup.
- **Hacker Aesthetic:** Matrix-themed CLI and premium dark-mode HTML reports.
- **Universal Compatibility:** Identical experience across all major operating systems.
- **Advanced IP Intel:** Detailed geolocation, ISP info, and proxy detection.
- **Social Grid Search:** Recursive username search across 300+ platforms.

---

## 🗺️ Roadmap (v4.0 Upcoming)
- [ ] **AI-Powered Analysis**: Findings summarization using LLMs.
- [ ] **Visual Link Analysis**: Interactive graphs of target connections.
- [ ] **Image Forensics**: Automated EXIF and metadata extraction.
- [ ] **Web Dashboard**: Local FastAPI interface for better visualization.

---

## ⚠️ Legal Disclaimer
This tool is for educational and ethical research purposes only. Unauthorized use against targets without consent is illegal. The author is not responsible for any misuse.

**Author:** Hamid Mammadov
**Version:** 3.5 (Hacker Edition)
