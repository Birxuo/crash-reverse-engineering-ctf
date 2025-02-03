from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sys
import pytesseract
from PIL import Image, ImageEnhance
import re
import json

# Configuration Constants
CONFIG = {
    "ocr_crop_area": (800, 400, 1100, 500),
    "user_agents": "user_agents.json",
    "max_retries": 5,
    "request_timeout": 30
}

class CrashMonitorPro:
    def __init__(self):
        self.driver = None
        self._initialize_driver()
        
    def _initialize_driver(self):
        """Initialize browser with optimized configuration"""
        chrome_options = Options()
        
        # Anti-Detection Configuration
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        
        # Performance Settings
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Load user agents
        self._rotate_user_agent(chrome_options)
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    def _rotate_user_agent(self, chrome_options):
        """Rotate user agent from predefined list"""
        with open(CONFIG["user_agents"]) as f:
            agents = json.load(f)
        chrome_options.add_argument(f"user-agent={random.choice(agents)}")

    def _enhance_ocr_image(self, image_path):
        """Advanced OCR processing pipeline"""
        img = Image.open(image_path)
        img = img.crop(CONFIG["ocr_crop_area"])
        
        # Image enhancement
        img = img.convert('L')
        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = img.point(lambda x: 0 if x < 200 else 255)
        
        return pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.')

    def get_crash_score(self):
        """Comprehensive score retrieval system"""
        try:
            self.driver.get("https://1xbet.com/en/allgamesentrance/crash")
            
            # Natural delay pattern
            time.sleep(random.uniform(1.2, 2.8))
            
            # Iframe handling
            iframe = WebDriverWait(self.driver, CONFIG["request_timeout"]).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'crash')]"))
            )
            self.driver.switch_to.frame(iframe)
            
            # Multi-stage detection
            detection_strategies = [
                {"type": By.CSS_SELECTOR, "selector": ".crash-multiplier__current"},
                {"type": By.XPATH, "selector": "//div[contains(@class,'multiplier')]"},
                {"type": "ocr", "method": self._enhance_ocr_image}
            ]
            
            for strategy in detection_strategies:
                try:
                    if strategy["type"] == "ocr":
                        result = self._enhance_ocr_image("ocr_capture.png")
                        match = re.search(r"\d+\.\d+", result)
                        return float(match.group()) if match else None
                    else:
                        element = WebDriverWait(self.driver, 7).until(
                            EC.visibility_of_element_located((strategy["type"], strategy["selector"]))
                        )
                        return float(element.text.split('x')[0].strip())
                except Exception as e:
                    continue
                    
            raise Exception("All detection methods failed")
            
        except Exception as e:
            self.driver.save_screenshot(f"error_{int(time.time())}.png")
            raise

    def monitor(self):
        """Professional monitoring loop"""
        retry_count = 0
        while retry_count < CONFIG["max_retries"]:
            try:
                score = self.get_crash_score()
                if score:
                    print(f"[{time.strftime('%H:%M:%S')}] Valid Score: {score}x")
                    retry_count = 0
                    time.sleep(random.gauss(3.0, 0.5))
                else:
                    raise Exception("Null score detected")
            except Exception as e:
                retry_count += 1
                print(f"Error ({retry_count}/{CONFIG['max_retries']}): {str(e)}")
                self._handle_error()
                
        print("Maximum retries exceeded. Restart recommended.")

    def _handle_error(self):
        """Error recovery mechanism"""
        self.driver.delete_all_cookies()
        time.sleep(random.uniform(3, 8))
        self.driver.refresh()

if __name__ == "__main__":
    print("""Professional Crash Monitor 8.0
    - Proxy-Free Operation
    - Advanced OCR
    - Anti-Ban Protection
    - Auto-Recovery System""")
    
    monitor = CrashMonitorPro()
    monitor.monitor()