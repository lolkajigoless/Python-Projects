from reportlab.pdfgen import canvas

textos = [
    "Este é o primeiro item da lista",
    "Python é muito bom para automatizar tarefas",
    "Estamos geranod um pdf automaticamente"
]

pdf = canvas.Canvas("relatorio.pdf")

y = 750

for linha in textos:
    pdf.drawString(100, y, linha)
    y -= 30 # Move para a próxima linha (mais abaixo)

pdf.save()