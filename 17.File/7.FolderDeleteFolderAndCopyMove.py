"""
1)Klasör Silme
2)Dosya ve Klasör Kopyalama
3)Dosya ve Klasör Tasima
4)Klasörü Yeniden Adlandirma
"""
import shutil
import os
import pathlib

#1-Klasör Silme
"""
*os.rmdir()-->tek klasör siler(klasör BOS ise)
*pathlib.Path.rmdir()-->tek klasör siler(klasör BOS ise)
*shutil.rmtree()-->tüm klasör agacini siler
"""
#önce silinecek klasör olustur
#os.mkdir("BeDeletedFolder")

#silinecek klasor bos oldugu icin-->os.rmdir()bunu silebilir
#os.rmdir("BeDeletedFolder")

#bos degilse -->OSERROR:[WinError 145]Dizin bos degil:"Silinecek Klasör"

#dolu klasör silmeyi-->shutil
#shutil.rmtree("BeDeletedFolder")

#2)DOSYA VE KLASÖR KOPYALAMA
#shutil.copy()
#shutil.copy2()
#Source--> Destination
#shutil.copy("SourceFolder/k1.txt","TargetFolder/b1.txt")

#Klasör Kopyalama
#Shutil.copytree()
#shutil.copytree("SourceFolder","Copy of SourceFolder")

#3)DOSYA VE KLASÖR TASIMA
#shutil.move(kaynak,hedef)
#shutil.move("SourceFolder/k2.txt","TargetFolder")

#4)Klasörü Yeniden Adlandirma
os.rename("Copy of SourceFolder","FinalFolder")


























