import psutil
import GPUtil
import customtkinter as ctk

# Configuração da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


janela = ctk.CTk()
janela.title("Monitor do Sistema")
janela.geometry("400x300")

# Função para atualizar os dados
def atualizar():
    cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory().percent

    # GPU
    gpus = GPUtil.getGPUs()
    gpu_info = f"{gpus[0].load*100:.1f}%" if gpus else "N/A"

    # Atualiza os textos
    label_cpu.configure(text=f"Uso da CPU: {cpu}%")
    label_mem.configure(text=f"Uso da Memória: {memoria}%")
    label_gpu.configure(text=f"Uso da GPU: {gpu_info}")

    # Chama novamente após 2 segundos
    janela.after(1000, atualizar)

# Rótulos
label_cpu = ctk.CTkLabel(janela, text="Uso da CPU: ")
label_cpu.pack(pady=10)

label_mem = ctk.CTkLabel(janela, text="Uso da Memória: ")
label_mem.pack(pady=10)

label_gpu = ctk.CTkLabel(janela, text="Uso da GPU: ")
label_gpu.pack(pady=10)

# Iniciar atualização
atualizar()
janela.mainloop()
