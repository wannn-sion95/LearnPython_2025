from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# load model
model = YOLO("yolov8n.pt")

# fungsi untuk buka gambar dan deteksi objek


def deteksi_gambar():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png")])
    if filepath:
        result = model(filepath)
        hasil_gambar = result[0].plot()

        # hasil deteksi
        cv2.imwrite("Hasil GUI.jpg", hasil_gambar)

        # Konversi ke format PIL untuk ditampilkan di Tkinter
        hasil_rgb = cv2.cvtColor(hasil_gambar, cv2.COLOR_BGR2RGB)
        hasil_pil = Image.fromarray(hasil_rgb)
        hasil_tk = ImageTk.PhotoImage(hasil_pil)

        # untuk update label gambar
        label_img.config(Image=hasil_tk)
        label_img.image = hasil_tk


# GUI nya
root = tk.Tk()
root.title("Deteksi objek menggunakan YOLOv8")

btn_pilih = tk.Button(
    root, text="Pilih Gambar dan deteksi", command=deteksi_gambar)
btn_pilih.pack()

label_img = tk.Label(root)
label_img.pack()

root.mainloop()
