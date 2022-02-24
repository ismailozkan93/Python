import csv


            #csv okuma
#reader() calisabilir mi?hangi ayirac
def csv_sniffer():
    with open(film_yolu,"r")as file:
        icerik=file.read()
        has_reader=csv.Sniffer().has_header(icerik)
        print(has_reader)

    dialect=csv.Sniffer().sniff(icerik)
    print("ayirac:",dialect.delimiter)


eklenecek=["Hello World","T-SHIRT-PREMIUM-QUALITY",
               "Üstün kaliteli",1,0,"visible","Gül filmini mi gitti"]
def csv_write():
    with open(film_yolu,"a", newline="") as dosya:
      writer=csv.writer(dosya,delimiter=",",quoting=csv.QUOTE_ALL)
      writer.writerow(eklenecek)

#csv_write()
#csv_sniffer()
film_yolu="Csv_Files_Sample/Sample.csv"
film_yolu_1="Csv_Files_Sample/Sample1.csv"
def csv_kopyala():
    yeni_film_yolu="Csv_Files_Sample/CopySample.csv"
    #yeni dosya olusturalim
    open(yeni_film_yolu,"x")

    #ayni anda iki dosya acma
    with open(film_yolu,"r") as movies, open(yeni_film_yolu,"a",newline="")as movies_c:
        filmler=csv.reader(movies)
        writer=csv.writer(movies_c, quoting=csv.QUOTE_ALL)

        for film in filmler:
            writer.writerow(film)