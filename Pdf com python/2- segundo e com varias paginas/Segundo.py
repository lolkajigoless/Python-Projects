from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Multipaginas.pdf")

#pagina 1
pdf.drawString(100, 750, "Esta é a pagina 1!")
pdf.showPage() # cria uma nova pagina

#pagina 2
pdf.drawString(100, 750 , "Esta é a pagina 2!")
pdf.showPage()

#pagina 3
pdf.drawString(100, 750, "Esta é a pagina 3!")
pdf.save()