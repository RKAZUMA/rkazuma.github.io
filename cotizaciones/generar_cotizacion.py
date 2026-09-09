#!/usr/bin/env python3
"""Genera cotización PDF Jayson Tech."""

from datetime import date
from fpdf import FPDF

LOGO = "/workspace/images/jaysontech_logo.png"
OUTPUT = "/workspace/cotizaciones/Cotizacion-Arquitectura-360-SAS-JaysonTech.pdf"
CLIENTE = "Arquitectura 360 S.A.S"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

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
    pdf.cell(95, 7, f"No. JT-2026-0909")
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
        (
            "Desarrollo Landing Page",
            "Diseño + desarrollo + formulario",
            money(350_000),
            False,
        ),
        (
            "Hosting anual",
            "Alojamiento web 12 meses",
            money(100_000),
            False,
        ),
        (
            "Dominio anual",
            "Registro .com / .com.co *",
            f"{money(70_000)} – {money(120_000)}",
            True,
        ),
    ]

    pdf.set_text_color(*TEXT)
    pdf.set_font("DejaVu", "", 10)
    for i, (concept, detail, value, variable) in enumerate(rows):
        fill = i % 2 == 1
        pdf.set_fill_color(*LIGHT if fill else (255, 255, 255))
        y0 = pdf.get_y()
        pdf.cell(95, 10, f"  {concept}", fill=True)
        pdf.cell(55, 10, detail, fill=True, align="C")
        pdf.set_font("DejaVu", "B" if not variable else "", 10)
        pdf.cell(36, 10, f"{value}  ", fill=True, align="R")
        pdf.set_font("DejaVu", "", 10)
        pdf.ln()

    pdf.ln(6)

    # Totals box
    pdf.set_fill_color(235, 245, 251)
    pdf.rect(105, pdf.get_y(), 96, 28, "F")
    y = pdf.get_y() + 5
    pdf.set_xy(110, y)
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(50, 6, "Inversión inicial estimada:")
    pdf.ln(7)
    pdf.set_x(110)
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.cell(50, 6, "Mínimo (dominio económico):")
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*SECONDARY)
    pdf.cell(41, 6, money(520_000), align="R")
    pdf.ln(7)
    pdf.set_x(110)
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.cell(50, 6, "Máximo (dominio premium):")
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*SECONDARY)
    pdf.cell(41, 6, money(570_000), align="R")
    pdf.ln(14)

    # Notes
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 7, "Condiciones y notas")
    pdf.ln(6)

    notes = [
        "* El costo del dominio varía entre $70.000 y $120.000 COP anuales, según disponibilidad y extensión del nombre elegido (.com, .com.co, etc.).",
        "Renovación anual: hosting ($100.000) + dominio ($70.000 – $120.000) deben renovarse cada año para mantener el sitio en línea.",
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


if __name__ == "__main__":
    generar()
