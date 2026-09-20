"""
Interface gráfica do BlueSentinel.

Responsável por:
- Exibir eventos detectados pelo scanner
- Permitir execução manual de scan
- Monitoramento contínuo do sistema
- Exibir contadores de alertas

A interface não realiza detecção diretamente.
Ela apenas chama o scanner principal.
"""

import tkinter as tk
import threading
import time
from utils.logger import registrar_evento
from datetime import datetime

from scanner import scan_completo


# =========================
# Variáveis globais
# =========================

monitorando = False

alertas_criticos = 0
eventos_suspeitos = 0
conexoes_detectadas = 0

janela = None
lista_resultados = None
contador_label = None
status_label = None


# =========================
# Atualiza contador
# =========================

def atualizar_contador():
    """
    Atualiza os contadores exibidos na interface.
    """

    contador_label.config(
        text=f"ALERTAS CRÍTICOS: {alertas_criticos} | EVENTOS SUSPEITOS: {eventos_suspeitos} | CONEXÕES: {conexoes_detectadas}"
    )


# =========================
# Inserir evento na interface
# =========================

def inserir_evento(texto):
    """
    Insere evento detectado na interface
    e aplica classificação visual baseada no tipo de alerta.
    """

    global alertas_criticos
    global eventos_suspeitos
    global conexoes_detectadas

    timestamp = datetime.now().strftime("%H:%M:%S")

    linha = f"{timestamp} {texto}"

    registrar_evento(texto)

    lista_resultados.insert(tk.END, linha)

    index = lista_resultados.size() - 1

    # =========================
    # Classificação visual
    # =========================

    if "[ALERTA C2]" in texto:

        lista_resultados.itemconfig(index, fg="red")
        alertas_criticos += 1

    elif "[PROCESSO SUSPEITO]" in texto:

        lista_resultados.itemconfig(index, fg="yellow")
        eventos_suspeitos += 1

    elif "[PERSISTENCIA]" in texto:

        lista_resultados.itemconfig(index, fg="cyan")
        eventos_suspeitos += 1

    elif "[BEACONING SUSPEITO]" in texto:

        lista_resultados.itemconfig(index, fg="orange")
        eventos_suspeitos += 1

    elif "[CONEXAO]" in texto:

        lista_resultados.itemconfig(index, fg="white")
        conexoes_detectadas += 1

    elif "[LOLBIN DETECTADO]" in texto:

        lista_resultados.itemconfig(index, fg="magenta")
        alertas_criticos += 1

    atualizar_contador()

    lista_resultados.yview(tk.END)


# =========================
# Scan manual
# =========================

def iniciar_scan():
    """
    Executa um scan único do sistema.
    """

    resultados = scan_completo()

    for r in resultados:
        inserir_evento(r)


# =========================
# Loop de monitoramento
# =========================

def loop_monitoramento():
    """
    Executa monitoramento contínuo do sistema.
    """

    global monitorando

    while monitorando:

        resultados = scan_completo()

        for r in resultados:
            janela.after(0, inserir_evento, r)

        time.sleep(5)


# =========================
# Iniciar monitoramento
# =========================

def iniciar_monitoramento():

    global monitorando

    if monitorando:
        return

    monitorando = True

    status_label.config(text="STATUS: monitorando sistema...")

    thread = threading.Thread(target=loop_monitoramento)

    thread.daemon = True

    thread.start()


# =========================
# Parar monitoramento
# =========================

def parar_monitoramento():

    global monitorando

    monitorando = False

    status_label.config(text="STATUS: monitoramento pausado")


# =========================
# Limpar eventos
# =========================

def limpar_eventos():

    global alertas_criticos
    global eventos_suspeitos
    global conexoes_detectadas

    lista_resultados.delete(0, tk.END)

    alertas_criticos = 0
    eventos_suspeitos = 0
    conexoes_detectadas = 0

    atualizar_contador()


# =========================
# Interface principal
# =========================

def iniciar_interface():

    global janela
    global lista_resultados
    global contador_label
    global status_label

    janela = tk.Tk()

    janela.title("BlueSentinel Security Monitor")

    janela.geometry("900x600")

    janela.configure(bg="#1e1e1e")


    titulo = tk.Label(
        janela,
        text="BlueSentinel Security Monitor",
        fg="white",
        bg="#1e1e1e",
        font=("Arial", 16),
    )

    titulo.pack(pady=10)


    contador_label = tk.Label(
        janela,
        text="ALERTAS CRÍTICOS: 0 | EVENTOS SUSPEITOS: 0 | CONEXÕES: 0",
        fg="#00ff9c",
        bg="#1e1e1e",
        font=("Arial", 10),
    )

    contador_label.pack()


    status_label = tk.Label(
        janela,
        text="STATUS: monitoramento pausado",
        fg="white",
        bg="#1e1e1e",
    )

    status_label.pack(pady=5)


    frame_botoes = tk.Frame(janela, bg="#1e1e1e")

    frame_botoes.pack(pady=10)


    btn_scan = tk.Button(
        frame_botoes,
        text="Iniciar Scan",
        command=iniciar_scan
    )

    btn_scan.grid(row=0, column=0, padx=5)


    btn_monitorar = tk.Button(
        frame_botoes,
        text="Monitorar em Tempo Real",
        command=iniciar_monitoramento
    )

    btn_monitorar.grid(row=0, column=1, padx=5)


    btn_parar = tk.Button(
        frame_botoes,
        text="Parar Monitoramento",
        command=parar_monitoramento
    )

    btn_parar.grid(row=0, column=2, padx=5)


    btn_limpar = tk.Button(
        frame_botoes,
        text="Limpar Eventos",
        command=limpar_eventos
    )

    btn_limpar.grid(row=0, column=3, padx=5)


    frame_lista = tk.Frame(janela)

    frame_lista.pack(pady=10)


    scrollbar = tk.Scrollbar(frame_lista)


    lista_resultados = tk.Listbox(
        frame_lista,
        width=110,
        height=25,
        bg="#000000",
        fg="white",
        yscrollcommand=scrollbar.set
    )


    scrollbar.config(command=lista_resultados.yview)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista_resultados.pack(side=tk.LEFT, fill=tk.BOTH)


    janela.mainloop()