import os
import tkinter as tk
from tkinter import filedialog, messagebox

def buscar_arquivos(diretorio, extensoes):
    """
    Busca arquivos em um diretório com as extensões especificadas.
    """
    arquivos_encontrados = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensoes):
                caminho_completo = os.path.join(raiz, arquivo)
                arquivos_encontrados.append(caminho_completo)
    return arquivos_encontrados

def gerar_relatorio(arquivos, nome_relatorio="relatorio.txt"):
    """
    Gera um relatório com os arquivos encontrados.
    """
    with open(nome_relatorio, "w") as relatorio:
        for arquivo in arquivos:
            relatorio.write(f"{arquivo}\n")
    messagebox.showinfo("Relatório Gerado", f"Relatório salvo como: {nome_relatorio}")

def remover_arquivos(arquivos, lista_arquivos):
    """
    Remove os arquivos especificados.
    """
    for arquivo in arquivos:
        try:
            os.remove(arquivo)
        except Exception as e:
            messagebox.showerror("Erro ao Remover Arquivo", f"Erro ao remover {arquivo}: {e}")
    lista_arquivos.delete(0, tk.END)
    messagebox.showinfo("Remoção Concluída", "Todos os arquivos foram removidos com sucesso.")

def selecionar_diretorio(entry_diretorio):
    """
    Abre o seletor de diretório e insere o caminho no campo de entrada.
    """
    diretorio = filedialog.askdirectory()
    if diretorio:
        entry_diretorio.delete(0, tk.END)
        entry_diretorio.insert(0, diretorio)

def buscar_arquivos_gui(entry_diretorio, lista_arquivos):
    """
    Busca os arquivos e exibe os resultados na interface gráfica.
    """
    diretorio = entry_diretorio.get()
    if not os.path.exists(diretorio):
        messagebox.showerror("Erro", "O diretório especificado não existe.")
        return

    extensoes = (".exe", ".bat")
    arquivos_encontrados = buscar_arquivos(diretorio, extensoes)

    lista_arquivos.delete(0, tk.END)
    if arquivos_encontrados:
        for arquivo in arquivos_encontrados:
            lista_arquivos.insert(tk.END, arquivo)
    else:
        messagebox.showinfo("Nenhum Arquivo Encontrado", "Nenhum arquivo .exe ou .bat foi encontrado.")

def main():
    """
    Cria a interface gráfica e inicializa o programa.
    """
    root = tk.Tk()
    root.title("Antivírus Básico")
    root.geometry("600x400")

    # Diretório de busca
    frame_diretorio = tk.Frame(root)
    frame_diretorio.pack(pady=10, fill=tk.X, padx=10)

    label_diretorio = tk.Label(frame_diretorio, text="Diretório:")
    label_diretorio.pack(side=tk.LEFT, padx=5)

    entry_diretorio = tk.Entry(frame_diretorio)
    entry_diretorio.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    btn_selecionar = tk.Button(frame_diretorio, text="Selecionar", command=lambda: selecionar_diretorio(entry_diretorio))
    btn_selecionar.pack(side=tk.LEFT, padx=5)

    # Lista de arquivos encontrados
    frame_lista = tk.Frame(root)
    frame_lista.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista_arquivos = tk.Listbox(frame_lista, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
    lista_arquivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista_arquivos.yview)

    # Botões de ação
    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10, padx=10)

    btn_buscar = tk.Button(frame_botoes, text="Buscar Arquivos",
                           command=lambda: buscar_arquivos_gui(entry_diretorio, lista_arquivos))
    btn_buscar.pack(side=tk.LEFT, padx=5)

    btn_gerar_relatorio = tk.Button(frame_botoes, text="Gerar Relatório",
                                    command=lambda: gerar_relatorio(lista_arquivos.get(0, tk.END)))
    btn_gerar_relatorio.pack(side=tk.LEFT, padx=5)

    btn_remover = tk.Button(frame_botoes, text="Remover Arquivos",
                            command=lambda: remover_arquivos(lista_arquivos.get(0, tk.END), lista_arquivos))
    btn_remover.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
