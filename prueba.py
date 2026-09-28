# ============================================================
# SISTEMA INTELIGENTE PARA ENCONTRAR LA MEJOR RUTA
# Sistema de transporte masivo basado en reglas lógicas
# ============================================================

# ------------------------------------------------------------
# 1. BASE DE CONOCIMIENTO: 
# ------------------------------------------------------------

# Cada elemento representa una conexión entre dos estaciones.
# Formato:
# (origen, destino, tiempo_en_minutos, linea)

rutas = [
    ("1", "2", 8, "L1"),
    ("2", "1", 8, "L1"),
    ("2", "3", 6, "L1"),
    ("3", "2", 6, "L1"),
    ("3", "4", 10, "L1"),
    ("4", "3", 10, "L1"),

    ("1", "5", 12, "L2"),
    ("5", "1", 12, "L2"),
    ("5", "2", 7, "L2"),
    ("2", "5", 7, "L2"),
    ("2", "6", 9, "L2"),
    ("6", "2", 9, "L2"),

    ("6", "4", 8, "L3"),
    ("4", "7", 15, "L3"),
    ("4", "6", 8, "L3"),
    ("3", "7", 12, "L4"),
    ("7", "3", 12, "L4"),
    ("7", "4", 15, "L4"),
]


# ------------------------------------------------------------
# 2. REGLAS LÓGICAS: 
# ------------------------------------------------------------

def existe_conexion(origen, destino):
    """
    Regla:
    Si existe una conexión directa entre dos estaciones,
    entonces es posible desplazarse entre ellas.
    """

    for ruta in rutas:
        if ruta[0] == origen and ruta[1] == destino:
            return True

    return False


def obtener_conexiones(estacion):
    """
    Regla:
    Una estación puede conectarse con todas las estaciones
    que aparezcan como destino de una ruta.
    """

    conexiones = []

    for ruta in rutas:
        if ruta[0] == estacion:
            conexiones.append(ruta)

    return conexiones


# ------------------------------------------------------------
# 3. MOTOR DE INFERENCIA: DANIEL
# ------------------------------------------------------------

def buscar_rutas(origen, destino, visitadas=None):
    """
    Busca todas las rutas posibles utilizando las reglas
    de la base de conocimiento.
    """

    if visitadas is None:
        visitadas = []

    # Evitar ciclos
    if origen in visitadas:
        return []

    visitadas = visitadas + [origen]

    # Regla de finalización:
    # Si llegamos al destino, encontramos una ruta.
    if origen == destino:
        return [(0, [origen])]

    soluciones = []

    # Obtener las estaciones conectadas
    conexiones = obtener_conexiones(origen)

    for siguiente in conexiones:

        nueva_estacion = siguiente[1]
        tiempo = siguiente[2]

        # No visitar nuevamente una estación
        if nueva_estacion not in visitadas:

            rutas_restantes = buscar_rutas(
                nueva_estacion,
                destino,
                visitadas
            )

            for tiempo_restante, camino in rutas_restantes:

                tiempo_total = tiempo + tiempo_restante

                soluciones.append(
                    (
                        tiempo_total,
                        [origen] + camino
                    )
                )

    return soluciones


# ------------------------------------------------------------
# 4. REGLA PARA DETERMINAR LA MEJOR RUTA: ALEJO
# ------------------------------------------------------------

def mejor_ruta(origen, destino):

    rutas_encontradas = buscar_rutas(origen, destino)

    # Si no existe una ruta
    if not rutas_encontradas:
        return None

    # Regla lógica:
    # La mejor ruta será aquella cuyo tiempo total sea menor.
    mejor = min(
        rutas_encontradas,
        key=lambda ruta: ruta[0]
    )

    return mejor

# ------------------------------------------------------------
# NOMBRES DE LAS ESTACIONES: ALEJO
# ------------------------------------------------------------

estaciones = {
    "1": "Terminal",
    "2": "Centro",
    "3": "Parque",
    "4": "Universidad",
    "5": "Estadio",
    "6": "Hospital",
    "7": "Aeropuerto",
}


# ------------------------------------------------------------
# 5. MOSTRAR RESULTADO: ALEJO
# ------------------------------------------------------------

def mostrar_ruta(origen, destino):

    resultado = mejor_ruta(origen, destino)
    
    print("\n==========================================")
    print(" RESULTADO DE LA BÚSQUEDA DE RUTA")

    print(f"Origen:  {estaciones.get(origen,origen)}")
    print(f"Destino: {estaciones.get(destino,destino)}")

    if resultado is None:
        print("\nNo existe una ruta disponible.")
        return

    tiempo, camino = resultado

    print("\nMejor ruta encontrada:")

    for i, estacion in enumerate(camino):
        
        # Convertir número a nombre
        nombre_estacion = estaciones.get(estacion, estacion)

        if i < len(camino) - 1:
            print(nombre_estacion, "->", end=" ")

        else:
            print(nombre_estacion)

    print(f"\nTiempo estimado: {tiempo} minutos")


# ------------------------------------------------------------
# 6. EJECUCIÓN DEL SISTEMA: ALEJO
# ------------------------------------------------------------

print("\n==========================================")
print(" SISTEMA INTELIGENTE DE TRANSPORTE")
print("==========================================")
    
print("\nEstaciones disponibles:")
for numero, nombre in estaciones.items():
    print(f"{numero}. {nombre}")

origen = input("Ingrese el número de la estación de origen: ")
destino = input("Ingrese el número de la estación de destino: ")

mostrar_ruta(origen, destino)
