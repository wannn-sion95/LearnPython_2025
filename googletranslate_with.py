from googletrans import Translator

translator = Translator()

text = "bro, what are you doing?"
text2 = "Where are you come from?"

translated_text = translator.translate(text=text, src='auto', dest='id').text
translated_text2 = translator.translate(text=text2, src='auto', dest='id').text

print(translated_text)
print(translated_text2)
