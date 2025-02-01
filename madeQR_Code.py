import qrcode

# Link atau teks yang ingin diubah menjadi QR Code
link = "https://github.com/wannn-sion95"

# Membuat QR Code
qr = qrcode.make(link)

# Menyimpan QR Code sebagai gambar
qr.save("qrcode_myGithub.png")
