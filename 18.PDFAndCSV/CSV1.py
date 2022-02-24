"""
CSV:COMMA SEPERATED VALUES
VIRGUL(NOKTALI VIRGÜL)ile ayrilmis degerler tutar
"""
#Python'da CSV okuma islemleri-->csv paketi ile yapilir

import csv

film_yolu="Csv_Files_Sample/Sample.csv"
film_yolu_1="Csv_Files_Sample/Sample1.csv"
            #csv okuma

def csv_oku():
    with open(film_yolu,"r")as file:
        #önce bir csv reader alalim
        filmler=csv.reader(file,delimiter=",")

        #csv.reader() geriye iterator döner--<üzerinden döngü
        for film in filmler:
            print(film)
csv_oku()
def csv_oku1():
    with open(film_yolu_1, "r") as file:
        # önce bir csv reader alalim
        filmler = csv.reader(file, delimiter="!")

        # csv.reader() geriye iterator döner--<üzerinden döngü
        for film in filmler:
            print(film)
#csv_oku1()

def csv_oku_dialect():
    csv.register_dialect("normal_okuma",delimiter=",",quoting=csv.QUOTE_MINIMAL)


    with open(film_yolu, "r") as file:
        # önce bir csv reader alalim
        filmler = csv.reader(file, dialect="normal_okuma")

        # csv.reader() geriye iterator döner--<üzerinden döngü
        for film in filmler:
            print(film)

csv_oku_dialect()