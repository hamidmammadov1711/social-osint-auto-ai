#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
███████╗ ██████╗  ██████╗██╗ █████╗ ██╗         ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║         ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
███████╗██║   ██║██║     ██║███████║██║         ██████╔╝█████╗  ██║██╔██╗ ██║   ██║   
╚════██║██║   ██║██║     ██║██╔══██║██║         ██╔══██╗██╔══╝  ██║██║╚██╗██║   ██║   
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗    ██║  ██║██║     ██║██║ ╚████║   ██║   
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                                       
███████╗░█████╗░██████╗░██╗██████╗░████████╗     █████╗░██╗░░░██╗████████╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝██████╦╝██║██████╔╝░░░██║░░░    ███████║██║░░░██║░░░██║░░░██║░░██║
██╔══╝░░██║░░██╗██╔══██╗██║██╔══██╗░░░██║░░░    ██╔══██║██║░░░██║░░░██║░░░██║░░██║
███████╗╚█████╔╝██║░░██║██║██║░░██║░░░██║░░░    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

Author: OSINT Professional [Hamid Mammadov]
Vesion: 2.0
License: Only educative use
"""

import os
import sys
import subprocess
import json
import time
import requests
import re
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# ======================= RƏNGLƏR =======================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLACK = '\033[30m'
    MAGENTA = '\033[35m'
    WHITE = '\033[97m'

# ======================= BANNER =======================
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Colors.CYAN + """
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║   ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗      ██████╗ ███████╗██╗███╗   ██╗████████╗ ║
║   ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║      ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝ ║
║   ███████╗██║   ██║██║     ██║███████║██║      ██████╔╝█████╗  ██║██╔██╗ ██║   ██║    ║
║   ╚════██║██║   ██║██║     ██║██╔══██║██║      ██╔══██╗██╔══╝  ██║██║╚██╗██║   ██║    ║
║   ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗ ██║  ██║██║     ██║██║ ╚████║   ██║    ║
║   ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝   ╚═╝    ║
║                                                                                       ║
║                                                                                       ║    
║                      AVTOMATLAŞDIRILMIŞ OSINT ALƏTİ                                   ║
║                           Versiya 2.0 - Kali Linux                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
    """ + Colors.END)
    print(Colors.YELLOW + "[!] Bu alət YALNIZ təhsil məqsədləri üçündür!" + Colors.END)
    print(Colors.RED + "[!] İcazəsiz istifadə qanun pozuntusudur!" + Colors.END)
    print(Colors.GREEN + "[✓] Müəllif heç bir qanunsuz fəaliyyətə görə məsuliyyət daşımır\n" + Colors.END)

# ======================= ANONİMLİK FUNKSİYALARI =======================
def mac_changer():
    """MAC ünvanını dəyişdirir"""
    print(Colors.CYAN + "[*] MAC ünvanı dəyişdirilir..." + Colors.END)
    try:
        interface = subprocess.getoutput("ip route | grep default | awk '{print $5}' | head -1")
        if interface:
            subprocess.run(f"sudo ifconfig {interface} down", shell=True, capture_output=True)
            subprocess.run(f"sudo macchanger -r {interface}", shell=True, capture_output=True)
            subprocess.run(f"sudo ifconfig {interface} up", shell=True, capture_output=True)
            print(Colors.GREEN + f"[✓] MAC ünvanı dəyişdirildi: {interface}" + Colors.END)
            return True
    except Exception as e:
        print(Colors.RED + f"[✗] MAC dəyişdirilə bilmədi: {e}" + Colors.END)
        return False

def tor_proxy():
    """Tor proxy-ni işə salır"""
    print(Colors.CYAN + "[*] Tor proxy aktivləşdirilir..." + Colors.END)
    try:
        subprocess.run("sudo systemctl start tor", shell=True, capture_output=True)
        time.sleep(3)
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        test = requests.get('https://check.torproject.org', proxies=proxies, timeout=10)
        if "Congratulations" in test.text:
            print(Colors.GREEN + "[✓] Tor proxy aktivdir!" + Colors.END)
            return proxies
        else:
            print(Colors.RED + "[✗] Tor işləmir, davam edilir..." + Colors.END)
            return None
    except:
        print(Colors.RED + "[✗] Tor bağlantısı uğursuz!" + Colors.END)
        return None

# ======================= SHERLOCK İNTEGRASİYASI =======================
def sherlock_search(username):
    """Username-i 300+ platformada axtarır"""
    print(Colors.CYAN + f"\n[*] '{username}' username-i axtarılır..." + Colors.END)
    
    if not os.path.exists("sherlock"):
        print(Colors.YELLOW + "[!] Sherlock tapılmadı, yüklənir..." + Colors.END)
        subprocess.run("git clone https://github.com/sherlock-project/sherlock.git", shell=True)
        subprocess.run("cd sherlock && pip3 install -r requirements.txt", shell=True)
    
    cmd = f"cd sherlock && python3 sherlock {username} --timeout 5 --no-color 2>/dev/null"
    result = subprocess.getoutput(cmd)
    
    found_sites = []
    for line in result.split('\n'):
        if '[' in line and ']' in line and 'https://' in line:
            site_name = line.split('[')[1].split(']')[0]
            found_sites.append(site_name)
    
    if found_sites:
        print(Colors.GREEN + f"[✓] {len(found_sites)} platformada tapıldı:" + Colors.END)
        for site in found_sites[:15]:  # İlk 15-i göstər
            print(f"    → {site}")
        return found_sites
    else:
        print(Colors.RED + "[✗] Heç bir platformada tapılmadı!" + Colors.END)
        return []

# ======================= HOLEHE İNTEGRASİYASI =======================
def holehe_check(email):
    """Email ünvanını yoxlayır"""
    print(Colors.CYAN + f"\n[*] '{email}' email-i yoxlanılır..." + Colors.END)
    
    try:
        subprocess.run("pip3 install holehe -q", shell=True, capture_output=True)
        cmd = f"holehe {email} --only-used --no-color 2>/dev/null"
        result = subprocess.getoutput(cmd)
        
        found_services = []
        phone_numbers = []
        
        for line in result.split('\n'):
            if '✅' in line or 'used' in line.lower():
                service = line.split('|')[0].strip()
                found_services.append(service)
            if 'phone' in line.lower() and '+' in line:
                phone_numbers.append(line)
        
        if found_services:
            print(Colors.GREEN + f"[✓] Email {len(found_services)} xidmətdə istifadə olunur:" + Colors.END)
            for svc in found_services[:10]:
                print(f"    → {svc}")
            if phone_numbers:
                print(Colors.MAGENTA + f"[+] Telefon nömrəsi tapıldı: {phone_numbers[0]}" + Colors.END)
            return found_services
        else:
            print(Colors.RED + "[✗] Email heç bir xidmətdə tapılmadı!" + Colors.END)
            return []
    except Exception as e:
        print(Colors.RED + f"[✗] Holehe xətası: {e}" + Colors.END)
        return []

# ======================= PHONEINFOGA İNTEGRASİYASI =======================
def phoneinfoga_check(phone):
    """Telefon nömrəsini yoxlayır"""
    print(Colors.CYAN + f"\n[*] '{phone}' nömrəsi yoxlanılır..." + Colors.END)
    
    try:
        if not os.path.exists("phoneinfoga"):
            print(Colors.YELLOW + "[!] PhoneInfoga yüklənir..." + Colors.END)
            subprocess.run("git clone https://github.com/sundowndev/phoneinfoga.git", shell=True)
            subprocess.run("cd phoneinfoga && go build -o phoneinfoga .", shell=True)
        
        cmd = f"cd phoneinfoga && ./phoneinfoga scan -n '{phone}' 2>/dev/null"
        result = subprocess.getoutput(cmd)
        
        info = {}
        if 'Valid' in result:
            info['valid'] = '✓' if 'true' in result.lower() else '✗'
        if 'Carrier' in result:
            carrier_line = [l for l in result.split('\n') if 'Carrier' in l]
            if carrier_line:
                info['carrier'] = carrier_line[0].split(':')[-1].strip()
        if 'Country' in result:
            country_line = [l for l in result.split('\n') if 'Country' in l]
            if country_line:
                info['country'] = country_line[0].split(':')[-1].strip()
        
        if info:
            print(Colors.GREEN + "[✓] Nömrə məlumatları:" + Colors.END)
            for k, v in info.items():
                print(f"    → {k}: {v}")
            return info
        else:
            print(Colors.RED + "[✗] Nömrə haqqında məlumat tapılmadı!" + Colors.END)
            return {}
    except Exception as e:
        print(Colors.RED + f"[✗] PhoneInfoga xətası: {e}" + Colors.END)
        return {}

# ======================= MAİL VERİFİKASİYASI =======================
def verify_email_instagram(email):
    """Email-in Instagram-a bağlı olub-olmadığını yoxlayır"""
    print(Colors.CYAN + f"[*] Instagram-da '{email}' yoxlanılır..." + Colors.END)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        # Instagram şifrə sıfırlama API-si
        url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
        
        # Bu sadəcə nümunədir - real implementasiya üçün daha mürəkkəb tələb olunur
        print(Colors.YELLOW + "[!] Manual yoxlama tələb olunur: instagram.com/accounts/password/reset/" + Colors.END)
        return None
    except:
        return None

# ======================= USERNAME EMAIL ƏLAQƏSİ =======================
def username_to_email_patterns(username):
    """Username-dən mümkün email pattern-ləri yaradır"""
    print(Colors.CYAN + f"[*] '{username}' üçün email pattern-ləri yaradılır..." + Colors.END)
    
    patterns = [
        f"{username}@gmail.com",
        f"{username}@yahoo.com",
        f"{username}@outlook.com",
        f"{username}@hotmail.com",
        f"{username}@mail.ru",
        f"{username}@icloud.com",
        f"{username}@protonmail.com",
        f"{username}@yandex.com",
        f"{username}@bk.ru",
        f"{username}@list.ru",
        f"{username}@inbox.ru",
        f"{username}@rambler.ru",
    ]
    
    print(Colors.GREEN + "[✓] Email pattern-ləri yaradıldı:" + Colors.END)
    for p in patterns[:10]:
        print(f"    → {p}")
    return patterns

# ======================= REKURSİV AXTARIŞ =======================
def recursive_osint(username=None, email=None, phone=None):
    """Rekursiv OSINT axtarışı"""
    results = {
        'username': username,
        'email': email,
        'phone': phone,
        'found_platforms': [],
        'email_services': [],
        'phone_info': {}
    }
    
    if username:
        results['found_platforms'] = sherlock_search(username)
    
    if email:
        results['email_services'] = holehe_check(email)
    
    if phone:
        results['phone_info'] = phoneinfoga_check(phone)
    
    return results

# ======================= NƏTİCƏLƏRİ EKSPORT ET =======================
def export_results(results, filename="osint_results.json"):
    """Nəticələri JSON faylına yazır"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(Colors.GREEN + f"\n[✓] Nəticələr '{filename}' faylına yazıldı!" + Colors.END)

# ======================= ƏSAS MENYU =======================
def main_menu():
    """Əsas menyu"""
    while True:
        banner()
        print(Colors.BOLD + "\n═══════════════════════════════════════════════════════════════" + Colors.END)
        print(Colors.CYAN + "  [1] 🔍 Username ilə axtarış" + Colors.END)
        print(Colors.GREEN + "  [2] 📧 Email ilə axtarış" + Colors.END)
        print(Colors.MAGENTA + "  [3] 📱 Telefon nömrəsi ilə axtarış" + Colors.END)
        print(Colors.YELLOW + "  [4] 🔄 Tam avtomatik axtarış (Username + Email + Nömrə)" + Colors.END)
        print(Colors.RED + "  [5] 🚪 Çıxış" + Colors.END)
        print(Colors.BOLD + "═══════════════════════════════════════════════════════════════" + Colors.END)
        
        choice = input(Colors.CYAN + "\n[?] Seçiminiz (1-5): " + Colors.END).strip()
        
        if choice == '1':
            username = input(Colors.YELLOW + "[?] Username daxil edin: " + Colors.END).strip()
            if username:
                print(Colors.CYAN + "\n[*] Anonimlik təmin edilir..." + Colors.END)
                mac_changer()
                proxies = tor_proxy()
                results = recursive_osint(username=username)
                export_results(results)
                input(Colors.CYAN + "\n[Davam etmək üçün Enter]..." + Colors.END)
        
        elif choice == '2':
            email = input(Colors.YELLOW + "[?] Email daxil edin: " + Colors.END).strip()
            if email:
                print(Colors.CYAN + "\n[*] Anonimlik təmin edilir..." + Colors.END)
                proxies = tor_proxy()
                results = recursive_osint(email=email)
                # Username email-dən çıxarılır
                username_from_email = email.split('@')[0]
                print(Colors.CYAN + f"[*] Email-dən username çıxarıldı: {username_from_email}" + Colors.END)
                more_results = recursive_osint(username=username_from_email)
                results['username_variants'] = username_from_email
                export_results(results)
                input(Colors.CYAN + "\n[Davam etmək üçün Enter]..." + Colors.END)
        
        elif choice == '3':
            phone = input(Colors.YELLOW + "[?] Telefon nömrəsi (+994XXXXXXXXX formatında): " + Colors.END).strip()
            if phone:
                print(Colors.CYAN + "\n[*] Anonimlik təmin edilir..." + Colors.END)
                proxies = tor_proxy()
                results = recursive_osint(phone=phone)
                export_results(results)
                input(Colors.CYAN + "\n[Davam etmək üçün Enter]..." + Colors.END)
        
        elif choice == '4':
            print(Colors.CYAN + "\n[!] TAM AVTOMATİK REJİM" + Colors.END)
            username = input(Colors.YELLOW + "[?] Username (varsa, yoxsa Enter): " + Colors.END).strip()
            email = input(Colors.YELLOW + "[?] Email (varsa, yoxsa Enter): " + Colors.END).strip()
            phone = input(Colors.YELLOW + "[?] Telefon (varsa, yoxsa Enter): " + Colors.END).strip()
            
            print(Colors.CYAN + "\n[*] Anonimlik təmin edilir..." + Colors.END)
            mac_changer()
            proxies = tor_proxy()
            
            all_results = {}
            
            if username:
                all_results['username_search'] = recursive_osint(username=username)
            
            if email:
                all_results['email_search'] = recursive_osint(email=email)
                # Email-dən username pattern-ləri yarat
                username_from_email = email.split('@')[0]
                print(Colors.CYAN + f"[*] Email-dən username yaradıldı: {username_from_email}" + Colors.END)
                email_username_results = recursive_osint(username=username_from_email)
                all_results['email_username_search'] = email_username_results
            
            if phone:
                all_results['phone_search'] = recursive_osint(phone=phone)
            
            # Email pattern-ləri yarat
            if username:
                patterns = username_to_email_patterns(username)
                print(Colors.CYAN + "[*] Email pattern-ləri yoxlanılır..." + Colors.END)
                for pattern in patterns[:5]:  # İlk 5 pattern-i yoxla
                    pattern_results = recursive_osint(email=pattern)
                    if pattern_results.get('email_services'):
                        all_results[f'pattern_{pattern}'] = pattern_results
            
            export_results(all_results, "full_osint_results.json")
            print(Colors.GREEN + "\n[✓] Tam avtomatik axtarış tamamlandı!" + Colors.END)
            input(Colors.CYAN + "\n[Davam etmək üçün Enter]..." + Colors.END)
        
        elif choice == '5':
            print(Colors.RED + "\n[!] Çıxış edilir..." + Colors.END)
            sys.exit(0)
        
        else:
            print(Colors.RED + "\n[!] Yanlış seçim! Yenidən cəhd edin." + Colors.END)
            time.sleep(1)

# ======================= ƏSAS PROQRAM =======================
if __name__ == "__main__":
    # Root icazələrini yoxla
    if os.geteuid() != 0:
        print(Colors.RED + "\n[!] Bu proqram root icazələri tələb edir!" + Colors.END)
        print(Colors.YELLOW + "[*] Zəhmət olmasa 'sudo python3 social_osint_auto.py' ilə işə salın" + Colors.END)
        sys.exit(1)
    
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Colors.RED + "\n\n[!] Proqram dayandırıldı!" + Colors.END)
        sys.exit(0)