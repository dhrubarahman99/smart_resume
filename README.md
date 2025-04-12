# Smart Resume: Automated Resume & QR Code Generator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-%234ea94b.svg?style=for-the-badge&logo=python&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white)
![MIT License](https://img.shields.io/badge/license-MIT-blue)

## 📝 Description
A Python application (`script.py`) that generates professional CVs in PDF format with a modern Tkinter GUI interface.

```bash
Project Structure:
script.py            # Main application file
requirements.txt     # Dependencies
assets/              # Optional folder for screenshots
```

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Requirements
```text
fpdf2>=2.7.4
pyqrcode>=1.2.1
pypng>=0.0.20
```

## 🖥️ GUI Interface
![Image](https://github.com/user-attachments/assets/a799267c-c787-40a3-8ded-0c1cabf43667)

### Sections:
1. **Personal Information**
2. **Skills List**
3. **Work Experience**
4. **Education**
5. **About Me**

## 💻 Usage
Run the application:
```bash
python script.py
```

Example workflow:
1. Fill in your details
2. Click "Generate CV"
3. Find `cv.pdf` in your directory

## 🛠 Configuration
Edit these in `script.py`:

```python
# File Output Paths
QR_PATH = "my-qr.png"    # QR code save location 
PDF_PATH = "resume.pdf"  # Output PDF path

# UI Theme
THEME = {
    "bg": "#f5f7fa",
    "fg": "#2d3748", 
    "accent": "#4f46e5",
    "font": ("Segoe UI", 10)
}
```

## 📋 Example Data
```text
Name: John Doe
Email: john@example.com
Skills: Python, Data Analysis
Experience: Data Scientist: Built ML models
Education: PhD: Stanford University
About Me: Passionate developer...
```

### Key Features:
1. **Complete Markdown Formatting** - Headers, code blocks, lists
2. **Visual Elements** - Badges, screenshot reference
3. **Structured Sections** - Clear hierarchy with emoji icons
4. **Ready-to-Use** - Includes installation and usage examples
5. **Technical Details** - Configuration options and requirements

