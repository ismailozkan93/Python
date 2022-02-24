"""
Bir klasör icindeki tüm dosya ve klasörleri os modülü ile okuruz
Bunlarin tipi:
*dosya
*klasör

"""

#Klasör icerigi okuma
import os
"""    
#1nci yol
dosya_yolu=os.getcwd()
icerik=os.listdir(dosya_yolu)
print(icerik)
for ic in icerik:
    print(ic)

#2nci Yol
folder=os.scandir(dosya_yolu)
for eleman in folder:
    print(eleman)

#3ncü yol
from pathlib import Path
icerik=Path(dosya_yolu)
for ic_eleman in icerik.iterdir():
    print(ic_eleman)
"""
dosya_yolu=os.getcwd()

icerik=os.listdir(dosya_yolu)
for ic in icerik:
    if os.path.isfile(ic):
        print(ic)

#2nci Yol
with os.scandir(dosya_yolu) as scans:
    for scan in scans:
        if scan.is_file():
            print(scan)

#3ncü Yol
from pathlib import Path
ana_dosya=Path(dosya_yolu)
dosya_icerigi=ana_dosya.iterdir()

for dos in dosya_icerigi:
    if dos.is_file():
        print(dos)












