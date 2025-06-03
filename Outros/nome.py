import tkinter as tk

janela = tk.Tk ()
janela.title ("Mini App com Tkinter")
janela.geometry ("300x200")

frame_superior = tk.Frame (janela)
frame_superior.pack (pady=10)

rotulo_instrucao = tk.Label (frame_superior, text="Digite seu nome:")
rotulo_instrucao.pack ()

entrada_nome = tk.Entry (frame_superior, width=25)
entrada_nome.pack ()

rotulo_mensagem = tk.Label (janela, text="", font=("Arial", 12))
rotulo_mensagem.pack (pady=10)

def atualizarMensagem ():
    nome = entrada_nome.get ()
    if nome:
        rotulo_mensagem.config (text=f"Olá, {nome}!")
    else:
        rotulo_mensagem.config (text="Você não digitou nada!")

def limparMensagem ():
    entrada_nome.delete (0, tk.END)
    rotulo_mensagem.config (text="")

frame_botoes = tk.Frame (janela)
frame_botoes.pack (pady=5)

botao_exibir = tk.Button (frame_botoes, text="Exibir mensagem", command=atualizarMensagem)
botao_exibir.pack (side=tk.LEFT, padx=5)

janela.mainloop ()