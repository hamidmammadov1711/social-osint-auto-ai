import subprocess
import shutil
from src.utils.logger import logger

class EmailChecker:
    def check(self, email):
        logger.info(f"Checking email: {email} using Holehe...")
        
        # Check if holehe is a system-wide command (Common in Kali)
        if shutil.which("holehe"):
            cmd = ["holehe", email, "--only-used", "--no-color"]
            logger.info("[+] Using system-wide Holehe (Native Mode)")
        else:
            # Fallback to python module
            cmd = ["python3", "-m", "holehe", email, "--only-used", "--no-color"]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stdout
            found_services = []
            
            for line in output.split('\n'):
                if '✅' in line or 'used' in line.lower():
                    service = line.split('|')[0].strip() if '|' in line else line.strip()
                    found_services.append(service)
            
            if found_services:
                logger.info(f"[✓] Email found on {len(found_services)} services.")
            else:
                logger.warning("[!] No services found for this email.")
                
            return found_services
        except Exception as e:
            logger.error(f"[X] Email check failed: {e}")
            
        return []

email_checker = EmailChecker()
