# 🖼️ Image Compressor using PCA

A simple machine learning project that compresses images using **Principal Component Analysis (PCA)**. The application allows users to upload a color image, applies PCA independently to each RGB channel, reconstructs the image using a reduced number of principal components, and displays the compressed result.

## 🚀 Features

* Upload an image through a simple Streamlit interface
* Compress color images using PCA
* Adjust the number of principal components
* Display the original and reconstructed images side by side
* Demonstrates dimensionality reduction in machine learning
* Easy to understand and extend

---

## 📷 How It Works

1. Upload a color image.
2. Split the image into Red, Green, and Blue channels.
3. Apply PCA independently to each channel.
4. Reconstruct each channel using the selected number of principal components.
5. Merge the channels back into a color image.
6. Display the compressed image.

```
Input Image
      │
      ▼
Convert to RGB
      │
      ▼
Split into R, G, B Channels
      │
      ▼
Apply PCA to Each Channel
      │
      ▼
Reconstruct Channels
      │
      ▼
Merge Channels
      │
      ▼
Compressed Image
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* OpenCV
* Pillow
* Scikit-learn (PCA)

---

## 📂 Project Structure

```text
Image-Compressor/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Madhubalakumar07/Image-Compressor.git
cd Image-Compressor
```

Create a virtual environment (optional but recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the URL displayed in your terminal (usually `http://localhost:8501`) in your browser.

---

## 📖 Understanding PCA Compression

Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms data into a new coordinate system where the most significant information is captured by a smaller number of principal components.

In this project:

* Each color channel is treated as a matrix.
* PCA reduces the number of features while preserving as much information as possible.
* Fewer principal components result in higher compression but lower image quality.
* More principal components preserve image quality but reduce the compression effect.

> **Note:** This project demonstrates PCA for educational purposes. Unlike formats such as JPEG or PNG, PCA is not a practical image file compression standard.

---

## 📌 Future Improvements

* Download the compressed image
* Display compression ratio
* Add PSNR, MSE, and SSIM quality metrics
* Support grayscale mode
* Compare PCA compression with JPEG compression
* Batch image compression

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project helpful

Please consider giving the repository a **Star ⭐** on GitHub.
