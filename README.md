# 📱 QRify | Professional QR Code Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**QRify** is a sleek, Python-powered web application that allows users to generate custom QR codes instantly. Designed with a focus on simplicity, it provides a clean interface for creating, managing, and previewing QR codes for URLs or plain text.

---

## ✨ Key Features
* 🚀 **Instant Generation**: Convert any text or URL into a QR code in milliseconds.
* 💾 **Custom Naming**: Save your generated codes with personalized filenames.
* 🖼️ **Live Preview**: View your generated QR codes instantly on the web page.
* 🗑️ **Easy Management**: Delete unwanted QR codes directly from the interface.
* 🎨 **Clean UI**: A modern interface built with no external CSS dependencies.
* 🔒 **Lightweight**: Perfect for learning Python web development and file handling.

---

## 🛠️ Technologies & Tools
* **Python 3**: Core backend logic.
* **Flask**: For backend routing and web server management.
* **qrcode[pil]**: For QR code generation engine.
* **Pillow (PIL)**: For image processing support.
* **HTML/CSS**: For the frontend user interface.

---

## 📂 Project Structure
```text
QRify/
├── app.py              # Main Flask application logic
├── qr_codes/           # Directory where generated QR codes are stored
├── templates/
│   └── index.html      # Main web interface
└── README.md           # Project documentation
```
---

## 🚀 Quick Setup & Installation
Follow these steps to get the project running locally in 1 minute:

# 1️⃣ Clone the Repository 
```
git clone https://github.com/abhishekwood/QRify.git
```
```
cd QRify
```

# 2️⃣ Install Required Dependencies
* Ensure you have Python 3 installed, then run this single command:
```
pip install flask qrcode
```
# 3️⃣ Run the Application
```
python app.py
```
# 4️⃣ Open in Browser

Visit the following URL in your browser: 👉 https://www.google.com/search?q=http://127.0.0.1:5000/

---

## 🧠 Application Workflow 
1. Input: User enters text or a URL in the input field.
2. Filename: User provides a custom name (e.g., "my_website").
3. Generate: The system creates the QR code using the Flask backend.
4. Storage: The .png file is automatically saved in the qr_codes/ folder.
5. Display: The generated image appears instantly on the dashboard.
6. Manage: You can view all codes or delete them with one click.

---

## 🎯 Use Cases 
- Generating QR codes for websites, social media, and personal links.
- Sharing information quickly via scannable images.
- Excellent Python mini-project for developer portfolios.
- Best for learning Flask routing and local file handling concepts. 

---

## 👤 Author

**[ Lᴜᴄʏ 모 ]**

* **Github:** [@abhishekwood](https://github.com/fix-the-lucy)
* **Telegram:** [LUCY ✨](https://t.me/Fix_the_lucy)
  
---

## 📝 License

This project is licensed under the **MIT License** .
