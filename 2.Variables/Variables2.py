#1Derleyici(COMPILER): kaynak kodu makine diline ceviren yazilimdir
#2Compiler kod yazilimi tamamlaninca tek seferde tüm kodu makine diline cevirir
#1Yorumlayici(Interpreter):Kaynak kodu makine diline ceviren yazilimdir
#2Interpreter, kod yazilirken cevirir. Satir satir makine cevirir
#Yorum satiri Python Interpreter tarafindan calistirilmaz
"""
COKLU YORUM SATIRI
\n bir alt satira gecer
"""
cok_satir_metin="Satir 1 \nSatir2 \nSatir3"
print(cok_satir_metin)

p = 8
p = p * 3
p /= 2
print(p)

#Stringler hem tek tirnak hem cift tirnak olarak gösterilebilirler
text='Alice says:"Run bunny,run ..."'
print(text)

##Stringler aritmetik islem yapamazlar
#'4'-'3 hata verir
birinci="sunny"
ikinci ="days"
#Concatination
print(birinci+ikinci)
print(5*birinci)

print(6*'5')
