import random

def chatbot_interativo(entrada):
    if "oi" in entrada.lower():
        return "Oi! Qual é seu nome?"
    elif "meu nome é" in entrada.lower():
        nome = entrada.lower().replace("meu nome é", "").strip() # Extrai o nome do texto
        return f"Prazer em conhecer voce, {nome.capitalize()}!, qual a sua idade?"
    elif "tenho" in entrada.lower():
        idade = entrada.lower().replace("tenho", "").strip()
        return f"{idade} que legal!"
    elif "bye" in entrada.lower():
        return "Tchau amigo"
    else:
        return "nao entendi mano, dá pra repetir nao?"


while True:
    mensagem = input("Voce: ")
    resposta = chatbot_interativo(mensagem)    
    print(f"Chatbot: {resposta}")
    if "bye" in mensagem.lower():
        break
