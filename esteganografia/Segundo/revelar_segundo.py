import numpy as np
from scipy.io import wavfile

# Função que extrai a mensagem escondida.
def revelar_mensagem(audio_codificado):

    # Lê o áudio e usa só o primeiro canal se for estéreo.
    taxa, dados = wavfile.read(audio_codificado)
    if dados.ndim > 1:
        dados = dados[:, 0]

    # Lê o último bit (LSB) de cada amostra (é onde os dados da mensagem foram colocados).
    # Exemplo:
    # Valor: 10101011 → & 1 → 1
    bits = [str(dado & 1) for dado in dados]

    # Junta todos os bits coletados num grande texto binário.
    mensagem_bin = ''.join(bits)

    # Procura o fim da mensagem usando o delimitador.
    # Corta o resto.
    fim = mensagem_bin.find('1111111111111110')    
    mensagem_bin = mensagem_bin[:fim]

    # Agrupa os bits de 8 em 8 
    # e converte cada grupo de volta para um caractere:
    # 01000001 → 65 → chr(65) → "A"
    mensagem = ''.join([chr(int(mensagem_bin[i:i+8], 2)) for i in range(0, len(mensagem_bin), 8)])
    print("Mensagem revelada: ", mensagem)

revelar_mensagem("Segundo\musica_ComMsg.wav")    