# data-analytics-tfm

Este proyecto forma parte nuestro Trabajo Final de Máster (TFM) enfocado en la aplicación de análisis de datos y modelado predictivo para optimizar el marketing directo en el sector de la Banca y Servicios Financieros.

Problema de Negocio

La entidad financiera enfrenta el desafío de maximizar la conversión de depósitos a plazo fijo mediante telemarketing.  Actualmente, existe:

    - Eficiencia operativa baja: Se realizan múltiples llamadas al mismo cliente sin garantía de éxito.

    -Volatilidad estacional: Concentración ineficiente de actividades en meses específicos (ej. mayo vs. noviembre).

    -Costes elevados: Recursos humanos y técnicos no optimizados según la propensión de compra del cliente.

Objetivo

    Analizar los datos de campañas de marketing de una empresa Fintech para identificar y predecir 
    los factores que hacen que un cliente contrate un depósito.

Dataset

    Source: Dataset privado proporcionado por el master (no disponible públicamente)
    Contenido: Datos crudos y procesados

Metodología
El notebook sigue una metodología rigurosa de ciencia de datos:

    Definición Estratégica: Establecimiento de objetivos generales, tácticas y árbol de indicadores (KPIs).

    Configuración y Carga: Preparación del entorno Python y librerías (Pandas, Seaborn, Plotly, FuzzyWuzzy).

    Exploración de Datos (EDA): Comprensión de perfiles demográficos, variables macroeconómicas (Euribor, inflación) y determinantes operativos.

    Limpieza de Datos: Procesamiento de valores nulos, duplicados, outliers y normalización de variables categóricas.

    Análisis de KPIs: * Penetración en Contexto de Tasas: Análisis del impacto del Euríbor en la contratación.

    Elasticidad de Conversión: Relación entre variaciones de mercado y ventas.

    Tasa de Recurrencia: Análisis de clientes con historial de éxito previo.

Principales Hallazgos (Insights)

    Ventana de Oportunidad: Se detectó un punto positivo de conversión en periodos con Euríbor superior al 4.8%.
    
    Perfil de Alta Conversión: Los perfiles administrativos con educación universitaria muestran una estabilidad financiera que correlaciona positivamente con la suscripción de depósitos.
    
    Fatiga del Cliente: El análisis de frecuencia de contacto sugiere un límite óptimo de llamadas antes de que la probabilidad de éxito decaiga drásticamente.

Entregables

    Documento técnico con metodología y resultados
    Entregables solicitados para cada tarea
    Presentación final para la junta ejecutiva de la Fintech

How to Use

    Abrir el notebook para ejecutar el análisis o abrir el PDF de la presentación.      
