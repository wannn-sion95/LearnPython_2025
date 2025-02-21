import re 
import random

chatbot = [
    "Hai, nama saya Wannn Sion", 
    "Halo, nama saya Wannn Sion, ada yang bisa saya bantu?", 
    "Hai, saya Wannn Sion, apa yang bisa saya bantu?",
    "Halo, saya Wannn Sion, bagaimana kabarmu?",
    "Hai, saya Wannn Sion, ada yang bisa saya bantu?",
    "Halo, ada yang bisa saya bantu"
]

tanya_kabar = [
    "Alhamdulillah, aku sehat. Bagaimana denganmu?", 
    "Kabarku baik, kalau kamu gimana?", 
    "Aku baik, kamu gimana?", 
    "Alhamdulillah, aku sehat. Bagaimana denganmu?",
    "Saya baik, kalau kabar kamu gimana?", 
    "Aku baik, kalau kabar kamu gimana?"
]
balasan_kabar = [
    "Alhamdulillah, kalau begitu",
    "Senang mendengarnya",
    "Syukurlah, semoga kamu sehat selalu ya"
]
pengenalan = [
    "Hai, namaku Wannn Sion, kalau kamu namanya siapa?", 
    "Haloo, namaku Wannn Sion, kalau kamu?", 
    "Halo, namaku Wannn Sion, kamu bisa juga panggil aku Wannn",
    "Namaku Wannn Sion, kalau kamu?", 
    "Hai, aku Wannn Sion, kamu bisa panggil aku Wannn"
]
tanya_nama = [
    "Nama kamu keren!!!",
    "Nama kamu bagus banget!!!",
    "Nama kamu unik!!!",
    "Nama kamu lucu!!!",          
]
terimakasih = [
    "Sama-sama, semoga harimu menyenangkan. Sampai jumpa!", 
    "Jangan bosan tanya-tanya ya, sampai jumpa!",
    "Senang bisa membantumu ^_^", 
    "Senang bisa membantumu, sampai jumpa!"
]

while True:
    user_input = input("You\t: ")
    
    if re.findall(r'Halo|Hai|Anyeonghaseo|oi|Hi|Aloo|Woi|Hei|Yo|hai|hei|halo|anyeonghaseo|Sumimase|sumimase|woi|aloo|hi|yo|hei|oi', user_input):
        print("Wannn Sion\t: ", random.choice(chatbot))
    elif re.findall(r'apa kabar|gimana kabarmu|kabar kamu gimana|apa kabarmu|kamu sehat?|kamu baik?', user_input):
        print("Wannn Sion\t: ", random.choice(tanya_kabar))
    elif re.findall(r"baik juga|aku baik|aku sehat|sehat juga|saya baik|saya sehat|Alhamdulillah", user_input):
        print("Wannn Sion\t: ", random.choice(balasan_kabar))
    elif re.findall(r'Nama kamu siapa?|Siapa nama kamu?|Kamu siapa?|Siapa kamu?|kamu siapa|nama kamu siapa|siapa nama kamu|kamu ini apa|siapa kamu', user_input):
        print("Wannn Sion\t: ", random.choice(pengenalan))
    elif re.findall(r'',user_input):
        print("Wannn Sion\t: ", random.choice(tanya_nama))
    elif re.findall(r'Makasih banyak', user_input):
        print("Wannn Sion\t: ", random.choice(terimakasih))
    else:
        print("Wannn Sion\t: Maaf, saya tidak mengerti. Silahkan tanya sesuatu yang lain.")
    
    if user_input.lower() in ['exit', 'quit', 'keluar']:
        print("Wannn Sion\t: Sampai jumpa!")
        break
