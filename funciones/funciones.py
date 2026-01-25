import datetime
import re

def check_df(df, tipo=""):
    if tipo == "simple":
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))

        print("¿Cuáles son las primeras dos filas del conjunto de datos?")
        display(df.head(2))
        print(
            "\n########################################################################################"
        )
    else:
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))
        print(
            "\n########################################################################################"
        )

        print("¿Cuáles son las primeras cinco filas del conjunto de datos?")
        display(df.head())
        print(
            "\n########################################################################################"
        )

        print("¿Cuáles son las últimas cinco filas del conjunto de datos?")
        display(df.tail())
        print(
            "\n########################################################################################"
        )

        print(
            "¿Cómo puedes obtener una muestra aleatoria de filas del conjunto de datos?"
        )
        display(df.sample(n=5))
        print(
            "\n########################################################################################"
        )

        print(
            "¿Cuáles son las columnas del conjunto de datos? ¿Cuál es el tipo de datos de cada columna?"
        )
        print(df.dtypes)
        print(
            "\n########################################################################################"
        )

        print("¿Cuántas columnas hay de cada tipo de datos?")
        print(df.dtypes.value_counts())
        print(
            "\n########################################################################################"
        )

        print("¿Cuáles son las variables numéricas?")
        df_numericas = df.select_dtypes(include="number")
        columnas_numericas = list(df_numericas.columns)
        print(columnas_numericas)
        print(
            "\n########################################################################################"
        )

        print("¿Cuáles son las variables categóricas?")
        df_categoricas = df.select_dtypes(include="object")
        columnas_categoricas = list(df_categoricas.columns)
        print(columnas_categoricas)
        print(
            "\n########################################################################################"
        )

        print("¿Cuántos valores únicos tiene cada columna?")
        print(df.nunique())
        print(
            "\n########################################################################################"
        )

        if len(columnas_numericas) > 0:
            print(
                "¿Cuáles son las estadísticas descriptivas básicas de las columnas numéricas?"
            )
            display(df.describe(include="number"))
            print(
                "\n########################################################################################"
            )

        if len(columnas_categoricas) > 0:
            print(
                "¿Cuáles son las estadísticas descriptivas básicas de las columnas categóricas?"
            )
            display(df.describe(include="object"))

def identificacion_valores_problem(df, columnas=[]):
    print('###################################################################################')
    print('3.1.1. Proporción de NULOS en cada una de las columnas del conjunto de datos:')
    print(round((df.isnull().sum()/len(df))*100, 2).sort_values(ascending= False))
    print('###################################################################################')
    print(f'3.1.2. Número de DUPLICADOS totales: {df.duplicated().sum()}')
    print('###################################################################################')
    if len(columnas) > 0:
        print(f'3.1.2. Número de DUPLICADOS parciales según las columnas {columnas}: {df.duplicated(subset=columnas).sum()}')
        print('###################################################################################')
    df_numericas = df.select_dtypes(include = 'number')
    columnas_numericas = list(df_numericas.columns)
    if len(columnas_numericas) > 0:
        print('3.1.3. Columnas numéricas con OUTLIERS')
        for var in columnas_numericas:
            Q1 = df[var].quantile(0.25)
            Q3 = df[var].quantile(0.75)
            limite_inferior = Q1 - 1.5 * (Q3 - Q1)
            limite_superior = Q3 + 1.5 * (Q3 - Q1)
            outliers = df[(df[var] < limite_inferior) | (df[var] > limite_superior)]
            print(f'Número de outliers en la columna "{var}": {outliers.shape[0]}')
        print('###################################################################################')

def eur_good(v):
    # 1. Caso datetime
    if isinstance(v, datetime.datetime):
        # Tomamos mes, día, hora, minuto → últimos 4 números
        digits = f"{v.month}{v.day}{v.hour}{v.minute}"
        return float(digits[0] + "." + digits[1:])

    # 2. Caso string
    if isinstance(v, str):
        # Aseguramos formato decimal
        if re.fullmatch(r"\d+\.\d+", v):
            # añadimos un decimal más si solo tiene 2
            entero, dec = v.split(".")
            if len(dec) == 2:
                dec += "0"
            return float(entero + "." + dec)

        # si es otra cosa rara, lo intentamos convertir
        v = int(v)

    # 3. Caso entero (ya convertido o original)
    if isinstance(v, int):
        s = str(v)

        # 4 dígitos → x.xxx
        if len(s) == 4:
            return float(s[0] + "." + s[1:])

        # 3 dígitos → 0.xxx
        if len(s) == 3:
            return float("0." + s)

        # 1 dígito (ej: 1 o 5)
        if len(s) == 1:
            return float(f"{s}.000")

    # 4. Fallback defensivo
    return float(v)