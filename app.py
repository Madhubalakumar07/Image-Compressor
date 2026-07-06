import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA

st.title("Image Compression using PCA")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    r, g, b = cv.split(img)
    k = st.slider(
        "Number of Principal Components",
        10,
        min(img.shape),
        100
    )
    def channel_compression(channel, k):
        pca = PCA(n_components=k)
        compressed = pca.fit_transform(channel)
        reconstructed = pca.inverse_transform(compressed)
        return np.clip(reconstructed, 0, 255).astype(np.uint8)

    compressed_b = channel_compression(b, k)
    compressed_g = channel_compression(g, k)
    compressed_r = channel_compression(r, k)

    reconstructed = cv.merge((compressed_r, compressed_g, compressed_b))

    col1, col2 = st.columns(2)

    with col1:
        st.image(img, caption="Original")

    with col2:
        st.image(reconstructed, caption="Compressed")