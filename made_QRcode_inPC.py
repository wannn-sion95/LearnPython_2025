import qrcode
import os

# Link yang diinginkan untuk membuat code QR
link = "https://github.com/wannn-sion95"

# Code pembuatan QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(link)
qr.make(fit=True)

# Membuat gambar QR code
img = qr.make_image(fill="yellow", back_color="white")

# Menyimpan gambar QR code di direktori PC anda
qr_image_path = "C:\\Users\\asus\\Downloads\\QRCode_myGithub.png"  # Ganti dengan path yang sesuai PC anda

# Memastikan direktori ada
os.makedirs(os.path.dirname(qr_image_path), exist_ok=True)

try:
    img.save(qr_image_path)
    print(f"QR code image saved successfully at {qr_image_path}")
except Exception as e:
    print(f"Failed to save QR code image: {e}")

# Menampilkan gambar
img.show()
