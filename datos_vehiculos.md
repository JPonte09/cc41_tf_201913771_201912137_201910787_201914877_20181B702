# Generar descripción de datos de vehículos de entrega indicando según su criterio, cálculo de costos

## Conceptos

- **Cargo Fijo:** Monto fijo a pagar por el servicio que se suma a otros factores, se mide en soles.

- **Tarifa mínima:** Monto mínimo a pagar por el servicio en soles.

- **Precio por distancia:** Es el precio por un kilómetro transcurrido expresado en soles. Este valor es fijo.

- **Distancia:** Es la longitud entre un punto de partida y un punto de llegada. La unidad de medición con el cual será expresado es en kilómetros.

- **Precio por tiempo:** El precio por tiempo será establecido para cubrir los gastos generados al transitar un vehículo con carga. Para ello, el precio se establecerá en función de las horas transcurridas.

- **Tiempo:** Periodo de tiempo que se demora un vehículo al entregar una carga entre 2 intervalos geográficos. Esto se medirá en función de las horas transcurridas.

## Ejemplo

**Tarifa mínima:** 15 Soles

**Cargo Fijo:** 5 Soles

**Precio por distancia:** 1.3 Soles

**Precio por tiempo:** 1 Sol

Se asume que el **automóvil** no se detiene y maneja a una velocidad constante de 30 km/h.

Se asume que cada **punto recorrido** es equivalente a 1 km.

### Entonces: 

```
Tiempo = distancia / velocidad = distancia / 30

Posible Fórmula

PrecioFinal = CargoFijo + PrecioDistancia * Distancia + PrecioTiempo * Tiempo

Si (PrecioFinal < TarifaMin) entonces

TarifaMin = 15

FinSi 
```
