<div align="center">

![HXR Banner](hxr_logo.svg)

<br>

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.1-FFD700?style=for-the-badge&logo=github&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-00D4FF?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-7B2FF7?style=for-the-badge)

![Stars](https://img.shields.io/github/stars/ruyynn/hxr?style=for-the-badge&logo=starship&color=FFD700&labelColor=1a1a2e)
![Forks](https://img.shields.io/github/forks/ruyynn/hxr?style=for-the-badge&logo=git&color=00D4FF&labelColor=1a1a2e)
![Issues](https://img.shields.io/github/issues/ruyynn/hxr?style=for-the-badge&logo=github&color=FF6B35&labelColor=1a1a2e)
![Last Commit](https://img.shields.io/github/last-commit/ruyynn/hxr?style=for-the-badge&logo=git&color=00FF88&labelColor=1a1a2e)

![Recon](https://img.shields.io/badge/Subdomain%20Enum-✓-00FF88?style=flat-square)
![XSS](https://img.shields.io/badge/XSS%20Scanner-✓-00FF88?style=flat-square)
![CORS](https://img.shields.io/badge/CORS%20Check-✓-00FF88?style=flat-square)
![Git Exposure](https://img.shields.io/badge/Git%20Exposure-✓-00FF88?style=flat-square)
![API Finder](https://img.shields.io/badge/API%20Finder-✓-00FF88?style=flat-square)
![Report](https://img.shields.io/badge/Report%20Generator-✓-00FF88?style=flat-square)

</div>

---

## ⚠️ Disclaimer

**HXR is intended strictly for authorized security testing and educational purposes.**

By downloading, installing, or using this tool, you agree to the following:

- You will **only** use HXR on systems you **own** or have **explicit written permission** to test — such as a signed penetration testing agreement, an active bug bounty program scope, a personal lab environment, or a CTF challenge.
- You will **not** use HXR to scan, probe, or attack any system without prior authorization from the owner.
- Unauthorized use of this tool against third-party systems is **illegal** and may violate laws including but not limited to:
  - 🇮🇩 **UU ITE No. 11/2008** (Indonesia)
  - 🇺🇸 **Computer Fraud and Abuse Act (CFAA)** (United States)
  - 🇬🇧 **Computer Misuse Act 1990** (United Kingdom)
  - And equivalent cybercrime laws in your jurisdiction.
- The author **assumes zero liability** for any damage, legal consequences, or misuse resulting from this tool. You are solely responsible for your own actions.

> If you're unsure whether your target is in scope — it's not. Don't do it.

---

## 📖 About

**HXR** is a modular Python-based security reconnaissance framework built to streamline the bug bounty hunting and penetration testing workflow. It combines multiple recon and scanning modules into a single interactive terminal interface — from subdomain enumeration and technology fingerprinting, to parameter crawling, basic vulnerability scanning, and automated report generation.

HXR runs natively on all major platforms — Linux, Windows, macOS, and Termux (Android) — with a clean terminal UI and automatic dependency handling on first launch.

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 🔍 **Target Reconnaissance** | Subdomain enumeration, DNS records, technology fingerprinting |
| 🕷️ **Parameter Discovery** | Web crawler, form extraction, hidden parameter detection |
| 📸 **Screenshot Automation** | Visual documentation via Selenium + HTTP fallback |
| 🛡️ **Vulnerability Scanner** | XSS, Open Redirect, CORS misconfiguration, Git exposure |
| 🔗 **API Endpoint Finder** | JavaScript analysis & API endpoint mining |
| 📄 **Report Generator** | Export scan results to TXT & JSON |
| 🗂️ **Report Archive** | Browse and manage previous scan reports |

---

## 🕷️ Parameter Discovery — Demo

<div align="center">

![Parameter Discovery Demo](param-discovery.gif)

</div>

---

## 📦 Requirements

Make sure you have the following installed before proceeding:

| Software | Download |
|----------|----------|
| **Python 3.7+** | [python.org/downloads](https://www.python.org/downloads/) |
| **pip** | [pip.pypa.io](https://pip.pypa.io/en/stable/installation/) |
| **Git** | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **Termux** *(Android only)* | [F-Droid](https://f-droid.org/en/packages/com.termux/) |

---

## 🚀 Installation

### 🐧 Linux
```bash
git clone https://github.com/ruyynn/hxr.git
cd hxr
pip install -r requirements.txt
python hxr.py
```

### 📱 Termux (Android)
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/ruyynn/hxr.git
cd hxr
pip install -r requirements.txt
python hxr.py
```

### 🪟 Windows
```cmd
git clone https://github.com/ruyynn/hxr.git
cd hxr
pip install -r requirements.txt
python hxr.py
```

### 🍎 macOS
```bash
brew install python git
git clone https://github.com/ruyynn/hxr.git
cd hxr
pip install -r requirements.txt
python hxr.py
```

> 💡 HXR automatically checks and installs any missing dependencies on first run.

---

## 🐛 Report a Bug / Ask a Question

Found a bug, want to request a feature, or just have a question?

| Platform | Contact |
|----------|---------|
| 🐙 **GitHub Issues** | [Open an Issue](https://github.com/ruyynn/hxr/issues) |
| 📧 **Email** | [Click Me](mailto:ruyynn25@gmail.com) |
| 📘 **Facebook** | [Facebook](https://facebook.com) |

---

<div align="center">

If HXR saved you time or helped you land a bounty, a ⭐ goes a long way.<br>
It keeps this project alive and motivates me to build more free tools for the community.

[![Star](https://img.shields.io/badge/⭐%20Star%20this%20repo-FFD700?style=for-the-badge&logo=github&logoColor=black)](https://github.com/ruyynn/hxr)
[![Follow](https://img.shields.io/badge/Follow%20for%20more-1a1a2e?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ruyynn)

<br>

*Built by [ruyynn](https://github.com/ruyynn) · For educational & authorized use only*

</div>
