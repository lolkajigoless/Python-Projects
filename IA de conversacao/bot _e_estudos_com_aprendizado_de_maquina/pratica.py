from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Base de conhecimento (perguntas e respostas)
perguntas_respostas = {
    "olá, tudo bem?": "Olá! Estou bem, e você?",
    "quem é você?": "Sou um assistente virtual criado para conversar com você.",
    "como funciona a inteligência artificial?": "A inteligência artificial simula capacidades humanas, como aprendizado e raciocínio.",
    "obrigado": "De nada! Estou aqui para ajudar.",
    "adeus": "Até logo! Foi bom conversar com você."
}

