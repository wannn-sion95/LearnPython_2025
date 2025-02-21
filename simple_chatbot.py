import re 
import random

chatbot = ["Hai, nama saya Wannn Sion", "Halo, nama saya Wannn Sion, ada yang bisa saya bantu?", "Hai, saya Wannn Sion, apa yang bisa saya bantu?",
          "Halo, saya Wannn Sion, bagaimana kabarmu?","Hai, saya Wannn Sion, ada yang bisa saya bantu?","Halo, ada yang bisa saya bantu"]

tanya_kabar = ["Alhamdulillah, aku sehat. Bagaimana denganmu?", "kabarku Baik, kalau kamu gimana", "Aku baik, kamu gimana?", "Alhamdulillah, aku sehat. Bagaimana denganmu?"
              "Saya baik, kalau kabar kamu gimana?", "Aku baik, kalau kabar kamu gimana?"]

pengenalan = ["Hai, namaku Wannn Sion, kalau kamu nama kamu siapa?", "Haloo, namaku Wannn Sion, kalau kamu?", "Halo, namaku Wannn Sion, kamu bisa juga panggil aku Wannn",
             "Namaku wannn Sion, kalau kamu?", "Hai, aku Wannn Sion, kamu bisa panggil aku Wannn"]
              

terimakasih = ["Sama-sama, semoga harimu menyenangkan.Sampai jumpa!", "Jangan bosan tanya-tanya ya, sampai jumpa!"
              "Senang bisa membantumu ^_^", "Senang bisa membantumu, sampai jumpa!"]

while True:
  user_input = input("You\t: ")
  
  if re.findall(r'Halo|Hai|Anyeonghaseo|oi|Hi|Aloo|Woi|Hei|Yo|hai|hei|halo|anyeonghaseo|Sumimase|sumimase|woi|aloo|hi|yo|hei|oi', user_input):
    print("Wannn Sion\t: ",random.choice(chatbot))
  elif re.findall(r'apa kabar|gimana kabarmu|kabar kamu gimana|apa kabarmu|kamu sehat?|kamu baik?|', user_input):
    print("Wannn Sion\t: ", random.choice(tanya_kabar))
  elif re.findall(r"Nama kamu siapa?|Siapa nama kamu?|Kamu siapa?|Siapa kamu?", user_input):
    print("Wannn Sion\t: ", random.choice(pengenalan))
  elif re.findall(r'Makasih banyak', user_input):
    print("Wannn Sion\t: ", random.choice(terimakasih))
  else:
    print("Wannn Sion\t: Maaf, saya tidak mengerti. Silahkan tanya sesuatu yang lain.")
