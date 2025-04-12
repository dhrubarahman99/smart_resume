# Smart Resume: Automated Resume & QR Code Generator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-%234ea94b.svg?style=for-the-badge&logo=python&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white)

## 📝 Description
An automated app that generates personalized resumes in PDF format with an embedded QR code linking to the user's linkedin profile.

```bash
Project Structure:
script.py            # Main application file
arial/font/          # Dependencies
```

## 🚀 Quick Start

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
1. Install the fonts
2. Run the python file
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

## 📋 CV Output with QR Code (Demo)
![Image](https://github.com/user-attachments/assets/714357de-43d2-4b7e-92f6-8763cb1b36f9)
