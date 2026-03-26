import os
import pandas as pd
from sqlalchemy import create_engine
from funciones import extraer_texto_pdf, estructurar_texto, csv_a_dataframe
from prompt import PROMPT_FACTURAS

CARPETA_FACTURAS = "facturas"
BASE_DE_DATOS = "facturas.db"

df_total = pd.DataFrame()

for carpeta_raiz, subcarpetas, archivos in os.walk(CARPETA_FACTURAS):
    for archivo in archivos:
        if archivo.endswith(".pdf"):
            ruta = os.path.join(carpeta_raiz, archivo)
            print(f"Procesando: {ruta}")

            texto = extraer_texto_pdf(ruta)
            texto_estructurado = estructurar_texto(texto, PROMPT_FACTURAS)
            if texto_estructurado.strip() == "ERROR":
                print(f"  No se pudo extraer datos de {archivo}")
                continue

            df = csv_a_dataframe(texto_estructurado)

            if df is not None:
                df["archivo"] = archivo
                df_total = pd.concat([df_total, df], ignore_index=True)
                print(f"  OK")

if not df_total.empty:
    engine = create_engine(f"sqlite:///{BASE_DE_DATOS}")
    df_total.to_sql("facturas", engine, if_exists="replace", index=False)
    print(f"\nListo. {len(df_total)} facturas guardadas en {BASE_DE_DATOS}")
else:
    print("\nNo se procesó ninguna factura.")