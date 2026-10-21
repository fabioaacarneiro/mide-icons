#!/usr/bin/env python3
"""Ícones próprios do mide, no estilo do WhiteSur (grade de 64 px, viewBox 16,933).

Cada ícone usa a mesma base dos ícones do WhiteSur (a sombra em camadas de
`base-shadow.svgpart`, tirada do tema, e o quadrado arredondado de 14,817 com
degradê) e um símbolo desenhado aqui. Os desenhos são do mide: não recriam ícones
da Apple.

Uso: python3 mide/build_icons.py  (grava em mide/icons/)
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "icons"
SHADOW = (HERE / "base-shadow.svgpart").read_text()

# Centro do quadrado.
CX, CY = 8.466, 8.458


def icon(name, top, bottom, defs, body, glossy=True):
    """Ícone completo: sombra do WhiteSur, quadrado com degradê `top` → `bottom` e o
    símbolo `body` por cima."""
    gloss = (
        '<rect width="14.817" height="14.817" x="1.058" y="1.05" fill="url(#gloss)" rx="3.44" ry="3.44"/>'
        if glossy
        else ""
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="64" height="64" viewBox="0 0 16.933 16.933">
<defs>
<linearGradient id="tile" x1="7.937" x2="7.937" y1="15.867" y2="1.05" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{bottom}"/><stop offset="1" stop-color="{top}"/></linearGradient>
<linearGradient id="gloss" x1="0" x2="0" y1="1.05" y2="15.867" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="soft" x="-.3" y="-.3" width="1.6" height="1.6" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation=".28"/></filter>
<filter id="glow" x="-.5" y="-.5" width="2" height="2" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation=".35"/></filter>
{defs}
</defs>
{SHADOW}
<rect width="14.817" height="14.817" x="1.058" y="1.05" fill="url(#tile)" rx="3.44" ry="3.44"/>
{gloss}
{body}
<rect width="14.617" height="14.617" x="1.158" y="1.15" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width=".1" rx="3.36" ry="3.36"/>
</svg>
"""
    (OUT / f"{name}.svg").write_text(svg)


def globe():
    """Navegador: um globo de vidro (no lugar da bússola do Safari)."""
    r = 5.05
    defs = f"""
<radialGradient id="sphere" cx="6.9" cy="6.3" r="7.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#d8efff"/><stop offset="1" stop-color="#8cc7ff"/></radialGradient>
<radialGradient id="land" cx="6.9" cy="6.3" r="7.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8fe6b2"/><stop offset=".6" stop-color="#3cc27f"/><stop offset="1" stop-color="#1c8f5a"/></radialGradient>
<clipPath id="ball"><circle cx="{CX}" cy="{CY}" r="{r}"/></clipPath>"""
    grid = "".join(
        f'<ellipse cx="{CX}" cy="{CY}" rx="{rx}" ry="{r}" fill="none" stroke="#1f7fe0" stroke-opacity=".38" stroke-width=".16"/>'
        for rx in (1.7, 3.5)
    )
    grid += f'<path d="M{CX} {CY - r}V{CY + r}" stroke="#1f7fe0" stroke-opacity=".38" stroke-width=".16"/>'
    for dy, w in ((0, r), (-2.45, 4.4), (2.45, 4.4)):
        grid += f'<path d="M{CX - w} {CY + dy}Q{CX} {CY + dy + 0.55} {CX + w} {CY + dy}" fill="none" stroke="#1f7fe0" stroke-opacity=".38" stroke-width=".16"/>'
    # Terras estilizadas (formas livres, não um mapa).
    land = (
        '<path fill="url(#land)" d="M5.1 5.2c.75-.55 1.75-.7 2.35-.3.45.3.3.85-.15 1.05-.55.25-.6.8-.1 1.05.65.3.95.85.65 1.35-.3.5-.15 1 .25 1.4.45.45.35 1.05-.25 1.2-.45.1-.6.6-.35 1.05.2.4-.1.8-.6.7-1.05-.25-1.85-1.35-2.15-2.6-.35-1.45-.25-3.05.35-3.9z"/>'
        '<path fill="url(#land)" d="M9.75 4.15c.95-.15 2.05.25 2.8.95.35.35.15.75-.3.75-.6 0-.95.4-.75.9.15.4.65.55 1.05.75.55.3.7.95.4 1.5-.35.65-.95 1.3-1.6 1.6-.45.2-.75-.15-.6-.55.2-.5 0-.95-.45-1.15-.55-.25-.75-.85-.4-1.3.3-.4.1-.85-.35-1-.55-.2-.55-1.3.1-1.45z"/>'
        '<path fill="url(#land)" d="M10.4 11.35c.5-.25 1.15-.15 1.45.2.25.3.05.65-.35.75-.45.1-.8.45-1.15.6-.45.2-.65-.2-.4-.55.15-.25.25-.8.45-1z"/>'
    )
    body = f"""
<circle cx="{CX}" cy="{CY + .45}" r="{r}" fill="#00306e" opacity=".45" filter="url(#soft)"/>
<circle cx="{CX}" cy="{CY}" r="{r}" fill="url(#sphere)"/>
<g clip-path="url(#ball)">{land}{grid}</g>
<circle cx="{CX}" cy="{CY}" r="{r - .06}" fill="none" stroke="#0d5fc0" stroke-opacity=".35" stroke-width=".14"/>
<ellipse cx="6.9" cy="5.6" rx="2.5" ry="1.45" fill="#fff" opacity=".55" filter="url(#soft)" transform="rotate(-25 6.9 5.6)"/>"""
    icon("mide-web-browser", "#52c5ff", "#1262c4", defs, body)


def store():
    """Loja de apps: uma sacola (no lugar do "A" da App Store)."""
    defs = """
<linearGradient id="bag" x1="0" x2="0" y1="6" y2="13.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#dde8fb"/></linearGradient>
<linearGradient id="band" x1="0" x2="0" y1="6" y2="7.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#c9daf6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>"""
    bag = "M4.55 6.25h7.83c.3 0 .55.23.57.53l.5 5.95c.05.62-.44 1.15-1.06 1.15H4.54c-.62 0-1.11-.53-1.06-1.15l.5-5.95c.02-.3.27-.53.57-.53z"
    body = f"""
<path d="{bag}" fill="#003a8c" opacity=".45" filter="url(#soft)" transform="translate(0 .4)"/>
<path d="{bag}" fill="url(#bag)"/>
<path d="M4.55 6.25h7.83c.3 0 .55.23.57.53l.1 1.1H3.88l.1-1.1c.02-.3.27-.53.57-.53z" fill="url(#band)"/>
<path d="M6.35 7.4V5.5a2.12 2.12 0 0 1 4.24 0v1.9" fill="none" stroke="#fff" stroke-width=".62" stroke-linecap="round"/>
<path d="M6.35 7.4V5.5a2.12 2.12 0 0 1 4.24 0v1.9" fill="none" stroke="#7aa7e6" stroke-opacity=".55" stroke-width=".18" stroke-linecap="round" transform="translate(0 .2)"/>
<circle cx="6.35" cy="7.45" r=".32" fill="#9db9e4"/><circle cx="10.59" cy="7.45" r=".32" fill="#9db9e4"/>
<path d="M8.466 9.2v2.9M7.06 10.95l1.406 1.4 1.406-1.4" fill="none" stroke="#1d74f0" stroke-width=".5" stroke-linecap="round" stroke-linejoin="round"/>"""
    icon("mide-software-store", "#17b7f1", "#1763e1", defs, body)


def terminal():
    """Terminal do mide: tela escura com o prompt ❯ e o cursor em bloco."""
    defs = """
<linearGradient id="screen" x1="0" x2="0" y1="2.4" y2="14.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#262a33"/><stop offset="1" stop-color="#0e1014"/></linearGradient>"""
    green = "#4ee6a5"
    prompt = f'<path d="M4.3 9.05l1.75 1.35-1.75 1.35" fill="none" stroke="{green}" stroke-width=".55" stroke-linecap="round" stroke-linejoin="round"/>'
    cursor = f'<rect x="6.85" y="9.55" width=".85" height="1.75" rx=".12" fill="{green}"/>'
    lines = "".join(
        f'<rect x="4.3" y="{y}" width="{w}" height=".42" rx=".21" fill="#c9d1dc" opacity="{o}"/>'
        for y, w, o in ((4.35, 6.2, ".5"), (5.6, 4.1, ".35"), (6.85, 7.3, ".25"))
    )
    body = f"""
<rect x="2.25" y="2.4" width="12.43" height="12.2" rx="2.25" fill="url(#screen)" stroke="#000" stroke-opacity=".45" stroke-width=".12"/>
<path d="M4.5 2.46h7.93" stroke="#fff" stroke-opacity=".14" stroke-width=".1" stroke-linecap="round"/>
{lines}
<g filter="url(#glow)" opacity=".75">{prompt}{cursor}</g>
{prompt}{cursor}"""
    icon("mide-terminal", "#5a606c", "#1d2026", defs, body)


def text_editor():
    """Editor de texto do mide: folha com linhas e o cursor de texto."""
    defs = """
<linearGradient id="page" x1="0" x2="0" y1="2.3" y2="14.7" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#f1f3f7"/></linearGradient>
<linearGradient id="head" x1="3.8" x2="13.1" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#7b6cff"/><stop offset="1" stop-color="#4c8dff"/></linearGradient>
<linearGradient id="fold" x1="11.4" x2="12.9" y1="2.4" y2="3.9" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#e6e9ef"/><stop offset="1" stop-color="#c3c9d4"/></linearGradient>"""
    page = "M4.45 2.35h6.75l2.25 2.25v9.45c0 .37-.3.66-.66.66H4.45a.66.66 0 0 1-.66-.66V3.01c0-.37.3-.66.66-.66z"
    lines = "".join(
        f'<rect x="5.0" y="{y}" width="{w}" height=".42" rx=".21" fill="{c}"/>'
        for y, w, c in (
            (6.15, 6.6, "#c7cdd7"),
            (7.35, 5.2, "#c7cdd7"),
            (8.55, 6.2, "#c7cdd7"),
            (9.75, 3.4, "#7b6cff"),
            (10.95, 5.8, "#c7cdd7"),
            (12.15, 4.3, "#c7cdd7"),
        )
    )
    body = f"""
<path d="{page}" fill="#5b6478" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{page}" fill="url(#page)"/>
<path d="M4.45 2.35h6.75v1.6c0 .36.29.65.65.65h1.6v-.05H3.79V3.01c0-.37.3-.66.66-.66z" fill="url(#head)"/>
<path d="M11.2 2.35v1.6c0 .36.29.65.65.65h1.6z" fill="url(#fold)"/>
{lines}
<path d="M8.75 9.35v1.25M8.45 9.35h.6M8.45 10.6h.6" stroke="#1f6feb" stroke-width=".22" stroke-linecap="round"/>"""
    icon("mide-text-editor", "#fdfdfe", "#dfe3ea", defs, body)


def settings():
    """Configurações do mide: três controles deslizantes (no lugar da engrenagem)."""
    colors = (("#3ea8ff", "#1677e6"), ("#3fd98f", "#14a865"), ("#ffae4a", "#f07a1a"))
    defs = """
<radialGradient id="knob" cx="0" cy="0" r="1" gradientUnits="objectBoundingBox" fx=".35" fy=".3"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#d5dae3"/></radialGradient>
<linearGradient id="track" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#0d1118"/><stop offset="1" stop-color="#2a313d"/></linearGradient>"""
    for i, (a, b) in enumerate(colors):
        defs += f'<linearGradient id="fill{i}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
    body = ""
    for i, (y, knob) in enumerate(((5.0, 10.6), (8.46, 6.2), (11.92, 9.0))):
        body += f"""
<rect x="3.4" y="{y - .42}" width="10.13" height=".84" rx=".42" fill="url(#track)"/>
<rect x="3.4" y="{y - .42}" width="{knob - 3.4}" height=".84" rx=".42" fill="url(#fill{i})"/>
<circle cx="{knob}" cy="{y + .2}" r="1.2" fill="#000" opacity=".45" filter="url(#soft)"/>
<circle cx="{knob}" cy="{y}" r="1.2" fill="url(#knob)"/>
<circle cx="{knob}" cy="{y}" r="1.15" fill="none" stroke="#000" stroke-opacity=".18" stroke-width=".08"/>"""
    icon("mide-settings", "#66758b", "#262e3a", defs, body)


def screenshot():
    """Captura de tela do mide: seleção tracejada com alças e a mira."""
    defs = """
<linearGradient id="sel" x1="0" x2="0" y1="3.6" y2="11.9" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#5cc2ff" stop-opacity=".35"/><stop offset="1" stop-color="#3a7bff" stop-opacity=".18"/></linearGradient>"""
    x0, y0, x1, y1 = 3.5, 3.7, 12.1, 11.4
    handles = "".join(
        f'<rect x="{x - .42}" y="{y - .42}" width=".84" height=".84" rx=".16" fill="#fff"/>'
        for x in (x0, x1)
        for y in (y0, y1)
    )
    body = f"""
<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="url(#sel)"/>
<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="none" stroke="#fff" stroke-width=".26" stroke-dasharray=".62 .42"/>
{handles}
<g transform="translate(12.35 12.35)">
<circle r="1.85" fill="#000" opacity=".4" filter="url(#soft)" transform="translate(0 .2)"/>
<circle r="1.75" fill="#fff"/>
<circle r="1.12" fill="#ff5a5f"/>
<circle r=".42" fill="#fff"/>
</g>"""
    icon("mide-screenshot", "#4a5a7d", "#1b2236", defs, body)


def files():
    """Arquivos do mide: a pasta azul do próprio tema sobre um quadrado claro (no
    lugar do rosto do Finder)."""
    import re
    folder = (HERE.parent / "src/places/scalable/folder.svg").read_text()
    inner = folder[folder.index(">", folder.index("<svg")) + 1 : folder.rindex("</svg>")]
    # Identificadores próprios, para não colidir com os do quadrado.
    inner = re.sub(r'id="([^"]+)"', r'id="f-\1"', inner)
    inner = re.sub(r'url\(#([^)]+)\)', r'url(#f-\1)', inner)
    inner = re.sub(r'xlink:href="#([^"]+)"', r'xlink:href="#f-\1"', inner)
    body = f"""
<svg x="2.0" y="2.35" width="12.93" height="12.93" viewBox="0 0 16.933 16.933">{inner}</svg>"""
    icon("mide-file-manager", "#fbfcfd", "#d9dfe7", "", body)


def default_app():
    """App sem ícone próprio: quatro blocos arredondados (no lugar da engrenagem)."""
    defs = """
<linearGradient id="blk" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e3e8f0"/></linearGradient>"""
    body = ""
    for x in (4.15, 8.85):
        for y in (4.15, 8.85):
            body += f'<rect x="{x}" y="{y + .25}" width="3.95" height="3.95" rx="1.1" fill="#1a2433" opacity=".35" filter="url(#soft)"/>'
            body += f'<rect x="{x}" y="{y}" width="3.95" height="3.95" rx="1.1" fill="url(#blk)"/>'
    icon("mide-default-app", "#9aa6b8", "#5b6578", defs, body)


# ---- Etapa 2: apps que tinham recriação do ícone da Apple ----

def calendar():
    """Calendário: folha com argolas, cabeçalho colorido e a grade dos dias."""
    defs = """
<linearGradient id="sheet" x1="0" x2="0" y1="3" y2="14.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#eef1f6"/></linearGradient>
<linearGradient id="cal-head" x1="3" x2="13.9" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff7a59"/><stop offset="1" stop-color="#ff4f7b"/></linearGradient>
<linearGradient id="ring" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5b6170"/><stop offset="1" stop-color="#2b2f38"/></linearGradient>"""
    sheet = "M3.85 3.6h9.23c.47 0 .85.38.85.85v8.95c0 .47-.38.85-.85.85H3.85a.85.85 0 0 1-.85-.85V4.45c0-.47.38-.85.85-.85z"
    days = ""
    for row in range(4):
        for col in range(5):
            x = 4.45 + col * 1.85
            y = 7.55 + row * 1.5
            if (row, col) == (1, 3):
                days += f'<circle cx="{x + .45}" cy="{y + .4}" r=".72" fill="url(#cal-head)"/><circle cx="{x + .45}" cy="{y + .4}" r=".22" fill="#fff"/>'
            else:
                days += f'<rect x="{x}" y="{y}" width=".9" height=".8" rx=".22" fill="#c4cad5"/>'
    body = f"""
<path d="{sheet}" fill="#5b6478" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{sheet}" fill="url(#sheet)"/>
<path d="M3.85 3.6h9.23c.47 0 .85.38.85.85v1.75H3V4.45c0-.47.38-.85.85-.85z" fill="url(#cal-head)"/>
<rect x="4.4" y="5.2" width="3.6" height=".42" rx=".21" fill="#fff" opacity=".85"/>
{days}
<rect x="5.15" y="2.45" width=".62" height="2.1" rx=".31" fill="url(#ring)"/>
<rect x="11.16" y="2.45" width=".62" height="2.1" rx=".31" fill="url(#ring)"/>"""
    icon("mide-calendar", "#fdfdfe", "#dfe3ea", defs, body)


def clock():
    """Relógio: mostrador claro sobre o quadrado azul-esverdeado."""
    defs = """
<radialGradient id="face" cx="7.6" cy="7.2" r="6.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e6ebf2"/></radialGradient>"""
    import math
    ticks = ""
    for i in range(12):
        a = math.radians(i * 30)
        r1, r2 = (4.15, 4.85) if i % 3 == 0 else (4.45, 4.85)
        w = ".32" if i % 3 == 0 else ".16"
        x1, y1 = CX + r1 * math.sin(a), CY - r1 * math.cos(a)
        x2, y2 = CX + r2 * math.sin(a), CY - r2 * math.cos(a)
        ticks += f'<path d="M{x1:.3f} {y1:.3f}L{x2:.3f} {y2:.3f}" stroke="#3b4252" stroke-width="{w}" stroke-linecap="round"/>'
    def hand(deg, length, width, color):
        a = math.radians(deg)
        x, y = CX + length * math.sin(a), CY - length * math.cos(a)
        bx, by = CX - .7 * math.sin(a), CY + .7 * math.cos(a)
        return f'<path d="M{bx:.3f} {by:.3f}L{x:.3f} {y:.3f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
    body = f"""
<circle cx="{CX}" cy="{CY + .4}" r="5.55" fill="#003a4a" opacity=".45" filter="url(#soft)"/>
<circle cx="{CX}" cy="{CY}" r="5.55" fill="url(#face)"/>
<circle cx="{CX}" cy="{CY}" r="5.5" fill="none" stroke="#000" stroke-opacity=".12" stroke-width=".1"/>
{ticks}
{hand(310, 2.6, ".46", "#1f2633")}
{hand(60, 3.7, ".34", "#1f2633")}
{hand(170, 4.1, ".14", "#ff6a3d")}
<circle cx="{CX}" cy="{CY}" r=".42" fill="#1f2633"/><circle cx="{CX}" cy="{CY}" r=".18" fill="#ff6a3d"/>"""
    icon("mide-clock", "#3fd3c6", "#1677c9", defs, body)


def contacts():
    """Contatos: cartão de visita com o avatar e as linhas de dados."""
    defs = """
<linearGradient id="card" x1="0" x2="0" y1="4" y2="13" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#eef1f6"/></linearGradient>
<linearGradient id="avatar" x1="3.9" x2="7.6" y1="5.6" y2="10.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8fb6ff"/><stop offset="1" stop-color="#5a7bf0"/></linearGradient>"""
    card = "M3.6 4.25h9.73c.5 0 .9.4.9.9v6.7c0 .5-.4.9-.9.9H3.6a.9.9 0 0 1-.9-.9v-6.7c0-.5.4-.9.9-.9z"
    body = f"""
<path d="{card}" fill="#6a2b10" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{card}" fill="url(#card)"/>
<circle cx="5.85" cy="8.2" r="2.05" fill="url(#avatar)"/>
<circle cx="5.85" cy="7.55" r=".78" fill="#fff" opacity=".95"/>
<path d="M4.45 9.85c.3-.85.9-1.25 1.4-1.25s1.1.4 1.4 1.25a2.05 2.05 0 0 1-2.8 0z" fill="#fff" opacity=".95"/>
<rect x="8.6" y="6.6" width="4.4" height=".5" rx=".25" fill="#3b4252"/>
<rect x="8.6" y="7.75" width="3.3" height=".42" rx=".21" fill="#b9c0cc"/>
<rect x="8.6" y="8.8" width="3.9" height=".42" rx=".21" fill="#b9c0cc"/>
<rect x="8.6" y="9.85" width="2.4" height=".42" rx=".21" fill="#ff8a5c"/>"""
    icon("mide-contacts", "#ffbf6b", "#ff6f4f", defs, body)


def music():
    """Música: disco de vinil com selo colorido (no lugar da nota rosa)."""
    defs = """
<radialGradient id="vinyl" cx="8.466" cy="8.458" r="5.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#3a3d46"/><stop offset=".55" stop-color="#16181d"/><stop offset="1" stop-color="#0b0c0f"/></radialGradient>
<linearGradient id="label" x1="6.9" x2="10" y1="6.9" y2="10" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="#ff4f7b"/></linearGradient>
<linearGradient id="sheen" x1="3.5" x2="13.4" y1="3.5" y2="13.4" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".45" stop-color="#fff" stop-opacity=".18"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></linearGradient>"""
    grooves = "".join(f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="#fff" stroke-opacity=".07" stroke-width=".06"/>' for r in (2.4, 2.9, 3.4, 3.9, 4.4, 4.9))
    body = f"""
<circle cx="{CX}" cy="{CY + .4}" r="5.4" fill="#000" opacity=".5" filter="url(#soft)"/>
<circle cx="{CX}" cy="{CY}" r="5.4" fill="url(#vinyl)"/>
{grooves}
<circle cx="{CX}" cy="{CY}" r="5.4" fill="url(#sheen)"/>
<circle cx="{CX}" cy="{CY}" r="1.85" fill="url(#label)"/>
<circle cx="{CX}" cy="{CY}" r=".3" fill="#0b0c0f"/>
<path d="M12.6 3.4l-1.9 3.3" stroke="#d7dbe2" stroke-width=".38" stroke-linecap="round"/>
<circle cx="12.7" cy="3.3" r=".62" fill="#eef1f6"/>"""
    icon("mide-music", "#8a5cff", "#3a2bb8", defs, body)


def photos():
    """Fotos: três fotos em leque, com paisagens em degradê (no lugar da flor)."""
    defs = """
<linearGradient id="sky1" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7cc8ff"/><stop offset="1" stop-color="#d9f0ff"/></linearGradient>
<linearGradient id="hill1" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4fc27f"/><stop offset="1" stop-color="#1f8f57"/></linearGradient>
<linearGradient id="sky2" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ff9a6b"/><stop offset="1" stop-color="#ffd59a"/></linearGradient>
<linearGradient id="hill2" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7a5cff"/><stop offset="1" stop-color="#4a33c9"/></linearGradient>"""
    def photo(angle, dx, sky, hill, sun):
        return f"""<g transform="rotate({angle} 8.466 9) translate({dx} 0)">
<rect x="4.2" y="4.6" width="8.53" height="7.2" rx=".55" fill="#2b2f38" opacity=".35" filter="url(#soft)" transform="translate(0 .3)"/>
<rect x="4.2" y="4.6" width="8.53" height="7.2" rx=".55" fill="#fff"/>
<rect x="4.75" y="5.15" width="7.43" height="5.5" rx=".25" fill="url(#{sky})"/>
<circle cx="10.6" cy="6.5" r=".7" fill="{sun}"/>
<path d="M4.75 9.4c1.1-1.1 2.2-1.65 3.3-.9.8.55 1.45.2 2.2-.35.8-.6 1.4-.3 1.93.15v2.1a.25.25 0 0 1-.25.25H5a.25.25 0 0 1-.25-.25z" fill="url(#{hill})"/>
</g>"""
    body = photo(-12, -.4, "sky2", "hill2", "#fff3c4") + photo(8, .3, "sky1", "hill1", "#fff")
    icon("mide-photos", "#ffffff", "#e3e8f0", defs, body)


def system_monitor():
    """Monitor do sistema: barras de uso e a linha de carga (no lugar do ECG verde)."""
    defs = """
<linearGradient id="panel" x1="0" x2="0" y1="3" y2="14" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#262a33"/><stop offset="1" stop-color="#14161b"/></linearGradient>
<linearGradient id="bar" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5ec8ff"/><stop offset="1" stop-color="#3a6bff"/></linearGradient>
<linearGradient id="line" x1="3" x2="14" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="#ff4f7b"/></linearGradient>"""
    bars = ""
    for i, h in enumerate((3.2, 5.4, 2.4, 6.6, 4.4)):
        x = 4.0 + i * 1.85
        bars += f'<rect x="{x}" y="{12.6 - h}" width="1.2" height="{h}" rx=".3" fill="url(#bar)" opacity=".9"/>'
    body = f"""
<rect x="2.6" y="2.75" width="11.73" height="11.43" rx="1.9" fill="url(#panel)" stroke="#000" stroke-opacity=".4" stroke-width=".1"/>
<path d="M3.4 6h10.1M3.4 8.4h10.1M3.4 10.8h10.1" stroke="#fff" stroke-opacity=".07" stroke-width=".08"/>
{bars}
<path d="M3.6 9.6l2-1.9 1.6 1.2 2.1-3.1 1.8 1.6 2.4-2.6" fill="none" stroke="url(#line)" stroke-width=".42" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="13.5" cy="4.8" r=".45" fill="#ff4f7b"/>"""
    icon("mide-system-monitor", "#eef1f6", "#c9d0db", defs, body)


def maps():
    """Mapas: mapa dobrado em três partes com o alfinete (no lugar das ruas e da bússola)."""
    defs = """
<linearGradient id="m1" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#bff0d0"/><stop offset="1" stop-color="#8fd9ad"/></linearGradient>
<linearGradient id="m2" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#9fe3bd"/><stop offset="1" stop-color="#6cc794"/></linearGradient>
<linearGradient id="pin" x1="0" x2="0" y1="3" y2="9" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff7a6b"/><stop offset="1" stop-color="#e5304f"/></linearGradient>"""
    body = """
<path d="M3 4.9l3.4-1.2 4.1 1.2 3.4-1.2v8.6l-3.4 1.2-4.1-1.2L3 13.5z" fill="#0b4f3a" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="M3 4.9l3.4-1.2v8.6L3 13.5z" fill="url(#m1)"/>
<path d="M6.4 3.7l4.1 1.2v8.6l-4.1-1.2z" fill="url(#m2)"/>
<path d="M10.5 4.9l3.4-1.2v8.6l-3.4 1.2z" fill="url(#m1)"/>
<path d="M3.6 10.6c1.4-.6 2.6.4 3.9-.3 1.3-.7 2.2-1.9 3.6-1.5 1.1.3 1.6-.2 2.2-.7" fill="none" stroke="#fff" stroke-width=".42" stroke-linecap="round" opacity=".9"/>
<path d="M3.6 10.6c1.4-.6 2.6.4 3.9-.3 1.3-.7 2.2-1.9 3.6-1.5 1.1.3 1.6-.2 2.2-.7" fill="none" stroke="#f4b740" stroke-width=".2" stroke-linecap="round"/>
<path d="M9.6 9.3c-.25-1.1-1.85-2.2-1.85-3.6a1.85 1.85 0 0 1 3.7 0c0 1.4-1.6 2.5-1.85 3.6z" fill="#000" opacity=".35" filter="url(#soft)" transform="translate(0 .25)"/>
<path d="M9.6 9.3c-.25-1.1-1.85-2.2-1.85-3.6a1.85 1.85 0 0 1 3.7 0c0 1.4-1.6 2.5-1.85 3.6z" fill="url(#pin)"/>
<circle cx="9.6" cy="5.7" r=".7" fill="#fff"/>"""
    icon("mide-maps", "#4fd1c5", "#1c8f8a", defs, body)


def reminders():
    """Lembretes: lista com caixas marcadas (no lugar dos pontos coloridos)."""
    defs = """
<linearGradient id="list" x1="0" x2="0" y1="3" y2="14" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#eef1f6"/></linearGradient>
<linearGradient id="tick" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4fe08f"/><stop offset="1" stop-color="#17a85f"/></linearGradient>"""
    card = "M4.1 3h8.73c.58 0 1.05.47 1.05 1.05v8.85c0 .58-.47 1.05-1.05 1.05H4.1a1.05 1.05 0 0 1-1.05-1.05V4.05C3.05 3.47 3.52 3 4.1 3z"
    rows = ""
    for i, done in enumerate((True, True, False)):
        y = 4.75 + i * 2.75
        if done:
            rows += f'<rect x="4.2" y="{y}" width="1.75" height="1.75" rx=".45" fill="url(#tick)"/><path d="M4.65 {y + .9}l.45.45.85-.95" fill="none" stroke="#fff" stroke-width=".3" stroke-linecap="round" stroke-linejoin="round"/>'
            rows += f'<rect x="6.75" y="{y + .67}" width="{4.6 - i * 1.1}" height=".42" rx=".21" fill="#b9c0cc"/>'
        else:
            rows += f'<rect x="4.25" y="{y + .05}" width="1.65" height="1.65" rx=".42" fill="none" stroke="#9aa3b2" stroke-width=".18"/>'
            rows += f'<rect x="6.75" y="{y + .67}" width="5.2" height=".42" rx=".21" fill="#3b4252"/>'
    body = f"""
<path d="{card}" fill="#3a2b7a" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{card}" fill="url(#list)"/>
{rows}"""
    icon("mide-reminders", "#a78bff", "#6a4cf0", defs, body)


def help_icon():
    """Ajuda: balão de conversa com o ponto de interrogação."""
    defs = """
<linearGradient id="bubble" x1="0" x2="0" y1="3" y2="13" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e3ecfb"/></linearGradient>"""
    bubble = "M8.466 3.1c3.05 0 5.4 2 5.4 4.55S11.52 12.2 8.466 12.2c-.55 0-1.07-.06-1.57-.18L4.7 13.4l.55-2.15C3.92 10.43 3.07 9.13 3.07 7.65 3.07 5.1 5.42 3.1 8.466 3.1z"
    body = f"""
<path d="{bubble}" fill="#003a8c" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{bubble}" fill="url(#bubble)"/>
<path d="M7.15 6.4c.1-.8.65-1.3 1.4-1.3.8 0 1.35.5 1.35 1.15 0 .55-.3.85-.8 1.15-.45.27-.6.5-.6.95v.25" fill="none" stroke="#1d74f0" stroke-width=".55" stroke-linecap="round"/>
<circle cx="8.5" cy="10.05" r=".38" fill="#1d74f0"/>"""
    icon("mide-help", "#5ec8ff", "#1d6fe8", defs, body)


def dictionary():
    """Dicionário: livro aberto com a fita marcadora (no lugar do livro vermelho "Aa")."""
    defs = """
<linearGradient id="pg" x1="0" x2="0" y1="4" y2="13" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#ece8df"/></linearGradient>
<linearGradient id="cover" x1="0" x2="0" y1="4" y2="13.5" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2f5d8c"/><stop offset="1" stop-color="#1c3a5c"/></linearGradient>"""
    body = """
<path d="M2.6 5.2c2-.6 4-.5 5.866.6 1.866-1.1 3.866-1.2 5.866-.6v7.6c-2-.6-4-.5-5.866.6-1.866-1.1-3.866-1.2-5.866-.6z" fill="#000" opacity=".35" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="M2.6 5.6c2-.6 4-.5 5.866.6 1.866-1.1 3.866-1.2 5.866-.6v7.6c-2-.6-4-.5-5.866.6-1.866-1.1-3.866-1.2-5.866-.6z" fill="url(#cover)"/>
<path d="M3.1 4.8c1.85-.55 3.7-.45 5.366.55v7.6c-1.666-1-3.516-1.1-5.366-.55z" fill="url(#pg)"/>
<path d="M13.832 4.8c-1.85-.55-3.7-.45-5.366.55v7.6c1.666-1 3.516-1.1 5.366-.55z" fill="url(#pg)"/>
<path d="M8.466 5.35v7.6" stroke="#c9c2b3" stroke-width=".12"/>
""" + "".join(
        f'<path d="M{x0} {y}c1.2-.3 2.3-.25 3.4.2" fill="none" stroke="#b5b0a6" stroke-width=".2" stroke-linecap="round"/>'
        for x0 in (3.75,)
        for y in (6.6, 7.6, 8.6, 9.6, 10.6)
    ) + "".join(
        f'<path d="M{x0} {y}c1.1-.45 2.2-.5 3.4-.2" fill="none" stroke="#b5b0a6" stroke-width=".2" stroke-linecap="round"/>'
        for x0 in (9.3,)
        for y in (6.8, 7.8, 8.8, 9.8)
    ) + """
<path d="M11.7 4.55v3.4l.55-.45.55.45v-3.5c-.37-.04-.74-.02-1.1.1z" fill="#ff5a5f"/>"""
    icon("mide-dictionary", "#6fd3c9", "#1f8f9e", defs, body)


def podcast():
    """Podcasts: microfone de estúdio (no lugar das ondas roxas)."""
    defs = """
<linearGradient id="mic" x1="6.6" x2="10.4" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#e9edf3"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="#c7ced9"/></linearGradient>"""
    grille = "".join(f'<path d="M6.95 {y}h3.03" stroke="#8a93a3" stroke-width=".12" opacity=".7"/>' for y in (4.9, 5.55, 6.2, 6.85, 7.5, 8.15))
    body = f"""
<rect x="6.55" y="3.2" width="3.83" height="6.6" rx="1.9" fill="#3a0d0d" opacity=".45" filter="url(#soft)" transform="translate(0 .35)"/>
<rect x="6.55" y="3.2" width="3.83" height="6.6" rx="1.9" fill="url(#mic)"/>
{grille}
<path d="M5.1 8.2a3.37 3.37 0 0 0 6.73 0" fill="none" stroke="#fff" stroke-width=".5" stroke-linecap="round"/>
<path d="M8.466 11.55v1.6M6.6 13.4h3.73" stroke="#fff" stroke-width=".5" stroke-linecap="round"/>"""
    icon("mide-podcast", "#ff9a5a", "#e8364f", defs, body)


def accessibility():
    """Acessibilidade: o símbolo universal dentro do anel."""
    body = """
<circle cx="8.466" cy="8.458" r="5.1" fill="none" stroke="#fff" stroke-width=".55" opacity=".95"/>
<circle cx="8.466" cy="5.35" r=".85" fill="#fff"/>
<path d="M5.35 6.75c1.05.3 2.05.45 3.116.45s2.066-.15 3.116-.45" fill="none" stroke="#fff" stroke-width=".62" stroke-linecap="round"/>
<path d="M8.466 7.2v2.2M8.466 9.4l-1.35 2.8M8.466 9.4l1.35 2.8" fill="none" stroke="#fff" stroke-width=".62" stroke-linecap="round" stroke-linejoin="round"/>"""
    icon("mide-accessibility", "#4fe08f", "#139a6b", "", body)


def camera():
    """Câmera: corpo de câmera com lente de vidro (no lugar da Captura de Imagem)."""
    defs = """
<linearGradient id="body" x1="0" x2="0" y1="5" y2="13" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f4f6f9"/><stop offset="1" stop-color="#c9d0da"/></linearGradient>
<radialGradient id="lens" cx="7.9" cy="8.6" r="3" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#5b7bd6"/><stop offset=".45" stop-color="#1b2a55"/><stop offset="1" stop-color="#05070d"/></radialGradient>"""
    cam = "M4.1 5.55h1.6l.7-1.05h4.13l.7 1.05h1.6c.6 0 1.1.5 1.1 1.1v5.65c0 .6-.5 1.1-1.1 1.1H4.1c-.6 0-1.1-.5-1.1-1.1V6.65c0-.6.5-1.1 1.1-1.1z"
    body = f"""
<path d="{cam}" fill="#000" opacity=".45" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{cam}" fill="url(#body)"/>
<circle cx="8.466" cy="9.45" r="2.95" fill="#2b2f38"/>
<circle cx="8.466" cy="9.45" r="2.55" fill="#8a93a3"/>
<circle cx="8.466" cy="9.45" r="2.25" fill="url(#lens)"/>
<ellipse cx="7.75" cy="8.6" rx=".75" ry=".45" fill="#fff" opacity=".65" transform="rotate(-30 7.75 8.6)"/>
<circle cx="12.1" cy="7.05" r=".42" fill="#ff8a3d"/>"""
    icon("mide-camera", "#4a5568", "#1a202c", defs, body)


def cleaner():
    """Limpeza do sistema: vassoura com brilhos (no lugar do estetoscópio)."""
    defs = """
<linearGradient id="handle" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#d9a066"/><stop offset="1" stop-color="#a86a32"/></linearGradient>
<linearGradient id="bristle" x1="0" x2="0" y1="9" y2="13.8" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffd36b"/><stop offset="1" stop-color="#f29a1f"/></linearGradient>"""
    def spark(x, y, k):
        return f'<path d="M{x} {y - k}c.12.75.25.88 1 {k}c-.75.12-.88.25-1 1c-.12-.75-.25-.88-1-1c.75-.12.88-.25 1-{k}z" fill="#fff" transform="translate(0 0)"/>'
    body = f"""
<g transform="rotate(-35 8.466 8.458)">
<rect x="8.1" y="2.2" width=".75" height="7.4" rx=".37" fill="url(#handle)"/>
<rect x="7.35" y="9.1" width="2.25" height=".9" rx=".25" fill="#5b6478"/>
<path d="M6.9 9.95h3.15l.85 3.75c.06.28-.15.55-.44.55H6.49c-.29 0-.5-.27-.44-.55z" fill="#000" opacity=".3" filter="url(#soft)" transform="translate(0 .3)"/>
<path d="M6.9 9.95h3.15l.85 3.75c.06.28-.15.55-.44.55H6.49c-.29 0-.5-.27-.44-.55z" fill="url(#bristle)"/>
<path d="M7.6 10.4l-.25 3.4M8.47 10.4v3.5M9.35 10.4l.25 3.4" stroke="#c97a14" stroke-width=".14" opacity=".7"/>
</g>
{spark(4.2, 5.0, 1)}{spark(12.6, 9.8, 1)}{spark(5.2, 11.6, .7)}"""
    icon("mide-cleaner", "#5ee0c8", "#169c9a", defs, body)


def mail():
    """Mail: envelope com a aba e o selo de mensagem nova (no lugar do "@")."""
    defs = """
<linearGradient id="env" x1="0" x2="0" y1="4.6" y2="12.8" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e3ecfb"/></linearGradient>
<linearGradient id="flap" x1="0" x2="0" y1="4.6" y2="9.3" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f3f7ff"/><stop offset="1" stop-color="#cfdcf3"/></linearGradient>"""
    env = "M3.6 4.6h9.73c.5 0 .9.4.9.9v6.4c0 .5-.4.9-.9.9H3.6a.9.9 0 0 1-.9-.9V5.5c0-.5.4-.9.9-.9z"
    body = f"""
<path d="{env}" fill="#003a8c" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{env}" fill="url(#env)"/>
<path d="M2.85 12.3l4.4-3.7M14.08 12.3l-4.4-3.7" stroke="#b8c8e6" stroke-width=".18"/>
<path d="M2.9 5.15l4.85 4.1c.42.35 1.01.35 1.43 0l4.85-4.1c-.15-.33-.48-.55-.86-.55H3.76c-.38 0-.71.22-.86.55z" fill="url(#flap)"/>
<circle cx="13.1" cy="4.75" r="1.35" fill="#ff5a5f" stroke="#fff" stroke-width=".22"/>"""
    icon("mide-mail", "#5ec8ff", "#1d6fe8", defs, body)


def image_viewer():
    """Visualizador de imagens: foto em moldura com o selo de ampliar."""
    defs = """
<linearGradient id="vsky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7cc8ff"/><stop offset="1" stop-color="#d9f0ff"/></linearGradient>
<linearGradient id="vhill" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4fc27f"/><stop offset="1" stop-color="#1f8f57"/></linearGradient>
<radialGradient id="glass" cx="11" cy="10.4" r="2" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#cfe6ff" stop-opacity=".2"/></radialGradient>"""
    body = """
<rect x="2.9" y="3.4" width="10.4" height="8.6" rx=".6" fill="#000" opacity=".3" filter="url(#soft)" transform="translate(0 .35)"/>
<rect x="2.9" y="3.4" width="10.4" height="8.6" rx=".6" fill="#fff"/>
<rect x="3.55" y="4.05" width="9.1" height="7.3" rx=".3" fill="url(#vsky)"/>
<circle cx="10.9" cy="5.6" r=".85" fill="#fff6c9"/>
<path d="M3.55 9.6c1.4-1.5 2.7-2.2 4-1.2.95.75 1.7.3 2.55-.4.95-.75 1.8-.35 2.55.3v2.75a.3.3 0 0 1-.3.3H3.85a.3.3 0 0 1-.3-.3z" fill="url(#vhill)"/>
<circle cx="12.2" cy="11.8" r="1.75" fill="#000" opacity=".35" filter="url(#soft)" transform="translate(0 .25)"/>
<circle cx="12.2" cy="11.8" r="1.75" fill="#1d74f0" stroke="#fff" stroke-width=".25"/>
<path d="M11.35 12.65l1.7-1.7M12.05 10.95h1v1M11.35 11.65v1h1" fill="none" stroke="#fff" stroke-width=".3" stroke-linecap="round" stroke-linejoin="round"/>"""
    icon("mide-image-viewer", "#ffffff", "#dfe5ee", defs, body)


def disks():
    """Discos: unidade com a barra de uso colorida e a luz (sem o estetoscópio)."""
    defs = """
<linearGradient id="drive" x1="0" x2="0" y1="5" y2="12" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f2f4f7"/><stop offset="1" stop-color="#bfc7d2"/></linearGradient>
<linearGradient id="u1" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5ec8ff"/><stop offset="1" stop-color="#2f7bff"/></linearGradient>
<linearGradient id="u2" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4fe08f"/><stop offset="1" stop-color="#17a85f"/></linearGradient>
<linearGradient id="u3" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ffc35a"/><stop offset="1" stop-color="#f08a1a"/></linearGradient>"""
    drive = "M3.7 5.1h9.53c.55 0 1 .45 1 1v5.7c0 .55-.45 1-1 1H3.7c-.55 0-1-.45-1-1V6.1c0-.55.45-1 1-1z"
    body = f"""
<path d="{drive}" fill="#000" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{drive}" fill="url(#drive)"/>
<path d="M3.7 5.1h9.53c.55 0 1 .45 1 1v.35H2.7V6.1c0-.55.45-1 1-1z" fill="#fff" opacity=".6"/>
<rect x="3.7" y="9.75" width="9.53" height="1.25" rx=".62" fill="#2b2f38" opacity=".85"/>
<rect x="3.9" y="9.95" width="3.6" height=".85" rx=".42" fill="url(#u1)"/>
<rect x="7.4" y="9.95" width="2.2" height=".85" fill="url(#u2)"/>
<rect x="9.5" y="9.95" width="1.4" height=".85" fill="url(#u3)"/>
<rect x="3.9" y="7.0" width="5.2" height=".42" rx=".21" fill="#8a93a3"/>
<circle cx="12.5" cy="7.2" r=".42" fill="#3fd98f"/>"""
    icon("mide-disks", "#5a606c", "#1d2026", defs, body)


def backup():
    """Backup: caixa de arquivo com a seta circular (no lugar do relógio da Time Machine)."""
    defs = """
<linearGradient id="box" x1="0" x2="0" y1="6" y2="13.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#dfe6f0"/></linearGradient>
<linearGradient id="lid" x1="0" x2="0" y1="4" y2="6.6" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f6f8fb"/><stop offset="1" stop-color="#c9d1dd"/></linearGradient>"""
    body = """
<path d="M3.6 6.4h9.73v6.3c0 .5-.4.9-.9.9H4.5a.9.9 0 0 1-.9-.9z" fill="#000" opacity=".35" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="M3.6 6.4h9.73v6.3c0 .5-.4.9-.9.9H4.5a.9.9 0 0 1-.9-.9z" fill="url(#box)"/>
<rect x="3.1" y="4.35" width="10.73" height="2.25" rx=".55" fill="url(#lid)"/>
<rect x="7.1" y="7.25" width="2.73" height=".7" rx=".35" fill="#9aa6b8"/>
<path d="M10.35 11.05a2 2 0 1 1-.55-1.95" fill="none" stroke="#1d74f0" stroke-width=".5" stroke-linecap="round"/>
<path d="M9.35 8.55l.6.55-.7.4" fill="none" stroke="#1d74f0" stroke-width=".42" stroke-linecap="round" stroke-linejoin="round"/>"""
    icon("mide-backup", "#7cc4ff", "#3b6fd8", defs, body)


def video_player():
    """Vídeo: quadro de filme com o botão de tocar (no lugar do "Q" do QuickTime)."""
    defs = """
<linearGradient id="film" x1="0" x2="0" y1="3.5" y2="13.5" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2b2f38"/><stop offset="1" stop-color="#121418"/></linearGradient>
<linearGradient id="play" x1="7" x2="11" y1="6" y2="11" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff9a5a"/><stop offset="1" stop-color="#ff4f7b"/></linearGradient>"""
    holes = "".join(
        f'<rect x="{x}" y="{y}" width=".75" height=".55" rx=".15" fill="#fff" opacity=".85"/>'
        for x in (3.55, 12.63)
        for y in (4.6, 6.0, 7.4, 8.8, 10.2, 11.6)
    )
    body = f"""
<rect x="3.05" y="3.8" width="10.83" height="9.4" rx=".9" fill="#000" opacity=".45" filter="url(#soft)" transform="translate(0 .35)"/>
<rect x="3.05" y="3.8" width="10.83" height="9.4" rx=".9" fill="url(#film)"/>
{holes}
<circle cx="8.466" cy="8.5" r="2.55" fill="url(#play)"/>
<path d="M7.75 7.2v2.6c0 .2.22.32.39.21l2.05-1.3a.25.25 0 0 0 0-.42l-2.05-1.3a.25.25 0 0 0-.39.21z" fill="#fff"/>"""
    icon("mide-video-player", "#7aa8ff", "#3f4fd8", defs, body)


def mouse():
    """Mouse: mouse com dois botões e a roda (no lugar do mouse da Apple)."""
    defs = """
<linearGradient id="shell" x1="0" x2="0" y1="3" y2="14" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#d3d9e2"/></linearGradient>"""
    shape = "M8.466 2.9c2.1 0 3.4 1.6 3.4 3.7v3.8c0 2.1-1.3 3.75-3.4 3.75s-3.4-1.65-3.4-3.75V6.6c0-2.1 1.3-3.7 3.4-3.7z"
    body = f"""
<path d="{shape}" fill="#000" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{shape}" fill="url(#shell)"/>
<path d="M5.07 7.15h6.79M8.466 2.95v4.2" stroke="#aab3c0" stroke-width=".14"/>
<rect x="8.16" y="4.05" width=".62" height="1.55" rx=".31" fill="#5b6478"/>
<path d="M5.4 5.2c.2-1 .9-1.75 1.9-2.05" fill="none" stroke="#fff" stroke-width=".3" stroke-linecap="round" opacity=".9"/>"""
    icon("mide-mouse", "#9aa6b8", "#4f5a6c", defs, body)


def notifications():
    """Notificações: sino com o selo (no lugar dos balões de mensagem)."""
    defs = """
<linearGradient id="bell" x1="0" x2="0" y1="3" y2="12.5" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e3ecfb"/></linearGradient>"""
    bell = "M8.466 3.4c1.95 0 3.35 1.5 3.35 3.45v2.4l1.05 1.6c.2.3 0 .7-.37.7H4.43c-.36 0-.57-.4-.37-.7l1.05-1.6v-2.4c0-1.95 1.4-3.45 3.35-3.45z"
    body = f"""
<path d="{bell}" fill="#3a0d5c" opacity=".4" filter="url(#soft)" transform="translate(0 .35)"/>
<path d="{bell}" fill="url(#bell)"/>
<path d="M7.25 12.05a1.25 1.25 0 0 0 2.43 0z" fill="url(#bell)"/>
<circle cx="11.9" cy="4.3" r="1.25" fill="#ff5a5f" stroke="#fff" stroke-width=".22"/>"""
    icon("mide-notifications", "#c08bff", "#7a3fe0", defs, body)


def mark_symbolic(path, size, color="#363636"):
    """Marca do mide (anel com ponto) no lugar do logo da Apple, para ícones de
    `start-here` (menu do sistema). Cor pelo esquema do tema, como o original."""
    k = size / 16
    svg = f"""<svg width="{size}" height="{size}" version="1.1" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <style id="current-color-scheme" type="text/css">.ColorScheme-Text {{ color:{color}; }}</style>
 </defs>
 <g class="ColorScheme-Text" fill="currentColor" transform="scale({k})">
  <path d="M8 2.2A5.8 5.8 0 1 0 8 13.8 5.8 5.8 0 0 0 8 2.2zm0 1.75a4.05 4.05 0 1 1 0 8.1 4.05 4.05 0 0 1 0-8.1z"/>
  <circle cx="9.55" cy="6.45" r="1.75"/>
 </g>
</svg>
"""
    Path(path).write_text(svg)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    globe()
    store()
    terminal()
    text_editor()
    settings()
    screenshot()
    files()
    default_app()
    calendar()
    clock()
    contacts()
    music()
    photos()
    system_monitor()
    maps()
    reminders()
    help_icon()
    dictionary()
    podcast()
    accessibility()
    camera()
    cleaner()
    mail()
    image_viewer()
    disks()
    backup()
    video_player()
    mouse()
    notifications()
    mark_symbolic(OUT / "mide-mark.svg", 16)
    print("ícones gerados em", OUT)
