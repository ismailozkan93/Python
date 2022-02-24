"""
try:
    ---kod----
except
    ---hata---
else
    ---hatasiz isleme---
finally
    ---ne olursa olsun---
"""
def bolme(x,y):
    try:
        result=x/y
    except ZeroDivisionError as e:
        print(e)
    else:
        print("sonuc",result)
    finally:
        print("islem tamamlandi")

#bolme(12,2)
#bolme(15,0)

def dosya_ac(path):
    try:
        file=open(path)
    except Exception as ext:
        print(ext)
    else:
        print(file.read())
    finally:
        try:
            file.close()##Herhangi bir dosya bulamadigi icin,kapatamaz ve  hata verir
        except:
            pass
dosya_ac("dizilerrr.txt")

