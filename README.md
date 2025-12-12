

# 📝 Simple OCR App

### A lightweight, offline, Tkinter-based OCR tool powered by Tesseract

---

## 📌 Overview

The **Simple OCR App** is a clean and easy-to-use desktop application built with **Python + Tkinter**, designed to extract text from images using **Tesseract OCR**.

It includes:

* 🖼 Image preview
* 🎛 Optional preprocessing (Grayscale, Sharpen, Threshold)
* 🔍 One-click OCR
* ✍ Extracted text displayed instantly
* 💾 Export options: TXT, CSV, DOCX, Excel
* ✔ Works fully offline
* ✔ 100% Conda-friendly

Ideal for users who want a **minimal yet powerful OCR application** without web interfaces, APIs, or complicated options.

---

## 🚀 Features

### 🔤 OCR Text Extraction

* Recognizes text from images (`JPG`, `PNG`, `WEBP`, etc.)
* Uses Tesseract OCR for high-accuracy recognition

### 🧪 Image Preprocessing for Better Accuracy

Tick boxes allow enabling:

* Grayscale
* Sharpen
* Black & White threshold

### 🖥 Clean Desktop UI

* Built using Tkinter
* Simple, fast, no distractions
* Image on left, OCR text on right

### 📤 Export Text in Multiple Formats

| Format | Description                        |
| ------ | ---------------------------------- |
| TXT    | Clean text output                  |
| CSV    | Saves each line as a row           |
| DOCX   | Word document export               |
| Excel  | Saves each line into an XLSX sheet |

---

## 📦 Installation

### 1. Install Conda Environment (Optional but recommended)

```bash
conda create -n ocr python=3.10
conda activate ocr
```

### 2. Install required Python libraries

```bash
conda install -c conda-forge pillow pytesseract pandas python-docx openpyxl
```

### 3. Install the Tesseract OCR Engine

#### **Linux**

```bash
sudo apt install tesseract-ocr
```

#### **Windows**

Download & install:
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

#### **macOS**

```bash
brew install tesseract
```

---

## ▶️ Running the App

Save the script as:

```
simple_ocr_app.py
```

Run:

```bash
python simple_ocr_app.py
```

The app window will open.

---

## 🖼 How to Use

1. Click **Open Image**
2. (Optional) Enable preprocessing filters
3. Click **Run OCR**
4. Extracted text appears on the right
5. Save as TXT, CSV, DOCX, or Excel

---

## 📁 Project Structure

```
SimpleOCR/
│
├── simple_ocr_app.py
└── README.md
```

---

## 🛠 Technology Stack

| Component        | Details              |
| ---------------- | -------------------- |
| GUI              | Tkinter              |
| OCR Engine       | Tesseract            |
| Image Processing | Pillow               |
| Data Handling    | Pandas               |
| File Export      | TXT, CSV, DOCX, XLSX |

---

## ⭐ Screenshots (optional placeholders)

### App Layout

```
+---------------------------+---------------------------+
|        Image Preview      |     Extracted Text        |
|                           |                           |
+---------------------------+---------------------------+
|     [Open] [OCR] [Save]   |   Options                 |
+---------------------------+---------------------------+
```

---

## 🧩 Future Enhancements (optional)

You may request ChatGPT to add:

* Batch OCR (folder support)
* Auto-rotate / auto-crop text
* OCR bounding box overlay
* Dark mode theme
* Search + highlight text
* Built-in PDF OCR support

---

## 📜 License

MIT License
Free to use, modify, and distribute.

---

## ❤️ Credits

* **Tesseract OCR** (Google)
* **Python Tkinter**
* **Pillow** for image processing
* **ChatGPT** for code generation and documentation

---

If you'd like a **logo**, **installer (.exe)**, or **dark mode UI**, just let me know!
