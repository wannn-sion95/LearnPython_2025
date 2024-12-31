import pyttsx3

# Inisialisasi engine
engine = pyttsx3.init()

# Teks yang akan dibacakan
text = "Halo, My Name is Wannn Sion."
print("Halo, My Name is Wannn Sion.")

# Mengatur kecepatan bicara
engine.setProperty('rate', 150)  # Default sekitar 200 kata per menit

#  Mengubah suara ke suara wanita
# voices = engine.getProperty('voices')  # Mendapatkan daftar suara
# engine.setProperty('voice', voices[1].id)  # Menggunakan suara wanita


# Mengatur volume
engine.setProperty('volume', 1.0)  # Volume berkisar antara 0.0 hingga 1.0

# Memulai text-to-speech
engine.say(text)

# Menutup engine setelah selesai
engine.runAndWait()
