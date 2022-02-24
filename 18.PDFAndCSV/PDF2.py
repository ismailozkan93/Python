import os
import PyPDF2
import pdfplumber
            ###3-PDF TEN SAYFA ALMA(EXTRACT)
proje_yolu=os.getcwd()
pdf_path=os.path.join(proje_yolu,"PDFs","tutorial.pdf")

def sayfa_al(sayfa_no=1):
    #tek seferde import
    from PyPDF2 import PdfFileReader,PdfFileWriter
    new_pdf_path=os.path.join(proje_yolu,"PDFs","yeni_pdf"+str(sayfa_no)+".pdf")

    #Önce PDF'i alalim
    pdf=PdfFileReader(pdf_path)

    #PDF'TEN sayfa alalim
    sayfa=pdf.getPage(sayfa_no)

    #Simdi yeni bir PDF olusturalim
    pdf_writer=PdfFileWriter()
    pdf_writer.addPage(sayfa)

    #simdi olusturdugumuz bu sayfanin icini doldur
    with open(new_pdf_path, "wb") as sonuc:
        pdf_writer.write(sonuc)


sayfa_al()