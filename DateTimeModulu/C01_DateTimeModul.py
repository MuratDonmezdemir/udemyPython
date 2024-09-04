import locale
from datetime import datetime

# Yerel ayarı 'tr_TR.UTF-8' veya 'Turkish_Turkey.1254' olarak deneyebilirsiniz
try:
    locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

a = datetime.now()

# '%B' ayın adını büyük harflerle döndürür, düzeltildi
tam_tarih = datetime.strftime(a, '%B')
print(tam_tarih)
