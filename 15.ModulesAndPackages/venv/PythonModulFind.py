"""
import <modul_adi>
Python Modulleri 3 sekilde arar:
1)Bu kodun calistigi klasörde arar(ayni seviyede)
2)PYTHONPATH environment variable-->tanimli
3)Python'un kurulu oldugu klasörlerde arar(virtual env'lerde)
sys.path-->arama klasörlerini göster
"""
import sys
python_Search_path=sys.path
print(python_Search_path)
for e in python_Search_path:
    print(e)