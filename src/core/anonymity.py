import subprocess
import platform
import requests
from src.utils.logger import logger

class AnonymityManager:
    def __init__(self):
        self.os_type = platform.system()

    def change_mac(self, interface=None):
        """Changes MAC address based on OS"""
        logger.info(f"Changing MAC address for OS: {self.os_type}...")
        
        if self.os_type == "Linux":
            try:
                if not interface:
                    interface = subprocess.getoutput("ip route | grep default | awk '{print $5}' | head -1")
                
                subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
                subprocess.run(["sudo", "macchanger", "-r", interface], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
                logger.info(f"[✓] MAC changed for {interface}")
                return True
            except Exception as e:
                logger.error(f"[✗] Linux MAC change failed: {e}")
        
        elif self.os_type == "Windows":
            logger.warning("[!] Automatic MAC changing on Windows requires specialized tools or Registry edits. Skipping...")
            # Note: A real pro tool might use a library or powershell script here, but it's risky to auto-run.
        
        return False

    def setup_tor(self):
        """Attempts to route traffic through Tor"""
        logger.info("Setting up Tor proxy...")
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        try:
            # Check if Tor is running
            test = requests.get('https://check.torproject.org', proxies=proxies, timeout=5)
            if "Congratulations" in test.text:
                logger.info("[✓] Tor proxy is active!")
                return proxies
        except:
            logger.warning("[!] Tor is not running or unreachable. Proceeding without Tor.")
        
        return None

anonymity = AnonymityManager()
