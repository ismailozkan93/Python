"""
Arsiv dosyasi acma
zipfile ile yapilir
"""
import shutil
import zipfile
import os
"""
#for f in os.listdir():
 #   print(f)
#arsiv dosyasini acalim
arsiv=zipfile.ZipFile("17.File/Folder/5-Object.create.rar","r")
print(arsiv)

#extract etmeden önce,icinde ne var bakalim
for d in arsiv.filelist:
    print(d.filename)

#simdi extract edelim
arsiv.extractall()

#arsivi kapattik
arsiv.close()
"""

###ARSIV DOSYASI OLUSTURMA
#shutil.make_archive()
shutil.make_archive("new_archive","zip","TargetFolder")
