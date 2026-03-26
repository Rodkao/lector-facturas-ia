import pypdf
import ollama
import pandas as pd
import io

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    with open(ruta_pdf, "rb") as f:
        lector = pypdf.PdfReader(f)
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def estructurar_texto(texto, prompt):
    respuesta = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nTexto de la factura:\n{texto}"
            }
        ]
    )
    return respuesta["message"]["content"]

def csv_a_dataframe(texto_csv):
    try:
        primera_linea = texto_csv.strip().split("\n")[0].lower()
        if "fecha" in primera_linea:
            df = pd.read_csv(io.StringIO(texto_csv))
        else:
            df = pd.read_csv(io.StringIO(texto_csv),
                           header=None,
                           names=["fecha", "proveedor", "concepto", "importe", "moneda"])
        df["importe"] = pd.to_numeric(
            df["importe"].astype(str).str.replace(",", "."),
            errors="coerce"
        )
        return df
    except Exception as e:
        print(f"Error al convertir CSV: {e}")
        return None