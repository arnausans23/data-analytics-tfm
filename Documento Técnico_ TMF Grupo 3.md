**Memoria Trabajo Final de Master: Marketing Analytics para Fintech**  
**Grupo 3**  
**Integrantes:** Arnau Sans, Sergi Pedrosa, Estefania Escribano, Francesc Mesquida

## **1\. Introducción y Contexto**

El presente proyecto tiene como objetivo principal identificar los patrones, tendencias y factores determinantes que influyen en la contratación de depósitos a plazo dentro de una entidad Fintech. El sector financiero actual exige una optimización de los recursos de marketing, por lo que este análisis busca predecir la efectividad de las campañas para mejorar la toma de decisiones estratégicas.

El conjunto de datos analizado recoge los resultados de campañas de marketing directo basadas en llamadas telefónicas realizadas entre mayo de 2018 y noviembre de 2020\. Se destaca que el dataset presenta una estructura cronológica, aunque carece de una variable de fecha completa original.

## **2\. Marco Estratégico y Métricas Clave**

### **2.1. North Star Metric (NSM): Ratio de Contratación**

Para este proyecto, se define el **Ratio de Contratación** como la métrica "North Star Metric".

* **Definición:** Relación porcentual entre el número de depósitos efectivamente contratados frente al número total de contactos realizados.  
* **Razonamiento:** Esta métrica refleja la eficiencia real de la campaña. Al medir esta relación, se evalúa si el esfuerzo comercial está alineado con la respuesta del mercado, permitiendo optimizar el Retorno de la Inversión (ROI).

### **2.2. Objetivos Generales del Proyecto**

#### **Objetivo 1: Aumento de la Contratación (Crecimiento de Clientes)**

* **Definición:** Incrementar el volumen de contrataciones de depósitos.  
* **Restricción:** Mantener el mismo número de llamadas (eficiencia operativa).  
* **Plazo:** Dos años.  
* **Justificación:** Los ingresos de la Fintech dependen directamente del volumen de clientes obtenidos; este objetivo busca maximizar el *output* sin elevar los costes de captación.  
* **Recomendación técnica:** Realizar un análisis del macro-entorno (Euribor, IPC) para asegurar que las metas de crecimiento son realistas frente a la coyuntura económica del sector.

#### **Objetivo 2: Optimización del Contacto Comercial**

* **Definición:** Mejorar la calidad y el *timing* de cada interacción telefónica.  
* **Justificación:** Maximizar la eficiencia operativa reduciendo llamadas innecesarias y costes asociados. Permite identificar la duración ideal del contacto para asegurar la suscripción sin saturar al cliente, garantizando que el equipo comercial se enfoque solo en las interacciones con mayor probabilidad de éxito.

## **3\. Metodología de Análisis de Datos**

### **3.1. Exploración de Datos (EDA)**

Se ha trabajado con un dataset compuesto por **41,188 registros y 21 variables** que describen el perfil del cliente, el contexto socioeconómico y los detalles del contacto.

* **Variables de Cliente:** Edad, trabajo, estado civil, educación y situación de crédito (default, vivienda, préstamo).  
* **Detalles de Campaña:** Mes, día de la semana y duración de la llamada.  
* **Contexto Económico:** Indicadores como la tasa de variación del empleo, el índice de precios al consumo y el Euribor.

### **3.2. Limpieza y Preparación**

Durante la fase de limpieza, se identificó una presencia significativa de valores catalogados como **"unknown"** en variables críticas como job (trabajo), education (educación) y default (incumplimiento de pagos). El tratamiento de estos valores es fundamental para no sesgar las estadísticas descriptivas ni los resultados del modelo predictivo.

### **3.3. Segmentación y Análisis de Respuesta**

Se evaluó el impacto de las características demográficas en la variable objetivo y (suscripción al depósito):

* **Perfil Demográfico:** Comparación de tasas de éxito según el nivel educativo y tipo de empleo.  
* **Eficiencia de Contacto:** Análisis de la relación entre el número de contactos realizados durante la campaña y la probabilidad de éxito.

## **4\. Modelado Predictivo**

Se implementó un modelo de **Regresión Logística simple** para predecir la probabilidad de que un cliente contrate un depósito a plazo.

* **Variables Seleccionadas:** Se priorizaron aquellas con mayor correlación con el éxito, incluyendo la duración de la llamada y variables macroeconómicas.  
* **Evaluación del Modelo:** El rendimiento se midió a través de métricas de **precisión (accuracy), sensibilidad (recall) y especificidad**.

## **5\. Resultados e Insights Clave**

A partir del análisis y el modelado, se extrajeron las siguientes conclusiones de negocio:

* **Impacto de la Duración:** La duración de la llamada es uno de los indicadores más fuertes del éxito de la campaña; sin embargo, no es un factor predictivo *a priori*, sino un indicador de interés durante la ejecución.  
* **Variables Macroeconómicas:** Factores externos como el **Euribor** muestran una influencia directa en la disposición del cliente para contratar productos de ahorro.  
* **Temporalidad:** Se identificaron meses y días de la semana específicos donde la tasa de respuesta positiva es significativamente superior, permitiendo optimizar el calendario de futuras campañas.

## **6\. Recomendaciones Estratégicas**

Basado en los hallazgos, se proponen las siguientes acciones:

1. **Focalización:** Priorizar segmentos demográficos con mayores tasas de conversión histórica identificados en el dashboard.  
2. **Optimización de Contacto:** Reducir el número de re-contactos tras un umbral específico para evitar la fatiga del cliente y optimizar costes operativos.  
3. **Monitoreo del Entorno:** Ajustar las campañas de depósitos según la evolución de los tipos de interés (Euribor) para alinear la oferta con el mercado.

