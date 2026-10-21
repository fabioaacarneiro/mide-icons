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
    mark_symbolic(OUT / "mide-mark.svg", 16)
    print("ícones gerados em", OUT)
