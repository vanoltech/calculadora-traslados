# Calculadora de tarifas de traslados - Versión 2

PRECIO_KM_HASTA_CLIENTE = 300.0
PRECIO_KM_CON_CLIENTE = 1000.0
RECARGO_NOCTURNO = 0.25

km_hasta_cliente = float(input("Km hasta el cliente: ").replace(",", "."))
km_con_cliente = float(input("Km de viaje con el cliente: ").replace(",", "."))
respuesta = input("¿El viaje es nocturno (de 22 a 6)? (s/n): ").strip().lower()

costo_hasta_cliente = km_hasta_cliente * PRECIO_KM_HASTA_CLIENTE
costo_con_cliente = km_con_cliente * PRECIO_KM_CON_CLIENTE
total = costo_hasta_cliente + costo_con_cliente

es_nocturno = respuesta in ("s", "si", "sí")

if es_nocturno:
    total = total + total * RECARGO_NOCTURNO
    print("Se aplicó el recargo nocturno.")

print(f"Total a cobrar: ${total:.2f}")