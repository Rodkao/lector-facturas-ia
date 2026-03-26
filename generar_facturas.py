from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import random

os.makedirs("facturas", exist_ok=True)

proveedores = [
    {"nombre": "Spotify", "concepto": "Suscripcion premium", "importe_min": 1299, "importe_max": 1599, "moneda": "ARS"},
    {"nombre": "Netflix", "concepto": "Suscripcion plan estandar", "importe_min": 2699, "importe_max": 3199, "moneda": "ARS"},
    {"nombre": "Disney Plus", "concepto": "Suscripcion mensual", "importe_min": 1499, "importe_max": 1799, "moneda": "ARS"},
    {"nombre": "Telecom Argentina", "concepto": "Internet fibra optica", "importe_min": 4500, "importe_max": 6500, "moneda": "ARS"},
    {"nombre": "Edesur", "concepto": "Servicio electrico", "importe_min": 6000, "importe_max": 15000, "moneda": "ARS"},
    {"nombre": "Metrogas", "concepto": "Servicio de gas", "importe_min": 3000, "importe_max": 8000, "moneda": "ARS"},
    {"nombre": "Aysa", "concepto": "Servicio de agua", "importe_min": 2000, "importe_max": 4000, "moneda": "ARS"},
    {"nombre": "Amazon AWS", "concepto": "Servicios cloud", "importe_min": 20, "importe_max": 80, "moneda": "USD"},
    {"nombre": "Adobe", "concepto": "Creative Cloud", "importe_min": 25, "importe_max": 55, "moneda": "USD"},
    {"nombre": "Github", "concepto": "Plan Pro mensual", "importe_min": 4, "importe_max": 7, "moneda": "USD"},
    {"nombre": "Google Workspace", "concepto": "Plan Business Starter", "importe_min": 6, "importe_max": 12, "moneda": "USD"},
    {"nombre": "Mercado Pago", "concepto": "Comision procesamiento pagos", "importe_min": 800, "importe_max": 3000, "moneda": "ARS"},
    {"nombre": "Personal", "concepto": "Servicio celular", "importe_min": 5000, "importe_max": 9000, "moneda": "ARS"},
    {"nombre": "Claro", "concepto": "Servicio celular", "importe_min": 5000, "importe_max": 9000, "moneda": "ARS"},
    {"nombre": "HBO Max", "concepto": "Suscripcion mensual", "importe_min": 1899, "importe_max": 2299, "moneda": "ARS"},
]

meses = [
    ("2024-01", 31), ("2024-02", 28), ("2024-03", 31),
    ("2024-04", 30), ("2024-05", 31), ("2024-06", 30),
    ("2024-07", 31), ("2024-08", 31), ("2024-09", 30),
    ("2024-10", 31), ("2024-11", 30), ("2024-12", 31),
]

facturas = []
for mes, dias in meses:
    seleccionados = random.sample(proveedores, k=random.randint(4, 6))
    for prov in seleccionados:
        dia = str(random.randint(1, dias)).zfill(2)
        importe = round(random.uniform(prov["importe_min"], prov["importe_max"]), 2)
        facturas.append({
            "proveedor": prov["nombre"],
            "fecha": f"{mes}-{dia}",
            "concepto": f"{prov['concepto']} {mes}",
            "importe": importe,
            "moneda": prov["moneda"]
        })

for i, datos in enumerate(facturas, 1):
    ruta = f"facturas/factura_{str(i).zfill(3)}.pdf"
    c = canvas.Canvas(ruta, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "FACTURA")
    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Proveedor: {datos['proveedor']}")
    c.drawString(50, 750, f"Fecha: {datos['fecha']}")
    c.drawString(50, 730, f"Concepto: {datos['concepto']}")
    c.drawString(50, 710, f"Importe: {datos['importe']} {datos['moneda']}")
    c.save()

print(f"Listo! {len(facturas)} facturas creadas en /facturas")