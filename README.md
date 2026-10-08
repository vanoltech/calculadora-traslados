# Calculadora de tarifas de traslados

Programa en Python que calcula cuánto cobrar por un traslado en camioneta, según los kilómetros recorridos y el horario del viaje.

Es un proyecto de práctica con el que estoy aprendiendo Python y Git, y que además resuelve una necesidad real de mi emprendimiento.

## Cómo funciona

El programa pide tres datos:

- Kilómetros desde mi ubicación hasta el cliente
- Kilómetros del viaje con el cliente
- Hora de inicio del viaje (de 0 a 23)

Y aplica estas reglas:

- Cada tramo tiene su propia tarifa por kilómetro.
- Si el viaje es nocturno (de 22:00 a 6:00), responder "s" para sumar un recargo del 25%

## Cómo usarlo

Requiere Python 3. Desde la terminal, en la carpeta del proyecto:

```bash
python3 calculadora.py
```

## Estado del proyecto

## Estado del proyecto

- [x] V1: cálculo por kilómetros
- [x] V2: tarifas separadas por tramo y recargo nocturno
- [x] V3: cálculo ordenado en una función
- [x] V4: validación de datos ingresados
- [ ] V5: interfaz gráfica de escritorio
- [ ] Guardar historial de viajes