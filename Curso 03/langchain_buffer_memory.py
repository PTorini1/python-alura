import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.globals import set_debug
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain.memory import ConversationBufferMemory

load_dotenv()
set_debug(True)

class Destino(BaseModel):
    cidade = Field("cidade a visitar")
    motivo = Field("motivo pelo qual é interessante visitar")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
)

mensagens = [
    "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
    "Qual é o melhor período do ano para visitar em termos de clima?",
    "Quais tipos de atividades ao ar livre estão disponíveis?",
    "Alguma sugestão de acomodação eco-friendly por lá?",
    "Cite outras 20 cidades com características semelhantes às que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
    "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm,
                                verbose=True,
                                memory=memory)

longa_conversa = ""
for mensagem in mensagens:
    resposta = conversation.predict(input = mensagem)
    print(resposta)
    
print(memory.load_memory_variables({}))