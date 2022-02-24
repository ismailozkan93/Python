"""
Python'da dosyalari:
*Yeniden adlandirma(rename)
*silme
*yaratma
os modulü ile yapilir
"""
import os
try:
    os.rename("WillBeDeleted2.txt", "BeforeDeleteRename.txt")
except:
    print("Dosya bulunamadi")

#Silme-->remove(),unlink
#os.remove("BeforeDeleteRename.txt")
#os.unlink("DeleteUnlink.txt")

#Create File
with open("DeleteUnlink.txt",mode="x") as File:
    File.write("Bu dosya open(mode=x) ile olusturuldu")

"""
Encoding:
cp1254-->Windows'un Türkce Encoding Formati

OS encodingleri ile ugrasmamak icin --> open() islemlerinde-->encoding=""utf
"""