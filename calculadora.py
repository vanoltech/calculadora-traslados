# Calculadora de tarifas de traslados - Versión 2

PRECIO_KM_HASTA_CLIENTE = 300.0
PRECIO_KM_CON_CLIENTE = 1000.0
RECARGO_NOCTURNO = 0.25
HORA_INICIO_NOCHE = 22
HORA_FIN_NOCHE = 6

km_hasta_cliente = float(input("Km hasta el cliente: ").replace(",", "."))
km_con_cliente = float(input("Km de viaje con el cliente: ").replace(",", "."))
hora_viaje = int(input("Hora de inicio del viaje (0 a 23): "))

costo_hasta_cliente = km_hasta_cliente * PRECIO_KM_HASTA_CLIENTE
costo_con_cliente = km_con_cliente * PRECIO_KM_CON_CLIENTE
total = costo_hasta_cliente + costo_con_cliente

es_nocturno = hora_viaje >= HORA_INICIO_NOCHE or hora_viaje < HORA_FIN_NOCHE

if es_nocturno:
    total = total + total * RECARGO_NOCTURNO
    print("Se aplicó el recargo nocturno.")

print(f"Total a cobrar: ${total:.2f}")