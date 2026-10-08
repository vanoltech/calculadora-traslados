# Calculadora de tarifas de traslados - Versión 4

from tarifas import calcular_total

def pedir_numero(mensaje):
    """Pide un número no negativo y repite hasta que se ingrese uno válido."""
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("Eso no es un número, lol. Probá de nuevo (por ejemplo: 12 o 12,5).")
            continue
        if numero < 0:
            print("El número no puede ser negativo >.>")
            continue
        return numero


def pedir_si_no(mensaje):
    """Pide una respuesta de sí o no y devuelve True o False."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respondé con 's' o 'n'.")


km_hasta_cliente = pedir_numero("Km hasta el cliente: ")
km_con_cliente = pedir_numero("Km de viaje con el cliente: ")
es_nocturno = pedir_si_no("¿El viaje es nocturno (de 22 a 6)? (s/n): ")

total = calcular_total(km_hasta_cliente, km_con_cliente, es_nocturno)

if es_nocturno:
    print("Se aplicó el recargo nocturno.")

print(f"Total a cobrar: ${total:.2f}")