def email_ayir():
    email=input("Email giriniz")
    kullanici_adi=""
    domain=""
    if (email.find("@")==-1):
        print("Lütfen @ giriniz")

    kullanici_adi=email[0:(email.find("@"))]
    domain=email[(email.find("@"))+1:(len(email))+1]
    print(kullanici_adi)
    print(domain)

#email_ayir()

def ters_cevir():
    cumle=input("Lütfen bir cümle giriniz")
    print(cumle[::-1])

#ters_cevir()
def siradaki_harfle_degistir():
    metin=input("Bir cümle giriniz")
    alfabe_kucuk = 'abcçdefgğhıijklmnoöprsştuüvyz'
    alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    yenimetin=""

    def harf_kucuk_mu():
        return harf in alfabe_kucuk
    def harf_buyuk_mu():
        return harf in alfabe_buyuk
    def siradaki_harf(alfabe,harf):
        index=alfabe.find(harf)
        return alfabe[index+1]
    for harf in metin:
        if harf_kucuk_mu():
            yeni_harf=siradaki_harf(alfabe_kucuk,harf)
        elif harf_buyuk_mu():
            yeni_harf=siradaki_harf(alfabe_buyuk,harf)
        else:
            yeni_harf=harf

        yenimetin=yenimetin+yeni_harf

    print(yenimetin)
    return yenimetin

siradaki_harfle_degistir()
