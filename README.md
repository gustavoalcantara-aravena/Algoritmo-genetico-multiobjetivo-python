
# ⛏️ **Algoritmo Genético para Optimización de Procesos Mineros**

Este proyecto implementa un **algoritmo genético** para optimizar procesos mineros bajo un enfoque de evaluación multiobjetivo. Utiliza métricas como **rendimiento económico**, **beneficio para los trabajadores**, y **duración total de los procesos**. Además, incluye la evaluación de tecnologías **Industria 4.0** aplicadas a cada proceso. 🚀

---

## 📋 **Características**
- ✅ **Optimización Multiobjetivo:** Evaluación basada en múltiples criterios como economía, eficiencia y beneficio social.
- ♻️ **Operadores Genéticos:** Implementación de selección, cruza y mutación.
- 🔍 **Procesos Mineros Modelados:** Incluye 15 procesos modelados con beneficios, duración y tecnologías asociadas.
- ⚙️ **Soporte para Industria 4.0:** Identificación de tecnologías clave como:
  - Automatización y control inteligente.
  - Análisis de datos y big data.
  - Ciberseguridad.
  - Simulación y modelado.
  - Monitoreo en tiempo real.

---

## 🛠️ **Requisitos**
Asegúrate de tener instalado:
- **Python 3.8** o superior 🐍
- Módulo estándar `random`.

---

## 🚀 **Cómo Ejecutar**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/mining-genetic-algorithm.git
   cd mining-genetic-algorithm
   ```
2. Ejecuta el script principal:
   ```bash
   python proceso_minero.py
   ```

3. Observa los resultados generados por el algoritmo, incluyendo:
   - **El mejor cromosoma** de cada generación.
   - **Rendimiento económico** de las mejores soluciones.
   - **Duración total** de los procesos optimizados.
   - **Componentes 4.0 presentes** en las soluciones encontradas.

---

## 🧪 **Detalles del Algoritmo**
### 🏗️ **Evaluación Multiobjetivo**
Cada cromosoma representa una secuencia de procesos mineros. El algoritmo evalúa:
- **Rendimiento Económico:** Basado en la duración y el beneficio de cada proceso.
- **Beneficio para los Trabajadores:** Suma de los beneficios de los procesos seleccionados.
- **Duración Total:** Tiempo total requerido por los procesos seleccionados.
- **Tecnologías 4.0 presentes:** Validación de las tecnologías aplicadas.

### 🔧 **Operadores Genéticos**
- **Selección:** Identificación de soluciones no dominadas para crear la siguiente generación.
- **Cruza:** Intercambio de genes entre cromosomas para diversificar soluciones.
- **Mutación:** Alteración aleatoria de genes para explorar nuevas soluciones.

### 💡 **Restricciones Incorporadas**
- Penalización si no hay continuidad en el uso de tecnologías como "Automatización y control inteligente".
- Validación de soluciones no dominadas para cumplir los objetivos multiobjetivo.

---

## 📈 **Resultados Esperados**
El script imprime en cada generación:
- Mejor cromosoma encontrado.
- Métricas clave como rendimiento económico, beneficio para trabajadores y duración total.
- Componentes 4.0 presentes en la solución.

Ejemplo de salida:
```
Generación: 5
Mejor solución encontrada hasta ahora:
Cromosoma: [0, 2, 6, 8, 11]
Rendimiento Económico: 1250
Beneficio Trabajadores: 350
Duración Total: 30
Componentes 4.0 presentes: ['Automatización y control inteligente', 'Ciberseguridad']
```

---

## 🧑‍💻 **Contribuciones**
¡Las contribuciones son bienvenidas! Para colaborar:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Envía un pull request explicando tus cambios.

---

## 📜 **Licencia**
Este proyecto está licenciado bajo la [MIT License](LICENSE). Siéntete libre de usarlo y mejorarlo. 🤝

---
