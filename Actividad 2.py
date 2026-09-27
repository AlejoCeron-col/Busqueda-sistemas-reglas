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
