import subprocess
import os
import shutil
from src.utils.logger import logger

class SocialSearch:
    def __init__(self, sherlock_path="sherlock"):
        self.sherlock_path = sherlock_path

    def search_username(self, username):
        logger.info(f"Searching for username: {username}...")
        
        # 1. Check if sherlock is a system-wide command (Common in Kali)
        if shutil.which("sherlock"):
            cmd = ["sherlock", username, "--timeout", "5", "--no-color"]
            logger.info("[+] Using system-wide Sherlock (Native Mode)")
        
        # 2. Check if it's installed as a python module
        elif self._is_module_installed("sherlock"):
            cmd = ["python3", "-m", "sherlock", username, "--timeout", "5", "--no-color"]
            logger.info("[+] Using Sherlock python module")
            
        # 3. Check local directory
        elif os.path.exists(self.sherlock_path):
            cmd = ["python3", os.path.join(self.sherlock_path, "sherlock"), username, "--timeout", "5", "--no-color"]
            logger.info("[+] Using local Sherlock installation")
            
        else:
            logger.warning("[!] Sherlock not found. Please install it with 'sudo apt install sherlock' or 'pip install sherlock'")
            return []

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            found_sites = []
            for line in result.stdout.split('\n'):
                if 'https://' in line:
                    found_sites.append(line.strip())
            
            logger.info(f"[✓] Found on {len(found_sites)} platforms.")
            return found_sites
        except Exception as e:
            logger.error(f"[X] Sherlock search failed: {e}")
            
        return []

    def _is_module_installed(self, module_name):
        try:
            subprocess.run(["python3", "-m", module_name, "--version"], capture_output=True)
            return True
        except:
            return False

social_search = SocialSearch()
