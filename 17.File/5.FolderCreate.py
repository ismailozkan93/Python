"""
Klasör Yaratma:
1-os.mkdir()
    *mkdir() --<tek klasör olusturur
    *makedirs()-->birden fazla klasör olusturur

2.path.Path.mkdir()-->hem tekli hem de coklu klasör yaratir
"""
#1nci yol
#Ana Klasör Yolu
import os
import pathlib
from pathlib import Path

ana_klasör_yolu=os.getcwd()
#os.mkdir("Sample Folder1")
#os.mkdir("Same Folder2")

#2nci Yol
"""
from pathlib import Path
pathlib.Path.mkdir()
p=Path("Path Folder_1")
p.mkdir()
"""

##Birden fazla klasör yaratma
"""
-Seviye 1
    -Seviye 2
        -Seviye 3   
"""
#exist_ok dosya varsa hata vermez
os.makedirs("Level1/Level2/Level3",exist_ok=True)

#2nci Yol
p3=Path("Path_level_1/Path_level_2/Path_level3")
p3.mkdir(parents=True,exist_ok=True)















