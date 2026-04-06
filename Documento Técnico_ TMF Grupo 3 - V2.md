**Trabajo Final de Master: Marketing Analytics para Fintech**  
**Grupo 3**  
**Integrantes:** Arnau Sans, Sergi Pedrosa, Estefania Escribano, Francesc Mesquida

# **MEMORIA TÉCNICA: MARKETING ANALYTICS PARA FINTECH**

**Enfoque:** Optimización de Campañas de Captación de Depósitos

**Audiencia:** Marketing Manager

## **1\. INTRODUCCIÓN Y CONTEXTO ESTRATÉGICO**

El presente proyecto surge de la necesidad de la Fintech de optimizar sus recursos de marketing directo. El objetivo central es identificar los patrones, tendencias y factores críticos que influyen en que un cliente decida contratar un depósito a plazo.

El análisis se basa en datos históricos de campañas telefónicas realizadas entre **mayo de 2018 y noviembre de 2020**. Entendemos que el éxito de la conversión no es fortuito, sino el resultado de la interacción entre el perfil demográfico del cliente, la gestión del contacto comercial y el contexto macroeconómico del momento.

## **2\. NORTH STAR METRIC (NSM): RATIO DE CONTRATACIÓN**

Para alinear los esfuerzos analíticos con el crecimiento del negocio, hemos establecido el **Ratio de Contratación** como nuestra métrica principal (North Star Metric).

* **Definición:** Relación porcentual entre el número de depósitos contratados y el total de contactos realizados.  
* **Razonamiento:** Es el indicador más fiel de la eficiencia de la campaña. Al medir esta relación, evaluamos si el esfuerzo comercial está alineado con la respuesta del mercado, permitiendo optimizar el ROI al evitar el contacto con perfiles de baja conversión.

  ## **3\. OBJETIVOS ESTRATÉGICOS**

  ### **Objetivo General 1: Aumentar la Contratación (Crecimiento de Cartera)**

* **Acción:** Incremento del volumen de clientes.  
* **Métrica:** Número total de suscripciones (Contrataciones).  
* **Restricción:** Mantener el mismo número actual de llamadas (eficiencia pura).  
* **Tiempo:** 2 años.  
* **Justificación:** De este objetivo dependen directamente los ingresos por captación de la entidad.

  ### **Objetivo General 2: Optimización del Contacto Comercial**

* **Acción:** Refinamiento del proceso de ventas.  
* **Métrica:** Contacto comercial efectivo.  
* **Justificación:** Maximizar la eficiencia operativa reduciendo llamadas innecesarias y costes asociados. Identificar la duración y el momento ideal del contacto para asegurar la suscripción sin saturar al cliente, permitiendo que el equipo comercial se enfoque solo en leads con alta probabilidad de éxito.

  ## **4\. DEFINICIÓN DE KPIs PARA EL DASHBOARD**

Para monitorear estos objetivos, el dashboard ejecutivo incluirá:

1. **Ratio de Contratación (NSM):** Control de la eficiencia global de la campaña.  
2. **Volumen de Suscripciones:** Seguimiento del crecimiento neto de clientes.  
3. **Duración Media de Llamada:** Indicador de engagement y calidad del contacto.  
4. **Frecuencia de Contacto por Cliente:** Control para evitar la saturación y optimizar el coste por adquisición.  
5. **Tasa de Éxito por Segmento:** Rendimiento según trabajo, educación y edad del cliente.

   ## **5\. METODOLOGÍA DE ANÁLISIS**

   ### **5.1. Análisis Exploratorio y Limpieza (EDA)**

Trabajamos con un conjunto de **41,188 registros y 21 variables**.

* **Limpieza:** Se identificaron y trataron valores "unknown" en variables como job, education y default.  
* **Análisis Demográfico:** Se analizó la relación entre el perfil del cliente (edad, trabajo, educación) y la suscripción efectiva.

  ### **5.2. Análisis de la Respuesta de la Campaña**

* Evaluamos el impacto de los detalles de la campaña, como el mes y día de la semana, en el resultado final.  
* Se identificó que la **duración de la llamada** es un indicador potente del éxito, sugiriendo que el interés del cliente se manifiesta en el tiempo de escucha activa.

  ### **5.3. Modelado Predictivo**

Implementamos un modelo de **Regresión Logística** para predecir la probabilidad de suscripción.

* **Evaluación:** El modelo fue validado mediante métricas de precisión, sensibilidad y especificidad para asegurar que las recomendaciones de contacto sean fiables.

  ## **6\. RESULTADOS E INSIGHTS CLAVE**

* **Macro-entorno:** El análisis revela que factores externos (como el **Euribor**) tienen una influencia directa en la realidad del sector y la disposición al ahorro.  
* **Variables de éxito:** La combinación de un perfil profesional estable con un contacto telefónico de calidad (duración óptima) dispara el Ratio de Contratación.  
* **Patrones temporales:** Existen meses específicos donde la efectividad de la campaña es notablemente superior, lo que permite una planificación de medios más inteligente.

  ## **7\. RECOMENDACIONES ESTRATÉGICAS**

1. **Priorización de Leads:** Utilizar el modelo predictivo para llamar primero a los perfiles con mayor probabilidad de éxito, cumpliendo así el objetivo de aumentar contrataciones sin subir el volumen de llamadas.  
2. **Ajuste por Coyuntura:** Sincronizar las ofertas de depósitos con las fluctuaciones del Euribor para mejorar la relevancia del mensaje comercial.  
3. **Entrenamiento Comercial:** Capacitar al equipo para identificar señales de interés que prolonguen la duración del contacto útil, basándose en los KPIs de calidad definidos.

