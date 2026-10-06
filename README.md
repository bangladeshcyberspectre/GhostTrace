```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  ░██████╗░██╗░░██╗░█████╗░░██████╗████████╗████████╗██████╗░░█████╗░░  ║
║  ██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗  ║
║  ██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░░░░██║░░░██████╔╝███████║  ║
║  ██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░░░░██║░░░██╔══██╗██╔══██║  ║
║  ╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░██║░░░██║░░██║██║░░██║  ║
║  ░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝  ║
║                                                                          ║
║          👻  GhostTrace — IP Tracker & Geolocation Hunter  👻           ║
║          Team   : Bangladesh Cyber Spectre (BCS)                        ║
║          Coder  : Ochena Gamer                                          ║
║          Version: 1.0.0                                                 ║
║                                                                         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 👻 About

**GhostTrace** is an interactive IP tracking and geolocation tool built by **Ochena Gamer** for **Bangladesh Cyber Spectre (BCS)**.

Feed it any IP address or domain name — GhostTrace traces it across multiple APIs, pulls every piece of geolocation and network data available, runs a reverse DNS lookup, and generates a Google Maps link. No flags. No complexity. Just run and trace.

---

## ⚡ Features

- ✅ **Interactive UI** — no command-line arguments needed
- ✅ **IP & Domain support** — resolves domains automatically
- ✅ **Multi-API fallback** — ip-api.com → ipwho.is → freeipapi.com
- ✅ **Reverse DNS lookup** — hostname resolution
- ✅ **Google Maps link** — auto-generated from coordinates
- ✅ **Proxy / VPN detection**
- ✅ **Mobile / Hosting detection**
- ✅ **Color-coded output** — easy to read at a glance
- ✅ **Export to .txt** — auto-named per target
- ✅ **Multi-trace** — trace again without restarting
- ✅ **Loading animation** — clean, minimal UX

---

## 📊 Data Collected

| Field         | Description                        |
|---------------|------------------------------------|
| IP Address    | Resolved IP                        |
| Country       | Country name + country code        |
| Region        | State / Division                   |
| City          | City name                          |
| ZIP Code      | Postal code                        |
| Latitude      | GPS latitude                       |
| Longitude     | GPS longitude                      |
| Timezone      | e.g. Asia/Dhaka                    |
| ISP           | Internet Service Provider          |
| Organization  | Registered organization            |
| ASN           | Autonomous System Number           |
| ASN Name      | AS organization name               |
| Mobile        | Mobile network? Yes / No           |
| Proxy / VPN   | Behind proxy or VPN? Yes / No      |
| Hosting       | Datacenter / hosting? Yes / No     |
| Reverse DNS   | Hostname for the IP                |
| Google Maps   | Direct map link                    |

---

## 🛠 Installation

```bash
git clone https://github.com/bangladeshcyberspectre/GhostTrace.git
cd ghosttrace
pip install -r requirements.txt
python ghosttrace.py
```

---

## 🚀 Usage

```bash
python ghosttrace.py
```

GhostTrace will ask:

```
❯ Target IP or Domain  : 8.8.8.8
❯ Save result to file? : y
❯ Output filename      : ghosttrace_8.8.8.8_143055.txt
```

Then traces and prints full results with Google Maps link.

---

## 📁 Project Structure

```
ghosttrace/
├── ghosttrace.py      ← Main tool (run this)
├── requirements.txt   ← Python dependencies
├── README.md          ← Documentation
└── LICENSE            ← MIT License
```

---

## 📦 Requirements

- Python 3.8+
- `requests`
- `colorama`
- `urllib3`

---

## ⚠️ Accuracy Note

| Data           | Accuracy           |
|----------------|--------------------|
| Country        | ~99% accurate      |
| City / Region  | ~70–80% accurate   |
| Exact location | ISP-level only     |
| VPN/Proxy IP   | Shows VPN location |

> Real-time GPS tracking is not possible via IP alone. GhostTrace gives ISP-level geolocation — the most accurate publicly available data.

---

## ⚠️ Legal Notice

For **authorized security research and network analysis only**. Only trace IPs and domains you own or have explicit permission to investigate.

---

## 👥 Team

```
Tool    : GhostTrace
Team    : Bangladesh Cyber Spectre (BCS)
Coder   : Ochena Gamer
Version : 1.0.0
```

---

*Bangladesh Cyber Spectre — Strike clean. Deliver sharp.*
