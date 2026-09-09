#!/usr/bin/env python3
"""Genera cotización PDF Jayson Tech."""

from datetime import date
from fpdf import FPDF

LOGO = "/workspace/images/jaysontech_logo.png"
OUTPUT = "/workspace/cotizaciones/Cotizacion-Arquitectura-360-SAS-JaysonTech.pdf"
CLIENTE = "Arquitectura 360 S.A.S"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PRECIO_DESARROLLO = 350_000
PRECIO_HOSTING = 100_000
PRECIO_DOMINIO_MIN = 70_000
PRECIO_DOMINIO_MAX = 120_000
TOTAL_MIN = PRECIO_DESARROLLO + PRECIO_HOSTING + PRECIO_DOMINIO_MIN
TOTAL_MAX = PRECIO_DESARROLLO + PRECIO_HOSTING + PRECIO_DOMINIO_MAX

PRIMARY = (44, 62, 80)
SECONDARY = (52, 152, 219)
TEXT = (51, 51, 51)
MUTED = (127, 140, 141)
LIGHT = (244, 244, 244)


class CotizacionPDF(FPDF):
    def footer(self):
        self.set_y(-18)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 5, "Jayson Tech | https://jaysontech.com.co | WhatsApp: @jayson_ricardo", align="C")
        self.ln(4)
        self.cell(0, 5, f"Página {self.page_no()}/{{nb}}", align="C")


def money(value):
    return f"$ {value:,.0f}".replace(",", ".")


def generar():
    pdf = CotizacionPDF("P", "mm", "Letter")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=22)
    pdf.add_font("DejaVu", "", FONT)
    pdf.add_font("DejaVu", "B", FONT_BOLD)
    pdf.add_page()

    # Header band
    pdf.set_fill_color(*PRIMARY)
    pdf.rect(0, 0, 216, 38, "F")

    pdf.image(LOGO, x=15, y=8, w=18)

    pdf.set_xy(36, 10)
    pdf.set_font("DejaVu", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, "Jayson Tech")

    pdf.set_xy(36, 19)
    pdf.set_font("DejaVu", "", 10)
    pdf.cell(0, 5, "Soluciones Digitales a tu Alcance")

    pdf.set_xy(130, 11)
    pdf.set_font("DejaVu", "B", 11)
    pdf.cell(71, 6, "COTIZACIÓN", align="R")

    pdf.set_xy(130, 18)
    pdf.set_font("DejaVu", "", 9)
    pdf.cell(71, 5, "https://jaysontech.com.co", align="R")
    pdf.set_xy(130, 24)
    pdf.cell(71, 5, "WhatsApp: @jayson_ricardo", align="R")

    # Meta info
    pdf.set_y(48)
    pdf.set_text_color(*TEXT)
    pdf.set_font("DejaVu", "B", 11)
    pdf.cell(95, 7, "No. JT-2026-0909")
    pdf.cell(0, 7, f"Fecha: {date.today().strftime('%d/%m/%Y')}", align="R")
    pdf.ln(10)

    pdf.set_font("DejaVu", "B", 14)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 8, "Landing Page de Presentación — Empresa de Arquitectura")
    pdf.ln(10)

    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(
        0,
        5.5,
        "Cotización para el diseño y desarrollo de una landing page sencilla de presentación "
        "dirigida a una empresa de arquitectura, con información de servicios, portafolio visual "
        "y formulario de contacto para captar clientes potenciales.",
    )
    pdf.ln(4)

    # Client block
    pdf.set_fill_color(*LIGHT)
    pdf.rect(15, pdf.get_y(), 186, 22, "F")
    y = pdf.get_y() + 4
    pdf.set_xy(20, y)
    pdf.set_font("DejaVu", "B", 10)
    pdf.cell(30, 6, "Cliente:")
    pdf.set_font("DejaVu", "", 10)
    pdf.cell(0, 6, CLIENTE)
    pdf.set_xy(20, y + 8)
    pdf.set_font("DejaVu", "B", 10)
    pdf.cell(30, 6, "Proyecto:")
    pdf.set_font("DejaVu", "", 10)
    pdf.cell(0, 6, "Landing page corporativa — Arquitectura 360 S.A.S")
    pdf.ln(18)

    # Scope
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 7, "Alcance del servicio")
    pdf.ln(6)

    scope_items = [
        "Diseño responsive (adaptado a móvil, tablet y escritorio).",
        "Sección de presentación de la empresa y servicios de arquitectura.",
        "Galería o bloques visuales para mostrar proyectos realizados.",
        "Formulario de contacto integrado para recibir solicitudes.",
        "Botón de contacto directo por WhatsApp.",
        "Publicación en hosting y configuración de dominio.",
    ]
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*TEXT)
    for item in scope_items:
        pdf.cell(6, 6, "•")
        pdf.multi_cell(0, 6, item)
        pdf.ln(1)

    pdf.ln(4)

    # Table header
    pdf.set_fill_color(*PRIMARY)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("DejaVu", "B", 10)
    pdf.cell(95, 8, "  Concepto", fill=True)
    pdf.cell(55, 8, "Detalle", fill=True, align="C")
    pdf.cell(36, 8, "Valor (COP)", fill=True, align="R")
    pdf.ln()

    rows = [
        ("Desarrollo Landing Page", "Pago único", money(PRECIO_DESARROLLO), False),
        ("Hosting anual", "Primer año (12 meses)", money(PRECIO_HOSTING), False),
        (
            "Dominio anual *",
            "Primer año",
            f"{money(PRECIO_DOMINIO_MIN)} – {money(PRECIO_DOMINIO_MAX)}",
            True,
        ),
    ]

    pdf.set_text_color(*TEXT)
    pdf.set_font("DejaVu", "", 10)
    for i, (concept, detail, value, variable) in enumerate(rows):
        fill = i % 2 == 1
        pdf.set_fill_color(*LIGHT if fill else (255, 255, 255))
        pdf.cell(95, 10, f"  {concept}", fill=True)
        pdf.cell(55, 10, detail, fill=True, align="C")
        pdf.set_font("DejaVu", "" if variable else "B", 10)
        pdf.cell(36, 10, f"{value}  ", fill=True, align="R")
        pdf.set_font("DejaVu", "", 10)
        pdf.ln()

    pdf.ln(4)

    # Totals table
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 7, "Resumen de inversión inicial (primer año)")
    pdf.ln(8)

    totals = [
        ("Desarrollo Landing Page", money(PRECIO_DESARROLLO), False),
        ("Hosting (1er año)", money(PRECIO_HOSTING), False),
        ("Dominio (1er año)", f"{money(PRECIO_DOMINIO_MIN)} – {money(PRECIO_DOMINIO_MAX)}", False),
        ("TOTAL INVERSIÓN INICIAL", f"{money(TOTAL_MIN)} – {money(TOTAL_MAX)}", True),
    ]

    pdf.set_fill_color(*LIGHT)
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(120, 8, "  Concepto", fill=True)
    pdf.cell(66, 8, "Valor (COP)", fill=True, align="R")
    pdf.ln()

    for label, value, is_total in totals:
        if is_total:
            pdf.set_fill_color(235, 245, 251)
            pdf.set_font("DejaVu", "B", 11)
            pdf.set_text_color(*SECONDARY)
        else:
            pdf.set_fill_color(255, 255, 255)
            pdf.set_font("DejaVu", "", 10)
            pdf.set_text_color(*TEXT)

        pdf.cell(120, 9, f"  {label}", fill=True)
        pdf.cell(66, 9, f"{value}  ", fill=True, align="R")
        pdf.ln()

    pdf.ln(6)

    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(
        0,
        5,
        f"Cálculo: {money(PRECIO_DESARROLLO)} + {money(PRECIO_HOSTING)} + dominio "
        f"({money(PRECIO_DOMINIO_MIN)} a {money(PRECIO_DOMINIO_MAX)}) = "
        f"{money(TOTAL_MIN)} a {money(TOTAL_MAX)} COP.",
    )
    pdf.ln(6)

    # Notes
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 7, "Condiciones y notas")
    pdf.ln(6)

    notes = [
        "* El costo del dominio varía entre $70.000 y $120.000 COP anuales, según disponibilidad y extensión del nombre elegido (.com, .com.co, etc.).",
        f"Renovación anual (a partir del 2.° año): hosting ({money(PRECIO_HOSTING)}) + dominio ({money(PRECIO_DOMINIO_MIN)} – {money(PRECIO_DOMINIO_MAX)}). El desarrollo es pago único.",
        "El desarrollo incluye una (1) ronda de ajustes menores posteriores a la entrega.",
        "Contenido (textos, fotos de proyectos y logo del cliente) suministrado por el contratante.",
        "Tiempo estimado de entrega: 5 a 10 días hábiles después de recibir el contenido.",
        "Forma de pago: 50% al iniciar, 50% contra entrega y publicación.",
        "Validez de esta cotización: 15 días calendario.",
    ]
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*TEXT)
    for note in notes:
        pdf.multi_cell(0, 5, f"• {note}")
        pdf.ln(1)

    pdf.ln(8)

    # Signature area
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(90, 6, "Elaborado por:")
    pdf.cell(0, 6, "Aprobado por el cliente:", align="R")
    pdf.ln(12)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*TEXT)
    pdf.cell(90, 6, "Jayson Tech")
    pdf.cell(0, 6, "Nombre: _________________________", align="R")
    pdf.ln(6)
    pdf.cell(90, 6, "https://jaysontech.com.co")
    pdf.cell(0, 6, "Firma: __________________________", align="R")

    pdf.output(OUTPUT)
    print(OUTPUT)
    print(f"Total mínimo: {money(TOTAL_MIN)}")
    print(f"Total máximo: {money(TOTAL_MAX)}")


if __name__ == "__main__":
    generar()
