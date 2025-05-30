from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
""" 
A4: tamanho da página.
SimpleDocTemplate: estrutura básica para montar o PDF.
Table, TableStyle: criam e estilizam a tabela.
colors: define cores.
"""

#  Cria o arquivo PDF chamado "tabela.pdf" com página do tamanho A4.
doc = SimpleDocTemplate("tabela.pdf", pagesize=A4)

#dados tabela
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 22, "São Paulo"],
    ["Nigga", 69, "Banana city"],
    ["João", 23, "Curitiba"]
]

#criacao da tabela
tabela = Table(dados)


#estilo da tabela
# (0, 0) até (-1, 0) = da primeira coluna à última,
# apenas na primeira linha. -1 significa "último elemento".
estilo = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),  # Fundo azul na 1ª linha
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Texto branco na 1ª linha
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),              # Alinhamento central
    ("GRID", (0, 0), (-1, -1), 1, colors.black)         # Linhas da grade pretas
])

tabela.setStyle(estilo)

# Adiciona ao PDF
doc.build([tabela])