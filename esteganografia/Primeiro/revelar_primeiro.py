from PIL import Image
import stepic

# Abre a imagem com a mensagem escondida
imagem_codificada = Image.open("Primeiro\mito_ComMensagem.png")

# Decodifica a mensagem
mensagem = stepic.decode(imagem_codificada)

print("Mensagem escondida era: ", mensagem)