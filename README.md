To run this code successfully, follow these steps:

---

### **1. Install Required Dependencies**
Run the following command in your terminal or command prompt to install the required Python libraries:

```bash
pip install selenium webdriver-manager pytesseract pillow
```

---

### **2. Download & Configure Tesseract OCR**
Since this script uses OCR (Optical Character Recognition) to extract numbers from images, you must install **Tesseract OCR**:

#### **Windows:**
1. Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).
2. Find the installation path (usually: `C:\Program Files\Tesseract-OCR\tesseract.exe`).
3. Add this path to the system's environment variables.
4. Or manually set the path in your script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

#### **Mac (Homebrew)**
```bash
brew install tesseract
```

#### **Linux (Ubuntu/Debian)**
```bash
sudo apt install tesseract-ocr
```

---

### **3. Prepare `user_agents.json`**
This script requires a file named `user_agents.json` in the same directory. Create it and add a list of user-agent strings:

```json
[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
]
```

---

### **4. Run the Script**
Once everything is set up, execute the script using:

```bash
python script_name.py
```
(Replace `script_name.py` with the actual filename.)

---

### **5. Troubleshooting**
- **ChromeDriver Issues?**  
  Ensure that `ChromeDriverManager()` is downloading the correct version. If you face version mismatches, update Chrome and try again.
  
- **Tesseract OCR Not Working?**  
  - Check if it's installed correctly.
  - Make sure the path is correctly set in `pytesseract.pytesseract.tesseract_cmd`.

- **Selenium Not Launching?**  
  Try running:

  ```bash
  python -c "from selenium import webdriver; print(webdriver.Chrome().capabilities)"
  ```

  If this fails, reinstall `webdriver-manager`:

  ```bash
  pip uninstall webdriver-manager
  pip install webdriver-manager
  ```

---
