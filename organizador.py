import os #trabalha com arquivos e pastas
import shutil #move arquivos
import tkinter as tk #Bibiblioteca para criar interface
from tkinter import messagebox #Importa janela de alerta(PopUp)


caminho = "C:/Users/arthu/Downloads"

pastas = {
    "Imagens": [".png", ".jpg", ".jpeg", ".heic"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Planilhas": [".xlsx", ".csv"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

#Função principal
def organizar():
    try:
        arquivos_movidos = 0
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

titulo = tk.Label(janela, text="Organizador de Arquivo", font=("Terminal", 12)) #
titulo.pack(pady=20)

botao = tk.Button(janela, text="Organizar Arquivos", font=("Terminal", 12), command=organizar)
botao.pack(pady=20)

janela.mainloop()