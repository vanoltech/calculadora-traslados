# Calculadora de tarifas de traslados - Versión 5 (ventana)

import tkinter as tk

from tarifas import calcular_total


def calcular():
    """Lee los datos de la ventana y muestra el total."""
    try:
        km_hasta = float(entrada_km_hasta.get().strip().replace(",", "."))
        km_con = float(entrada_km_con.get().strip().replace(",", "."))
    except ValueError:
        resultado.set("Revisá los kilómetros: tienen que ser números.")
        return

    if km_hasta < 0 or km_con < 0:
        resultado.set("Los kilómetros no pueden ser negativos.")
        return

    total = calcular_total(km_hasta, km_con, es_nocturno.get())
    resultado.set(f"Total a cobrar: ${total:.2f}")


ventana = tk.Tk()
ventana.title("Calculadora de traslados")

es_nocturno = tk.BooleanVar()
resultado = tk.StringVar()

tk.Label(ventana, text="Km hasta el cliente:").grid(
    row=0, column=0, padx=10, pady=5, sticky="e"
)
entrada_km_hasta = tk.Entry(ventana)
entrada_km_hasta.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Km de viaje con el cliente:").grid(
    row=1, column=0, padx=10, pady=5, sticky="e"
)
entrada_km_con = tk.Entry(ventana)
entrada_km_con.grid(row=1, column=1, padx=10, pady=5)

tk.Checkbutton(
    ventana, text="Viaje nocturno (de 22 a 6)", variable=es_nocturno
).grid(row=2, column=0, columnspan=2, pady=5)

tk.Button(ventana, text="Calcular", command=calcular).grid(
    row=3, column=0, columnspan=2, pady=5
)

tk.Label(ventana, textvariable=resultado).grid(
    row=4, column=0, columnspan=2, padx=10, pady=10
)

ventana.mainloop()