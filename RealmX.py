#!/usr/bin/env python3
import os
import sys
import time
import random
import webbrowser
from colorama import init, Fore, Back, Style

# --- Initialize for Android/Pydroid ---
init(autoreset=True)
IS_ANDROID = "ANDROID_ROOT" in os.environ
STORAGE_DIR = "/storage/emulated/0/RealmX" if IS_ANDROID else "./"

# --- RealmX Branding ---
TOOL_NAME = "RealmX"
VERSION = "v2.1"
SLOGAN = "X Marks the Hack"
DEVELOPER = "The Realm of Classic Hackers"
FB_PAGE = "https://www.facebook.com/profile.php?id=61555424416864"
PASSWORD = "Th3 Realm of Classic Hackers"

# --- Disclaimer ---
DISCLAIMER = f"""
{Fore.RED}╔════════════════════════════════════════╗
║ {Style.BRIGHT}FOR EDUCATIONAL USE ONLY!{Style.NORMAL}          ║
║ Unauthorized access is illegal.          ║
╚════════════════════════════════════════╝{Style.RESET_ALL}"""

# ======================
# CORE FUNCTIONALITY
# ======================

def glitch_text(text, delay=0.05):
    """Android-compatible glitch effect"""
    for _ in range(3):
        glitched = "".join(random.choice([c.upper(), c.lower()]) for c in text)
        print(f"\r{Fore.GREEN}{glitched}{Style.RESET_ALL}", end="", flush=True)
        time.sleep(delay)
    print(f"\r{text}")

def android_loading(msg, duration=2):
    """Mobile-friendly loading animation"""
    icons = ["[■□□□]", "[■■□□]", "[■■■□]", "[■■■■]"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for icon in icons:
            print(f"\r{Fore.CYAN}{msg} {icon}{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.2)

def show_banner():
    os.system("clear" if IS_ANDROID else "cls")
    print(f"""{Fore.GREEN}
    ██████╗ ███████╗ █████╗ ██╗  ██╗███╗   ███╗{Fore.YELLOW}╔═╗
    ██╔══██╗██╔════╝██╔══██╗██║  ██║████╗ ████║{Fore.YELLOW}║ ║
    ██████╔╝█████╗  ███████║███████║██╔████╔██║{Fore.YELLOW}║ ║
    ██╔══██╗██╔══╝  ██╔══██║██╔══██║██║╚██╔╝██║{Fore.YELLOW}║ ║
    ██║  ██║███████╗██║  ██║██║  ██║██║ ╚═╝ ██║{Fore.YELLOW}╚═╝
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
    {Fore.CYAN}{DEVELOPER}
    {Fore.MAGENTA}{SLOGAN}{Style.RESET_ALL}
    """)

# ======================
# PASSWORD & STORAGE
# ======================

def check_storage():
    """Ensure Android storage permissions"""
    if IS_ANDROID and not os.path.exists(STORAGE_DIR):
        try:
            os.makedirs(STORAGE_DIR)
            android_loading("Configuring Android Storage")
            print(f"{Fore.GREEN}[+] Created: {STORAGE_DIR}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Storage Error: {e}{Style.RESET_ALL}")
            sys.exit(1)

def password_gate():
    attempts = 0
    while attempts < 2:
        show_banner()
        print(DISCLAIMER)
        glitch_text(f"\n{TOOL_NAME} {VERSION} - Access Portal")
        
        password = input(f"\n{Fore.YELLOW}Enter Password: {Style.RESET_ALL}")
        if password == PASSWORD:
            android_loading("Authenticating")
            return True
        
        attempts += 1
        if attempts == 1:
            print(f"\n{Fore.RED}Wrong Password!{Style.RESET_ALL}")
            print(f"Visit: {Fore.CYAN}{FB_PAGE}{Style.RESET_ALL}")
            time.sleep(3)
        else:
            choice = input(f"{Fore.RED}Contact for password? (Y/N): {Style.RESET_ALL}")
            if choice.lower() == "y":
                webbrowser.open(FB_PAGE)
            sys.exit(0)
    return False

# ======================
# COMPLETE TOOL DATABASE
# ======================

TOOLS = {
    # Format: ["Tool Name", "GitHub URL", "Install Command", "Needs Root"]
    "Brute Force": [
        ["Hydra", "https://github.com/vanhauser-thc/thc-hydra", "make && sudo make install", True],
        ["John the Ripper", "https://github.com/openwall/john", "./configure && make", False],
        ["Hashcat", "https://github.com/hashcat/hashcat", "make && sudo make install", True],
        ["Patator", "https://github.com/lanjelot/patator", "pip3 install -r requirements.txt", False],
        ["Medusa", "https://github.com/jmk-foofus/medusa", "./configure && make", True]
    ],
    "Phishing": [
        ["SocialFish", "https://github.com/UndeadSec/SocialFish", "pip3 install -r requirements.txt", False],
        ["SEToolkit", "https://github.com/trustedsec/social-engineer-toolkit", "python setup.py", False],
        ["Evilginx2", "https://github.com/kgretzky/evilginx2", "make && sudo make install", True],
        ["Gophish", "https://github.com/gophish/gophish", "go build", False],
        ["BlackEye", "https://github.com/thelinuxchoice/blackeye", "bash setup.sh", False]
    ],
    "Reconnaissance": [
        ["theHarvester", "https://github.com/laramies/theHarvester", "pip3 install -r requirements.txt", False],
        ["SpiderFoot", "https://github.com/smicallef/spiderfoot", "pip3 install -r requirements.txt", False],
        ["Recon-ng", "https://github.com/lanmaster53/recon-ng", "pip3 install -r REQUIREMENTS", False],
        ["Osmedeus", "https://github.com/j3ssie/osmedeus", "./install.sh", True],
        ["Maltego", "https://github.com/paterva/maltego-trx", "python setup.py install", False]
    ],
    "Vulnerability Scanners": [
        ["Nmap", "https://github.com/nmap/nmap", "./configure && make && sudo make install", True],
        ["Nikto", "https://github.com/sullo/nikto", "perl nikto.pl", False],
        ["WPScan", "https://github.com/wpscanteam/wpscan", "bundle install && rake install", False],
        ["Lynis", "https://github.com/CISOfy/lynis", "./lynis audit system", True],
        ["OpenVAS", "https://github.com/greenbone/openvas", "sudo openvas-setup", True]
    ],
    "Web Exploitation": [
        ["SQLMap", "https://github.com/sqlmapproject/sqlmap", "python3 sqlmap.py --wizard", False],
        ["XSStrike", "https://github.com/s0md3v/XSStrike", "pip3 install -r requirements.txt", False],
        ["Commix", "https://github.com/commixproject/commix", "python3 commix.py --install", False],
        ["WAFW00F", "https://github.com/EnableSecurity/wafw00f", "python setup.py install", False],
        ["JoomScan", "https://github.com/rezasp/joomscan", "perl joomscan.pl", False]
    ],
    "Wireless Attacks": [
        ["Aircrack-ng", "https://github.com/aircrack-ng/aircrack-ng", "make && sudo make install", True],
        ["Reaver", "https://github.com/t6x/reaver-wps-fork-t6x", "./configure && make", True],
        ["Wifite", "https://github.com/derv82/wifite2", "python3 setup.py install", True],
        ["Bettercap", "https://github.com/bettercap/bettercap", "sudo bettercap -eval \"help\"", True],
        ["PixieWPS", "https://github.com/wiire/pixiewps", "make && sudo make install", True]
    ],
    "Post Exploitation": [
        ["Metasploit", "https://github.com/rapid7/metasploit-framework", "./msfinstall", True],
        ["Empire", "https://github.com/BC-SECURITY/Empire", "./setup/install.sh", False],
        ["Mimikatz", "https://github.com/gentilkiwi/mimikatz", "powershell -ep bypass", True],
        ["Pupy", "https://github.com/n1nj4sec/pupy", "python setup.py install", False],
        ["CrackMapExec", "https://github.com/byt3bl33d3r/CrackMapExec", "pip3 install -r requirements.txt", True]
    ],
    "Forensics": [
        ["Autopsy", "https://github.com/sleuthkit/autopsy", "./configure && make", True],
        ["Bulk Extractor", "https://github.com/simsong/bulk_extractor", "./configure && make", True],
        ["Volatility", "https://github.com/volatilityfoundation/volatility", "python setup.py install", False],
        ["Binwalk", "https://github.com/ReFirmLabs/binwalk", "python setup.py install", True],
        ["Foremost", "https://github.com/jonstewart/foremost", "make && sudo make install", True]
    ],
    "Android Tools": [
        ["APKTool", "https://github.com/iBotPeaches/Apktool", "java -jar apktool.jar", False],
        ["JADX", "https://github.com/skylot/jadx", "./gradlew dist", False],
        ["MobSF", "https://github.com/MobSF/Mobile-Security-Framework-MobSF", "./setup.sh", False],
        ["Frida", "https://github.com/frida/frida", "pip3 install frida-tools", False],
        ["Objection", "https://github.com/sensepost/objection", "pip3 install objection", False]
    ]
}

# ======================
# TOOL INSTALLATION SYSTEM
# ======================

def install_tool(tool_info):
    name, url, cmd, needs_root = tool_info
    
    # Root check for Android
    if needs_root and IS_ANDROID and os.geteuid() != 0:
        print(f"{Fore.RED}[-] {name} requires root! Use Termux with 'su'{Style.RESET_ALL}")
        return False
    
    print(f"\n{Fore.YELLOW}[*] Installing {name}...{Style.RESET_ALL}")
    
    try:
        # Clone repo
        android_loading(f"Downloading {name}")
        os.chdir(STORAGE_DIR)
        os.system(f"git clone {url} {name.lower()}")
        
        # Install
        os.chdir(f"{name.lower()}")
        android_loading(f"Building {name}")
        
        if IS_ANDROID and "sudo" in cmd:
            cmd = cmd.replace("sudo ", "")  # Handle Android root
        
        os.system(cmd)
        
        print(f"{Fore.GREEN}[+] {name} installed at: {os.getcwd()}{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}[-] Failed: {str(e)}{Style.RESET_ALL}")
        return False

# ======================
# MENU SYSTEM
# ======================

def show_category(category):
    while True:
        show_banner()
        print(f"\n{Fore.CYAN}=== {category} ==={Style.RESET_ALL}")
        
        tools = TOOLS[category]
        for idx, tool in enumerate(tools, 1):
            root_flag = f"{Fore.RED}[ROOT]{Style.RESET_ALL}" if tool[3] else ""
            print(f"{idx}. {tool[0]} {root_flag}")
        
        print(f"\n0. Back")
        
        try:
            choice = int(input(f"\n{Fore.YELLOW}Select tool: {Style.RESET_ALL}"))
            if choice == 0:
                return
            elif 1 <= choice <= len(tools):
                if install_tool(tools[choice-1]):
                    input(f"\n{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
            time.sleep(1)

def main_menu():
    check_storage()
    if not password_gate():
        return
    
    # Android warning
    if IS_ANDROID:
        print(f"\n{Fore.YELLOW}[!] Running on Android - Some tools need root")
        print(f"Storage: {STORAGE_DIR}{Style.RESET_ALL}")
        time.sleep(2)
    
    while True:
        show_banner()
        print(f"\n{Fore.BLUE}=== RealmX Main Menu ==={Style.RESET_ALL}")
        categories = list(TOOLS.keys())
        
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        
        print(f"\n0. Exit")
        
        try:
            choice = int(input(f"\n{Fore.YELLOW}Select category: {Style.RESET_ALL}"))
            if choice == 0:
                break
            elif 1 <= choice <= len(categories):
                show_category(categories[choice-1])
        except:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
            time.sleep(1)

# ======================
# ENTRY POINT
# ======================

if __name__ == "__main__":
    try:
        main_menu()
        print(f"\n{Fore.MAGENTA}Thanks for using {TOOL_NAME}!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Shutdown detected. Cleaning up...{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Fatal error: {str(e)}{Style.RESET_ALL}")