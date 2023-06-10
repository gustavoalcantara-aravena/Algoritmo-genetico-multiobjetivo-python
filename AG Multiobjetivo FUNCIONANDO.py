import random

# Definir la clase de Proceso Minero
class ProcesoMinero:
    def __init__(self, id_proceso, duracion, beneficio, componentes_40):
        self.id_proceso = id_proceso
        self.duracion = duracion
        self.beneficio = beneficio
        self.componentes_40 = componentes_40

# Definir los procesos mineros
procesos_mineros = [
    ProcesoMinero(0, 10, 100, ["Automatización y control inteligente"]),   # Exploración
    ProcesoMinero(1, 8, 80, ["Monitoreo en tiempo real"]),     # Perforación
    ProcesoMinero(2, 6, 60, ["Análisis de datos y big data"]),     # Voladura
    ProcesoMinero(3, 7, 70, []),     # Carga
    ProcesoMinero(4, 5, 50, ["Automatización y control inteligente"]),     # Transporte
    ProcesoMinero(5, 4, 40, []),     # Trituración
    ProcesoMinero(6, 6, 60, ["Automatización y control inteligente", "Ciberseguridad"]),     # Separación
    ProcesoMinero(7, 9, 90, []),     # Refinación
    ProcesoMinero(8, 7, 70, []),     # Desarrollo de infraestructuras
    ProcesoMinero(9, 5, 50, []),     # Rehabilitación ambiental
    ProcesoMinero(10, 6, 60, ["Monitoreo en tiempo real", "Análisis de datos y big data"]),    # Proceso adicional 1
    ProcesoMinero(11, 4, 40, ["Automatización y control inteligente"]),    # Proceso adicional 2
    ProcesoMinero(12, 7, 70, ["Simulación y modelado"]),    # Proceso adicional 3
    ProcesoMinero(13, 8, 80, ["Automatización y control inteligente"]),    # Proceso adicional 4
    ProcesoMinero(14, 5, 50, ["Ciberseguridad"])     # Proceso adicional 5
]

# Definir la función de evaluación multiobjetivo
def evaluar(cromosoma):
    rendimiento_economico = 0
    beneficio_trabajadores = 0
    duracion_total = 0
    componentes_40_presentes = set()
    for i, gen in enumerate(cromosoma):
        proceso = procesos_mineros[gen]
        duracion_total += proceso.duracion
        rendimiento_economico += proceso.duracion * proceso.beneficio
        beneficio_trabajadores += proceso.beneficio
        componentes_40_presentes.update(proceso.componentes_40)
        if i > 0:
            # Aplicar restricciones adicionales basadas en las relaciones entre los procesos
            proceso_anterior = procesos_mineros[cromosoma[i - 1]]
            if "Automatización y control inteligente" in proceso.componentes_40 and \
                    "Automatización y control inteligente" not in proceso_anterior.componentes_40:
                rendimiento_economico *= 0.5  # Penalizar si no hay continuidad en la automatización y control inteligente
    return rendimiento_economico, beneficio_trabajadores, duracion_total, list(componentes_40_presentes)

# Definir las operaciones genéticas
def seleccion(cromosomas, fitness):
    cromosomas_seleccionados = []
    while len(cromosomas_seleccionados) < len(cromosomas):
        idx = random.randint(0, len(cromosomas) - 1)
        if es_no_dominada(fitness[idx], cromosomas, fitness):
            cromosomas_seleccionados.append(cromosomas[idx])
    return cromosomas_seleccionados

def es_no_dominada(fitness, cromosomas, fitness_cromosomas):
    for i, cromosoma in enumerate(cromosomas):
        if fitness_cromosomas[i] != fitness:
            if (fitness_cromosomas[i][0] >= fitness[0] and fitness_cromosomas[i][1] >= fitness[1]) or \
               (fitness_cromosomas[i][0] > fitness[0] and fitness_cromosomas[i][1] > fitness[1]):
                return False
    return True

def cruza(cromosoma_actual, otro_cromosoma):
    punto_cruza = random.randint(1, len(cromosoma_actual) - 1)
    nuevo_cromosoma = cromosoma_actual[:punto_cruza] + otro_cromosoma[punto_cruza:]
    return nuevo_cromosoma

def mutacion(cromosoma, prob_mutacion):
    for i in range(len(cromosoma)):
        if random.random() < prob_mutacion:
            nuevo_gen = random.randint(0, len(procesos_mineros) - 1)
            cromosoma[i] = nuevo_gen
    return cromosoma

# Definir los parámetros del algoritmo genético
tamano_poblacion = 50
num_generaciones = 50
prob_mutacion = 0.1
tasa_elitismo = 0.1  # Tasa de elitismo del 10%

# Inicializar la población inicial
poblacion = []
for _ in range(tamano_poblacion):
    cromosoma = [random.randint(0, len(procesos_mineros) - 1) for _ in range(len(procesos_mineros))]
    poblacion.append(cromosoma)

# Ejecutar el algoritmo genético
for generacion in range(num_generaciones):
    fitness = []
    for cromosoma in poblacion:
        fitness.append(evaluar(cromosoma))

    # Obtener las mejores soluciones de la generación actual
    mejores_soluciones = []
    for cromosoma, fit in zip(poblacion, fitness):
        if es_no_dominada(fit, poblacion, fitness):
            mejores_soluciones.append((cromosoma, fit))

    # Ordenar las mejores soluciones por su dominancia
    mejores_soluciones.sort(key=lambda x: x[1])

    # Obtener las soluciones elitistas
    num_elitismo = int(tamano_poblacion * tasa_elitismo)
    soluciones_elitistas = [sol[0] for sol in mejores_soluciones[:num_elitismo]]

    nueva_generacion = []

    # Agregar las soluciones elitistas a la nueva generación sin cambios
    nueva_generacion.extend(soluciones_elitistas)

    # Generar el resto de la nueva generación mediante selección, cruza y mutación
    while len(nueva_generacion) < tamano_poblacion:
        cromosoma_actual = random.choice(poblacion)
        otro_cromosoma = random.choice(poblacion)
        nuevo_cromosoma = cruza(cromosoma_actual, otro_cromosoma)
        nuevo_cromosoma = mutacion(nuevo_cromosoma, prob_mutacion)
        nueva_generacion.append(nuevo_cromosoma)

    poblacion = nueva_generacion

    # Obtener el mejor cromosoma de la generación actual y mostrar resultados
    fitness_generacion = [evaluar(cromosoma) for cromosoma in poblacion]
    mejor_cromosoma_generacion = poblacion[fitness_generacion.index(max(fitness_generacion))]

    print("Generación:", generacion)
    print("Mejor solución encontrada hasta ahora:")
    print("Cromosoma:", mejor_cromosoma_generacion)
    print("Rendimiento Económico:", evaluar(mejor_cromosoma_generacion)[0])
    print("Beneficio Trabajadores:", evaluar(mejor_cromosoma_generacion)[1])
    print("Duración Total:", evaluar(mejor_cromosoma_generacion)[2])
    print("Componentes 4.0 presentes:", evaluar(mejor_cromosoma_generacion)[3])
    print("Fitness:", max(fitness_generacion, key=lambda x: x[0]))
    print("============================================")

# Obtener el mejor cromosoma de la última generación
fitness = [evaluar(cromosoma) for cromosoma in poblacion]
mejor_cromosoma = poblacion[fitness.index(max(fitness))]
mejor_rendimiento_economico, mejor_beneficio_trabajadores, mejor_duracion_total, componentes_40_presentes = evaluar(mejor_cromosoma)

# Verificar reglas básicas de dominancia
cromosomas_seleccionados = []  # Variable para almacenar las soluciones seleccionadas
for solucion in poblacion:
    es_no_dominante = True
    for otra_solucion in poblacion:
        if otra_solucion != solucion:
            if (otra_solucion[0] >= solucion[0] and otra_solucion[1] >= solucion[1]) or \
               (otra_solucion[0] > solucion[0] and otra_solucion[1] > solucion[1]):
                es_no_dominante = False
                break
    if es_no_dominante:
        cromosomas_seleccionados.append(solucion)  # Agregar la solución no dominada

# Verificar que las soluciones seleccionadas sean no dominadas
for solucion in cromosomas_seleccionados:
    for otra_solucion in cromosomas_seleccionados:
        if otra_solucion != solucion:
            assert not ((otra_solucion[0] >= solucion[0] and otra_solucion[1] >= solucion[1]) or \
                        (otra_solucion[0] > solucion[0] and otra_solucion[1] > solucion[1])), \
                        "Error: una solución dominante fue seleccionada en lugar de una no dominada"

# Imprimir los resultados
print("Mejor solución encontrada:")
print("Cromosoma:", mejor_cromosoma)
print("Rendimiento Económico:", mejor_rendimiento_economico)
print("Beneficio Trabajadores:", mejor_beneficio_trabajadores)
print("Duración Total:", mejor_duracion_total)
print("Componentes 4.0 presentes:", componentes_40_presentes)
print("Fitness:", max(fitness, key=lambda x: x[0]))


