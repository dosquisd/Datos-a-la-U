# GeoData

## Miembros

- [Diederik A. Burbano](https://github.com/Parcesito)
- [Juan D. Perez](https://github.com/dosquisd)
- [Mauro A. Gonzales](https://github.com/MauroGonzalez51)

## Descripción

GeoData es un software de análisis y visualización que permite transformar los datos en mapas intuitivos, que comprenden al espacio no solo como escenario sino como un factor fundamental e influyente en los hechos.

## Datos

### Principal

El dataset principal con el que se está trabajando es llamado "Procesos en casas de justicia" es proveído por el Ministerio de Justicia y Derecho por medio del repositorio de datos abiertos, contiene todos los procesos por cada una de las casas de justicia del país durante los últimos 4 años. Tiene más de 3.700.000 incisos y es de actualización trimestral.

### Georeferencia

También proveído por el Ministerio de Justicia y Derecho, es un directorio de todas las casas de justica del país y su dirección. Es de actualización anual.

### Apoyo

Proveniente del DANE, es el conjunto de datos que contiene todos los indicadores de vulnerabilidad económica de cada región del país durante más de 4 años. Está completamente georeferenciado, lo que facilita su compaginación con el resto de la información.

Para más información acerca los datos utilizados, ir a [aquí](./backend/data/README.md).

## Mapa inteligente

GeoData busca diferenciarse al ser un mapa inteligente, que ayuda a observar el mundo que fue, es y será con la ayuda de la inteligencia artificial.

Para ello, se está haciendo uso de las modelos regresivos para calcular valores de cada nodo del mapa en función de sus últimos patrones y los indicadores de vulnerabilidad en la zona, en concreto, para los modelos de regresión se está haciendo uso de redes neuronales LSTM (Long Short-Term Memory). Además, aumentamos la confiabilidad de las predicciones al constrastar los resultados utilizando múltiples modelos predictivos entrenados con fuentes confiables.

## Impacto

GeoData amplía la capacidad de análisis y visualización de datos, proporcionando herramientas que permiten comprender de manera más integral las dinámicas de las regiones vulnerables. Gracias a su enfoque basado en inteligencia artificial y georreferenciación, facilita la identificación de patrones y la toma de decisiones fundamentadas. Esto permite no solo mejorar la asignación de recursos y la planificación estratégica, sino también fortalecer el acceso a la justicia y servicios en zonas con mayores índices de pobreza y vulnerabilidad.

### Caso de estudio

- Entender mejor las necesidades de las zonas vulnerables.
- Anticipar la asignación de recursos económicos, humanos y de seguridad.
- Mejorar el acceso a la justicia en áreas con alto índice de pobreza y vulnerabilidad.

### Con GeoData

- Reducir el tiempo necesario para la construcción de mapas de datos.
- Dar visibilidad a las historias intrínsecas en los datos que se desvanecen en los métodos de visualización más usuales.
- Facilitar la visualización de datos y la correlación de información para analistas y usuarios.

## Estructura

Para el desarrollo de todo el software, está dividido en 4 secciones claves:

- Desarrollo Frontend. [Aquí](./nuxtapp/)
- Preparación de los datos. [Aquí](./backend/data/)
- Desarrollo de la API en el backend. [Aquí](./backend/api/)
- Desarrollo de los modelos de IA. [Aquí](./backend/models/)
