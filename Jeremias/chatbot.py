from openai import AzureOpenAI

conversa_completa = "Histórico da Conversa até agora: \n"

# Configurações Azure
### Bloco com chave de API e informações do AZURE removida por segurança

# Cria o cliente AzureOpenAI
client = AzureOpenAI(
    api_version=api_version, # type: ignore
    azure_endpoint=endpoint, # type: ignore
    api_key=subscription_key, # type: ignore
)

# Função que responde perguntas
def responder(pergunta: str) -> str:
    global conversa_completa
    try:
        conversa_completa += f"eu: {pergunta}\n"
        response = client.chat.completions.create(
            model=deployment, # type: ignore
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": conversa_completa},
            ],
            max_tokens=800,
            temperature=1.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        resposta = response.choices[0].message.content.strip()
        conversa_completa += f"voce: {resposta}\n"
        return resposta
    except Exception as e:
        print(f"[ERRO AZURE] {e}")
        return "Erro ao processar a pergunta com a IA."



