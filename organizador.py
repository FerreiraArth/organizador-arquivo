import os #trabalha com arquivos e pastas
import shutil #move arquivos

caminho = "C:/Users/arthu/Downloads/Photos-3-001"

pastas = {
    "Imagens": [".png", ".jpg", ".jpeg", ".heic"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Planilhas": [".xlsx", ".csv"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

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

                print(f"Movido: {arquivo} -> {pasta}")
                break