import googletrans
from googletrans import Translator

t = Translator()
a = t.translate("thích", src = "vi", dest = "ja")
print(a.text)