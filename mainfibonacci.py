import tkinter as tk
import time
import matplotlib.pyplot as plt

from ord import fibonacci, fibonacci_dp

# Listas globales
N = []
t_fibonacci = []
t_fibonacci_dp = []


def ejecutar_ordenamiento():
    global N, t_fibonacci, t_fibonacci_dp

    N = []
    t_fibonacci = []
    t_fibonacci_dp = []

    inicio = int(entry_inicio.get())
    incremento = int(entry_incremento.get())
    limite = int(entry_limite.get())

    for i in range(inicio, limite + 1, incremento):
        N.append(i)

        # Fibonacci Normal
        t_ini = time.time()
        fibonacci(i)
        t_fin = time.time()
        t_fibonacci.append(t_fin - t_ini)

        # Fibonacci Programación Dinámica
        t_ini = time.time()
        fibonacci_dp(i)
        t_fin = time.time()
        t_fibonacci_dp.append(t_fin - t_ini)

    print("Lista de N:", N)
    print("Tiempos de Fibonacci:", t_fibonacci)
    print("Tiempos de Fibonacci DP:", t_fibonacci_dp)


def generar_grafica():
    plt.plot(N, t_fibonacci, label="Fibonacci")
    plt.plot(N, t_fibonacci_dp, label="Fibonacci DP")
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.legend()
    plt.show()


# --- INTERFAZ GRÁFICA (GUI SENCILLA) ---

ventana = tk.Tk()
ventana.title("Comparador de Fibonacci")
ventana.geometry("320x280")

tk.Label(ventana, text="Valor inicial (n):").pack(pady=(10, 0))
entry_inicio = tk.Entry(ventana)
entry_inicio.insert(0, "10")
entry_inicio.pack()

tk.Label(ventana, text="Incremento:").pack(pady=(5, 0))
entry_incremento = tk.Entry(ventana)
entry_incremento.insert(0, "5")
entry_incremento.pack()

tk.Label(ventana, text="Límite máximo (n):").pack(pady=(5, 0))
entry_limite = tk.Entry(ventana)
entry_limite.insert(0, "30")
entry_limite.pack()

# Botón 1: Capturar tiempos
btn_ordenar = tk.Button(
    ventana,
    text="1. Ordenar y Capturar Tiempos",
    command=ejecutar_ordenamiento,
)
btn_ordenar.pack(pady=(15, 5))

# Botón 2: Graficar los resultados guardados
btn_graficar = tk.Button(
    ventana, text="2. Graficar Resultados", command=generar_grafica
)
btn_graficar.pack(pady=5)

ventana.mainloop()