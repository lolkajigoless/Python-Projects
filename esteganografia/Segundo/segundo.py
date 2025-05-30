#🎧 Esteganografia em Áudio 

import numpy as np # usado para lidar com arrays de números (amostras do som).
from scipy.io import wavfile # usado para ler e salvar arquivos .wav.

# Função principal: recebe o caminho do áudio original,
# a mensagem a ser escondida, e o nome do novo arquivo que será gerado.
def esconder_mensagem(audio_entrada, mensagem, audio_saida):
    # taxa: frequência de amostragem (ex: 44100 Hz).
    # dados: array com as amostras de som (valores numéricos que representam a forma de onda).
    taxa, dados = wavfile.read(audio_entrada)

    # Se o áudio tiver dois canais (estéreo), ele pega apenas o primeiro canal. Isso simplifica o processo.
    if dados.ndim > 1:
        dados = dados[:, 0]

    # Converte cada caractere da mensagem para binário de 8 bits.
    # Ex: "A" → 01000001.
    mensagem_binaria = ''.join(format(ord(c), '08b') for c in mensagem)

    # Adiciona um marcador de fim. Isso indica onde a mensagem termina durante a leitura depois.
    mensagem_binaria += '1111111111111110'    

    # Cria uma cópia do áudio original para não modificar o original diretamente.
    dados_modificados = np.copy(dados)

    # Para cada bit da mensagem:
    # & ~1: zera o último bit da amostra (LSB).
    # | int(bit): insere o bit da mensagem (0 ou 1).
    # Exemplo:
    #  Valor da amostra: 10101011
    # ~1 = 11111110, então & ~1 zera o último bit → 10101010
    #| 1 → 10101011  
    for i, bit in enumerate(mensagem_binaria):
        dados_modificados[i] = (dados_modificados[i] & ~1) | int(bit)

    # Salva o novo arquivo .wav, agora com a mensagem escondida nos bits do som.
    wavfile.write(audio_saida, taxa, dados_modificados.astype(np.int16))
    print("Mensagem escondida com sucesso!")


esconder_mensagem("Segundo\musica.wav", "Mensagem super secreta!", "Segundo\musica_ComMsg.wav")        


# ✅ Resumo do funcionamento:
# 
# 1. Cada amostra de som (sample) é representada por um número inteiro.
#    A esteganografia funciona modificando apenas o último bit (LSB) de cada amostra,
#    o que quase não afeta a qualidade do áudio.
#
# 2. A mensagem de texto é convertida para uma sequência de bits binários (0s e 1s),
#    e esses bits são "injetados" um por um nos LSBs das amostras de som.
#
# 3. Para recuperar a mensagem, basta ler o último bit de cada amostra na mesma ordem.
#    Quando se encontra um delimitador especial (ex: 1111111111111110), a leitura para,
#    e os bits extraídos são convertidos de volta para caracteres.
