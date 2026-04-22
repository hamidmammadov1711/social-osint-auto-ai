import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "")
        self.HIBP_API_KEY = os.getenv("HIBP_API_KEY", "")
        self.HUNTER_API_KEY = os.getenv("HUNTER_API_KEY", "")
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.OUTPUT_DIR = "results"
        
        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)

config = Config()
