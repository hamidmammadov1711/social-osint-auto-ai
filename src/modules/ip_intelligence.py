import requests
from src.utils.logger import logger

class IPIntelligence:
    def __init__(self):
        self.base_url = "http://ip-api.com/json/"

    def analyze(self, ip_or_domain):
        logger.info(f"Analyzing IP/Domain: {ip_or_domain}...")
        try:
            response = requests.get(f"{self.base_url}{ip_or_domain}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query")
            data = response.json()
            
            if data.get("status") == "success":
                logger.info(f"[+] Found info for {data.get('query')}: {data.get('city')}, {data.get('country')}")
                return data
            else:
                logger.error(f"[-] API Error: {data.get('message')}")
        except Exception as e:
            logger.error(f"[X] Failed to analyze IP: {e}")
        
        return None

ip_intel = IPIntelligence()
