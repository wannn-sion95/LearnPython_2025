import pywhatkit as kit
import datetime

now = datetime.datetime.now()

phone_number = "+6287896222827"
message = ("Hai, I'm Wannn Sion")

kit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)

print("SMS berhasil dikirim!")
