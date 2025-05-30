from PIL import Image # (para manipulação de imagens)
import stepic # (para esconder mensagens)

# Abre a imagem original
imagem = Image.open("Primeiro\mito.png")

# Mensagem que será escondida
mensagem = "Essa é uma mensagem secreta!"

# Codifica a mensagem na imagem
imagem_codificada = stepic.encode(imagem, mensagem.encode())

# Salva a nova imagem com a mensagem escondida
imagem_codificada.save("mito_ComMensagem.png")

print("Mensagem escondida com sucesso!")