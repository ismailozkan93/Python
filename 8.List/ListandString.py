gun="Pazartesi"
print(gun)
print(type(gun))

harfler_gun=list(gun)
print(harfler_gun)
print(type(harfler_gun))

metin="Today is very hot"
kelimeler=metin.split() #Kelimler split() ile
print(kelimeler)        #Harfler list ile

mailbox="spam-spam-spam-spam"
karakter="-"
mailler=mailbox.split(karakter)
print(mailler)

##join() split() in tam tersidir
kelimeler=["günes","acar","yüzler","güler"]

#join()
cumle=" ".join(kelimeler)
print(cumle)
cumle="-".join(kelimeler)
print(cumle)