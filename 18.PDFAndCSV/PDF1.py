#
import os
import PyPDF2
import pdfplumber

proje_yolu=os.getcwd()
pdf_path=os.path.join(proje_yolu,"PDFs","Zusammenfassung+-+Klassen+und+Objekte.pdf")

def pdf_ozellikleri_okuma():
    #pdf'i oku
    pdf=PyPDF2.PdfFileReader(pdf_path)
    print(pdf)

    #SAYFA SAYISI
    sayfa_sayisi=pdf.getNumPages()
    print(f"sayfa sayisi: {sayfa_sayisi}")

    #simdi dokuman bilgileri
    dokuman_bilgileri=pdf.documentInfo
    print("Dokuman bilgileri: {0}".format(dokuman_bilgileri))#Dictionary

    for key,value in dict(dokuman_bilgileri).items():
        print(f"{key}:{value}")

#######1-PDF'TEN TEXT(SAYFA) OKUMA ###########
def pdf_sayfa_oku(sayfa_no=1):
    #pdfplumber normal open metodu gibi calisir
    with pdfplumber.open(pdf_path) as pdf:
        sayfa=pdf.pages[sayfa_no]
        icerik=sayfa.extract_text()
        print(icerik)

pdf_sayfa_oku()

def pdf_coklu_sayfa_oku(ilk_sayfa_no=0,son_sayfa_no=2):
    #pdfplumber normal open metodu gibi calisir
    with pdfplumber.open(pdf_path) as pdf:
        for i in range(ilk_sayfa_no,son_sayfa_no+1):
            print(f"-------{i}.sayfa basi---------")
            sayfa=pdf.pages[i]
            icerik=sayfa.extract_text()
            print(icerik)
            print(f"------{i}.sayfa sonu-------")

pdf_coklu_sayfa_oku()


pdf_ozellikleri_okuma()