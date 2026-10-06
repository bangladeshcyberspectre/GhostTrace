#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   ░██████╗░██╗░░██╗░█████╗░░██████╗████████╗████████╗██████╗░░█████╗░░█████╗░███████╗
#   ██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
#   ██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░░░░██║░░░██████╔╝███████║██║░░╚═╝█████╗░░
#   ██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░
#   ╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝███████╗
#   ░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝
#
#   GhostTrace — IP Tracker & Geolocation Hunter
#   Team    : Bangladesh Cyber Spectre (BCS)
#   Coder   : Ochena Gamer
#   Version : 1.0.0
#

import requests
import sys
import os
import time
import socket
import json
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama -q")
    from colorama import Fore, Style, init
    init(autoreset=True)

# ── Colors ────────────────────────────────────────────────────────────────────
R   = Fore.RED
G   = Fore.GREEN
Y   = Fore.YELLOW
C   = Fore.CYAN
W   = Fore.WHITE
M   = Fore.MAGENTA
B   = Fore.BLUE
DM  = Style.DIM
BRT = Style.BRIGHT
RST = Style.RESET_ALL

# ── APIs (free, no key needed) ────────────────────────────────────────────────
APIS = [
    "http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,"
    "regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,"
    "hosting,query",
    "https://ipwho.is/{ip}",
    "https://freeipapi.com/api/json/{ip}",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}


# ── Banner ────────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    clear()
    print(f"""
{C}╔{'═'*70}╗
║{' '*70}║
║{R}  ░██████╗░██╗░░██╗░█████╗░░██████╗████████╗████████╗██████╗░░█████╗░░  {C}║
║{R}  ██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗  {C}║
║{Y}  ██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░░░░██║░░░██████╔╝███████║  {C}║
║{Y}  ██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░░░░██║░░░██╔══██╗██╔══██║  {C}║
║{G}  ╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░██║░░░██║░░██║██║░░██║  {C}║
║{G}  ░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝  {C}║
║{' '*70}║
║{W}        👻  GhostTrace — IP Tracker & Geolocation Hunter  👻          {C}║
║{' '*70}║
║{DM}   Team    : {W}Bangladesh Cyber Spectre {DM}(BCS){' '*31}{C}║
║{DM}   Coder   : {W}Ochena Gamer{' '*43}{C}║
║{DM}   Version : {W}1.0.0  {DM}|  Multi-API  |  Domain Support  |  Export{' '*10}{C}║
║{' '*70}║
╚{'═'*70}╝{RST}
""")


# ── Resolve domain → IP ───────────────────────────────────────────────────────
def resolve(target: str) -> str:
    target = target.strip()
    # strip protocol
    for prefix in ("http://", "https://", "ftp://"):
        if target.startswith(prefix):
            target = target[len(prefix):]
    target = target.split("/")[0].split("?")[0]

    # already an IP?
    try:
        socket.inet_aton(target)
        return target
    except socket.error:
        pass

    # resolve domain
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        return None


# ── Fetch from ip-api.com ─────────────────────────────────────────────────────
def fetch_ipapi(ip: str) -> dict | None:
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country," \
              f"countryCode,regionName,city,zip,lat,lon,timezone,isp,org," \
              f"as,asname,mobile,proxy,hosting,query"
        r = requests.get(url, headers=HEADERS, timeout=8)
        d = r.json()
        if d.get("status") == "success":
            return {
                "IP Address"  : d.get("query", "N/A"),
                "Country"     : d.get("country", "N/A"),
                "Country Code": d.get("countryCode", "N/A"),
                "Region"      : d.get("regionName", "N/A"),
                "City"        : d.get("city", "N/A"),
                "ZIP Code"    : d.get("zip", "N/A"),
                "Latitude"    : str(d.get("lat", "N/A")),
                "Longitude"   : str(d.get("lon", "N/A")),
                "Timezone"    : d.get("timezone", "N/A"),
                "ISP"         : d.get("isp", "N/A"),
                "Organization": d.get("org", "N/A"),
                "ASN"         : d.get("as", "N/A"),
                "ASN Name"    : d.get("asname", "N/A"),
                "Mobile"      : "Yes" if d.get("mobile") else "No",
                "Proxy / VPN" : "Yes" if d.get("proxy") else "No",
                "Hosting"     : "Yes" if d.get("hosting") else "No",
            }
    except Exception:
        pass
    return None


# ── Fetch from ipwho.is ───────────────────────────────────────────────────────
def fetch_ipwho(ip: str) -> dict | None:
    try:
        r = requests.get(f"https://ipwho.is/{ip}", headers=HEADERS, timeout=8)
        d = r.json()
        if d.get("success"):
            return {
                "IP Address"  : d.get("ip", "N/A"),
                "Country"     : d.get("country", "N/A"),
                "Country Code": d.get("country_code", "N/A"),
                "Region"      : d.get("region", "N/A"),
                "City"        : d.get("city", "N/A"),
                "ZIP Code"    : d.get("postal", "N/A"),
                "Latitude"    : str(d.get("latitude", "N/A")),
                "Longitude"   : str(d.get("longitude", "N/A")),
                "Timezone"    : d.get("timezone", {}).get("id", "N/A"),
                "ISP"         : d.get("connection", {}).get("isp", "N/A"),
                "Organization": d.get("connection", {}).get("org", "N/A"),
                "ASN"         : str(d.get("connection", {}).get("asn", "N/A")),
                "ASN Name"    : d.get("connection", {}).get("domain", "N/A"),
                "Mobile"      : "N/A",
                "Proxy / VPN" : "N/A",
                "Hosting"     : "N/A",
            }
    except Exception:
        pass
    return None


# ── Fetch from freeipapi ──────────────────────────────────────────────────────
def fetch_freeipapi(ip: str) -> dict | None:
    try:
        r = requests.get(f"https://freeipapi.com/api/json/{ip}",
                         headers=HEADERS, timeout=8)
        d = r.json()
        if d.get("ipVersion"):
            return {
                "IP Address"  : d.get("ipAddress", "N/A"),
                "Country"     : d.get("countryName", "N/A"),
                "Country Code": d.get("countryCode", "N/A"),
                "Region"      : d.get("regionName", "N/A"),
                "City"        : d.get("cityName", "N/A"),
                "ZIP Code"    : d.get("zipCode", "N/A"),
                "Latitude"    : str(d.get("latitude", "N/A")),
                "Longitude"   : str(d.get("longitude", "N/A")),
                "Timezone"    : d.get("timeZone", "N/A"),
                "ISP"         : "N/A",
                "Organization": "N/A",
                "ASN"         : "N/A",
                "ASN Name"    : "N/A",
                "Mobile"      : "N/A",
                "Proxy / VPN" : "N/A",
                "Hosting"     : "N/A",
            }
    except Exception:
        pass
    return None


# ── Reverse DNS ───────────────────────────────────────────────────────────────
def reverse_dns(ip: str) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "N/A"


# ── Google Maps link ──────────────────────────────────────────────────────────
def maps_link(lat: str, lon: str) -> str:
    try:
        float(lat); float(lon)
        return f"https://maps.google.com/?q={lat},{lon}"
    except ValueError:
        return "N/A"


# ── Print result box ──────────────────────────────────────────────────────────
def val_color(key: str, val: str) -> str:
    if val in ("N/A", ""):
        return f"{DM}{val}{RST}"
    if key == "Proxy / VPN" and val == "Yes":
        return f"{R}{val}{RST}"
    if key == "Mobile" and val == "Yes":
        return f"{Y}{val}{RST}"
    if key == "Hosting" and val == "Yes":
        return f"{M}{val}{RST}"
    if key in ("Latitude", "Longitude"):
        return f"{M}{val}{RST}"
    if key == "IP Address":
        return f"{BRT}{G}{val}{RST}"
    if key in ("Country", "City", "Region"):
        return f"{W}{val}{RST}"
    if key in ("ISP", "Organization"):
        return f"{C}{val}{RST}"
    return f"{W}{val}{RST}"


def print_result(target: str, ip: str, data: dict, rdns: str, source: str):
    print(f"\n  {C}{'═'*64}{RST}")
    print(f"  {BRT}{G}  ✓ Target Resolved & Traced{RST}")
    print(f"  {C}{'─'*64}{RST}")
    print(f"  {DM}  Target Input : {W}{target}{RST}")
    print(f"  {DM}  Resolved IP  : {G}{ip}{RST}")
    print(f"  {DM}  Reverse DNS  : {W}{rdns}{RST}")
    print(f"  {DM}  Data Source  : {Y}{source}{RST}")
    print(f"  {DM}  Traced At    : {W}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RST}")
    print(f"  {C}{'─'*64}{RST}\n")

    rows = [
        ("IP Address",   data.get("IP Address",   "N/A")),
        ("Country",      f"{data.get('Country','N/A')} ({data.get('Country Code','N/A')})"),
        ("Region",       data.get("Region",       "N/A")),
        ("City",         data.get("City",         "N/A")),
        ("ZIP Code",     data.get("ZIP Code",     "N/A")),
        ("Latitude",     data.get("Latitude",     "N/A")),
        ("Longitude",    data.get("Longitude",    "N/A")),
        ("Timezone",     data.get("Timezone",     "N/A")),
        ("ISP",          data.get("ISP",          "N/A")),
        ("Organization", data.get("Organization", "N/A")),
        ("ASN",          data.get("ASN",          "N/A")),
        ("ASN Name",     data.get("ASN Name",     "N/A")),
        ("Mobile",       data.get("Mobile",       "N/A")),
        ("Proxy / VPN",  data.get("Proxy / VPN",  "N/A")),
        ("Hosting",      data.get("Hosting",      "N/A")),
    ]

    for key, val in rows:
        vc = val_color(key, val)
        print(f"  {C}│{RST}  {DM}{key:<14}{RST}  {C}:{RST}  {vc}")

    lat = data.get("Latitude",  "N/A")
    lon = data.get("Longitude", "N/A")
    gmap = maps_link(lat, lon)

    print(f"  {C}│{RST}")
    print(f"  {C}│{RST}  {DM}{'Google Maps':<14}{RST}  {C}:{RST}  {B}{gmap}{RST}")
    print(f"  {C}{'═'*64}{RST}\n")


# ── Save result ───────────────────────────────────────────────────────────────
def save_result(target: str, ip: str, data: dict, rdns: str, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  GhostTrace — IP Tracker & Geolocation Hunter\n")
        f.write("  Bangladesh Cyber Spectre | Coded by Ochena Gamer\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Target      : {target}\n")
        f.write(f"  Resolved IP : {ip}\n")
        f.write(f"  Reverse DNS : {rdns}\n")
        f.write(f"  Traced At   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        for k, v in data.items():
            f.write(f"  {k:<16}: {v}\n")
        lat = data.get("Latitude",  "N/A")
        lon = data.get("Longitude", "N/A")
        f.write(f"\n  Google Maps  : {maps_link(lat, lon)}\n")
        f.write("\n" + "=" * 60 + "\n")


# ── Prompt ────────────────────────────────────────────────────────────────────
def prompt(label: str, default=None):
    dflt = f" {DM}[{default}]{RST}" if default is not None else ""
    while True:
        try:
            val = input(f"  {C}❯{RST} {W}{label}{dflt}{RST} : ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {Y}[!] Interrupted. Goodbye.{RST}\n")
            sys.exit(0)
        if not val and default is not None:
            return str(default)
        if val:
            return val
        print(f"    {R}[!] Cannot be empty.{RST}")


# ── Loading animation ─────────────────────────────────────────────────────────
def loading(msg: str, duration: float = 1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {C}{frames[i % len(frames)]}{RST}  {W}{msg}...{RST}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()


# ── Main trace ────────────────────────────────────────────────────────────────
def trace(target: str, save: bool, out_path: str):
    # resolve
    loading("Resolving target")
    ip = resolve(target)
    if not ip:
        print(f"\n  {R}[!] Could not resolve: {target}{RST}\n")
        return

    print(f"  {G}[✓] Resolved → {W}{ip}{RST}\n")

    # fetch data — try APIs in order
    data   = None
    source = ""

    loading("Fetching geolocation data")
    data = fetch_ipapi(ip)
    if data:
        source = "ip-api.com"
    else:
        data = fetch_ipwho(ip)
        if data:
            source = "ipwho.is"
        else:
            data = fetch_freeipapi(ip)
            if data:
                source = "freeipapi.com"

    if not data:
        print(f"  {R}[!] All APIs failed. Check connection.{RST}\n")
        return

    loading("Running reverse DNS lookup")
    rdns = reverse_dns(ip)

    print_result(target, ip, data, rdns, source)

    if save:
        save_result(target, ip, data, rdns, out_path)
        print(f"  {C}[*] Saved → {W}{out_path}{RST}\n")


# ── Config prompt ─────────────────────────────────────────────────────────────
def gather_config():
    print_banner()
    print(f"  {Y}{'─'*64}{RST}")
    print(f"  {BRT}{W}   Enter target below. IP address or domain — both work.{RST}")
    print(f"  {Y}{'─'*64}{RST}\n")

    target   = prompt("Target IP or Domain  (e.g. 8.8.8.8 or google.com)")

    save_ans = prompt("Save result to file? (y/n)", default="y")
    save     = save_ans.lower() in ("y", "yes")
    out_path = ""
    if save:
        clean = target.replace("http://","").replace("https://","").split("/")[0]
        default_out = f"ghosttrace_{clean}_{datetime.now().strftime('%H%M%S')}.txt"
        out_path = prompt("Output filename", default=default_out)

    return {"target": target, "save": save, "out_path": out_path}


# ── Entry ─────────────────────────────────────────────────────────────────────
def main():
    while True:
        cfg = gather_config()
        trace(cfg["target"], cfg["save"], cfg["out_path"])

        print(f"  {C}╔{'═'*62}╗{RST}")
        print(f"  {C}║{'  GhostTrace — Bangladesh Cyber Spectre | Ochena Gamer':^62}║{RST}")
        print(f"  {C}╚{'═'*62}╝{RST}\n")

        try:
            again = input(f"  {C}❯{RST} {W}Trace another target? (y/n){RST} : ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            again = "n"

        if again not in ("y", "yes"):
            print(f"\n  {Y}[*] GhostTrace shutting down. Stay invisible.{RST}\n")
            break


if __name__ == "__main__":
    main()
