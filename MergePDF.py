from PyPDF2 import PdfMerger

AllPdf = ["pdf1.pdf", "pdf2.pdf"]

NewMerger = PdfMerger()

for NewPDF in AllPdf:
    NewMerger.append(NewPDF)

NewMerger.write("Merge By Python.pdf")
NewMerger.close()
