from reportlab.pdfgen import canvas

# Cria o arquivo PDF
pdf = canvas.Canvas("meu_Primeiro.pdf")

# escreve um texto(x, y, texto);
# escreve algo nas coordenadas x e y, 
# (a origem [0, 0] é no canto inferior esquerdo).
pdf.drawString(100, 750, "Olá! seu lixo kkkkkkkkk")

# Alterar fonte e tamanho
pdf.setFont("Helvetica-Bold", 20)

pdf.line(50, 700, 500, 700) # linha horizontal

# imagem
pdf.drawImage("Mito.png", 100, 600, width=200, height=150)

#finaliza o PDF
pdf.save()