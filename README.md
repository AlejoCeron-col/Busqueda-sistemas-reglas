# 🚌 Sistema Inteligente de Transporte

Sistema inteligente desarrollado en **Python** que permite encontrar la mejor ruta entre dos estaciones de un sistema de transporte masivo.

El sistema utiliza una **base de conocimiento**, reglas lógicas y un **motor de inferencia** para analizar las diferentes rutas disponibles y seleccionar aquella que tenga el **menor tiempo de recorrido**.

## 📌 Descripción

El sistema representa las rutas mediante conexiones entre estaciones. Cada conexión contiene:

* Estación de origen.
* Estación de destino.
* Tiempo estimado en minutos.
* Línea de transporte.

Por ejemplo:

```python
("1", "2", 8, "L1")
```

Esto significa que existe una conexión desde la estación **1** hasta la estación **2**, con un tiempo de **8 minutos**, perteneciente a la línea **L1**.

El sistema busca todas las rutas posibles entre el origen y el destino, evita ciclos y finalmente selecciona la ruta con menor tiempo.

## 🧠 Funcionamiento

El programa está dividido en varias partes:

### 1. Base de conocimiento

Contiene las rutas y conexiones disponibles:

```python
rutas = [
    ("1", "2", 8, "L1"),
    ("2", "3", 6, "L1"),
    ("3", "4", 10, "L1")
]
```

### 2. Diccionario de estaciones

Permite mostrar el nombre de cada estación en lugar de su número:

```python
estaciones = {
    "1": "Terminal",
    "2": "Centro",
    "3": "Parque",
    "4": "Universidad"
}
```

### 3. Reglas lógicas

Las funciones `existe_conexion()` y `obtener_conexiones()` permiten consultar las conexiones disponibles en la base de conocimiento.

### 4. Motor de inferencia

La función `buscar_rutas()` analiza las conexiones y encuentra las diferentes rutas posibles entre dos estaciones.

También evita visitar nuevamente una estación para prevenir ciclos.

### 5. Selección de la mejor ruta

La función `mejor_ruta()` compara las rutas encontradas y selecciona aquella que tenga el menor tiempo total.

### 6. Resultado

Finalmente, `mostrar_ruta()` presenta la información de manera sencilla:

```text
Origen: Terminal
Destino: Universidad

Mejor ruta encontrada:
Terminal -> Centro -> Parque -> Universidad

Tiempo estimado: 24 minutos
```

---

## ⚙️ Requisitos

Para ejecutar el proyecto necesitas:

* **Python 3.8 o superior**
* Git (opcional, si vas a clonar el repositorio)
* Una terminal o consola

El programa utiliza únicamente librerías estándar de Python, por lo que **no es necesario instalar paquetes externos**.

---

## 📥 Instalación

### 1. Clonar el repositorio

Si el proyecto está alojado en GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Por ejemplo:

```bash
git clone https://github.com/AlejoCeron-col/Busqueda-sistemas-reglas.git
```

---

## ▶️ Ejecución

Ejecuta el archivo Python desde la terminal o Visual Studio Code:

```bash
python nombre_del_archivo.py
```

Por ejemplo, si el archivo se llama `rutas.py`:

```bash
python rutas.py
```

El programa mostrará las estaciones disponibles:

```text
==========================================
 SISTEMA INTELIGENTE DE TRANSPORTE
==========================================

Estaciones disponibles:

1. Terminal
2. Centro
3. Parque
4. Universidad
5. Estadio
6. Hospital
7. Aeropuerto
8. Estación 8
9. Estación 9
10. Estación 10
```

Después solicitará el origen y el destino:

```text
Ingrese el número de la estación de origen: 1
Ingrese el número de la estación de destino: 4
```

El sistema calculará automáticamente la mejor ruta.

### Resultado esperado

```text
==========================================
 RESULTADO DE LA BÚSQUEDA DE RUTA
==========================================

Origen: Terminal
Destino: Universidad

Mejor ruta encontrada:

Terminal -> Centro -> Parque -> Universidad

Tiempo estimado: 24 minutos
```

---

## 📂 Estructura del proyecto

```text
Busqueda-sistemas-reglas/
│
├── rutas.py
└── README.md
```

* `rutas.py`: contiene el sistema inteligente y el motor de inferencia.
* `README.md`: documentación del proyecto.

---

## 🎯 Objetivo

Desarrollar un sistema inteligente basado en **reglas lógicas** capaz de analizar una base de conocimiento sobre rutas de transporte y determinar automáticamente el recorrido con menor tiempo entre una estación de origen y una estación de destino.

## 👨‍💻 Tecnologías

* 🐍 Python
* 🧠 Sistemas basados en conocimiento
* 📚 Reglas lógicas
* ⚙️ Motor de inferencia
* 💻 Consola/Terminal

