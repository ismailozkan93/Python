"""
Iki yol:
*String Metodlari--->startswith,endswith,find
*fnmatch modülü

"""
import fnmatch
import os
from pathlib import Path
"""
#Stringlerin icinde\karakter varsa-->basina r harfi--> raw string
arama_klasörü=r"C:\Windows"

for k in os.listdir(arama_klasörü):
    print(k)
print("******************************")
#Simdi .exe olan dosyalari bulalim
with Path(arama_klasörü) as folder_exe:
     for dosya in folder_exe.iterdir():
         if dosya.is_file() and dosya.name.endswith(".exe"):
             print(dosya)
"""
#Fnmatch Modülü
arama_klasörü=r"C:\Windows"
desen="*.exe"
with Path(arama_klasörü) as Folder:
    for file in Folder.iterdir():
        if file.is_file() and fnmatch.fnmatch(file.name,desen):
            print(file.name)












