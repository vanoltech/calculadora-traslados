# Reglas de cobro de la calculadora de traslados

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