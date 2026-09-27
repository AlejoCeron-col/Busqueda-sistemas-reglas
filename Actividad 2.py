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
