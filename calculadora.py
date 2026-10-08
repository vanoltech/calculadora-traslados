# Calculadora de tarifas de traslados - Versión 3

PRECIO_KM_HASTA_CLIENTE = 300.0
PRECIO_KM_CON_CLIENTE = 1000.0
RECARGO_NOCTURNO = 0.25


def calcular_total(km_hasta_cliente, km_con_cliente, es_nocturno):
    """Devuelve el total a cobrar por un traslado."""
    costo_hasta_cliente = km_hasta_cliente * PRECIO_KM_HASTA_CLIENTE
    costo_con_cliente = km_con_cliente * PRECIO_KM_CON_CLIENTE
    total = costo_hasta_cliente + costo_con_cliente

    if es_nocturno:
        total = total + total * RECARGO_NOCTURNO

    return total


km_hasta_cliente = float(input("Km hasta el cliente: ").replace(",", "."))
km_con_cliente = float(input("Km de viaje con el cliente: ").replace(",", "."))
respuesta = input("¿El viaje es nocturno (de 22 a 6)? (s/n): ").strip().lower()

es_nocturno = respuesta in ("s", "si", "sí")

total = calcular_total(km_hasta_cliente, km_con_cliente, es_nocturno)

if es_nocturno:
    print("Se aplicó el recargo nocturno.")

print(f"Total a cobrar: ${total:.2f}")