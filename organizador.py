import os                   #trabalha com arquivos e pastas
import shutil               #move arquivos
import tkinter as tk        #Bibiblioteca para criar interface
from tkinter import filedialog, messagebox
#Possibilita abrir explorador de pastas
#Importa janela de alerta(PopUp)

pastas = {
    "Imagens": [".png", ".jpg", ".jpeg", ".heic"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Planilhas": [".xlsx", ".csv"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

caminho = ""

def selecionar_pasta():
    global caminho
    caminho = filedialog.askdirectory()
    if caminho:
        label_caminho.config(text=f"Pasta: {caminho}")

#Função principal
def organizar():
    if not caminho:
        messagebox.showwarning("Aviso", "Selecione uma pasta primeiro!")
        return
    
    log_text.delete(1.0, tk.END)
    arquivos_movidos = 0


    try:
        for arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, arquivo)

            #ignora pastas
            if os.path.isfile(caminho_arquivo):
                _, extensao = os.path.splitext(arquivo)

                for pasta, extensoes in pastas.items():

                    if extensao.lower() in extensoes: 
                        caminho_pasta = os.path.join(caminho, pasta)

                        #Cria pasta se não existir
                        if not os.path.exists(caminho_pasta):
                            os.mkdir(caminho_pasta)
                        
                        shutil.move(caminho_arquivo, os.path.join(caminho_pasta, arquivo))
                        arquivos_movidos += 1

        messagebox.showinfo("Sucesso", f"{arquivos_movidos} arquivos organizados!")

    except Exception as e:
        messagebox.showerror("Erro", str(e)) #mostra erro na tela

#INTERFACE
janela = tk.Tk()
janela.title("Organizador de Arquivo")
janela.geometry("300x200")

titulo = tk.Label(janela, text="Organizador de Arquivo", font=("Terminal", 12)) 
titulo.pack(pady=20)

botao_pasta = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_pasta.pack(pady=5)

label_caminho = tk.Label(janela, text="Nenhuma pasta selecionada", fg = "gray")
label_caminho.pack(pady=10)

botao = tk.Button(janela, text="Organizar Arquivos", font=("Terminal", 12), command=organizar)
botao.pack(pady=20)

#Area de log
log_text = tk.Text(janela, height=10, width=50)
log_text.pack(pady=10)

janela.mainloop()