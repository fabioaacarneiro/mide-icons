#!/usr/bin/env python3
"""Aplica as mudanças do mide no tema (rodar de novo depois de trazer o WhiteSur).

1. Ícones que recriam desenhos da Apple passam a usar os do mide (`mide/icons`):
   o rosto do Finder, a bússola do Safari, o "A" da App Store, a engrenagem das
   Preferências do Sistema, o Terminal, o TextEdit e a Captura de Tela. Os atalhos
   que apontam para eles (Nautilus, Firefox não, gnome-control-center...) seguem.
2. O logo da Apple (`start-here`, todos os tamanhos) vira a marca do mide; a maçã do
   iMac (`computer`) também; `folder-apple` vira pasta comum.
3. O "A" das pastas `folder-templates` (todas as cores) vira um modelo de documento.
4. Nomes dos apps do mide (`mide-terminal`, `mide-files`...).

Uso: python3 mide/build_icons.py && python3 mide/apply.py
"""

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "mide" / "icons"
APPS = ROOT / "src" / "apps" / "scalable"
LINKS = ROOT / "links" / "apps" / "scalable"

# Arquivo do tema → ícone do mide que o substitui.
REPLACE = {
    "file-manager": "mide-file-manager",
    "web-browser": "mide-web-browser",
    "softwarecenter": "mide-software-store",
    "system-software-install": "mide-software-store",
    "preferences-system": "mide-settings",
    "applications-system": "mide-settings",
    "application-default-icon": "mide-default-app",
    "terminal": "mide-terminal",
    "accessories-text-editor": "mide-text-editor",
    "text-editor": "mide-text-editor",
    "accessories-screenshot": "mide-screenshot",
    # Etapa 2: os outros apps que recriavam o ícone de um app da Apple.
    "calendar": "mide-calendar",
    "preferences-system-time": "mide-clock",
    "addressbook": "mide-contacts",
    "gnome-music": "mide-music",
    "shotwell": "mide-photos",
    "utilities-system-monitor": "mide-system-monitor",
    "gnome-maps": "mide-maps",
    "basket": "mide-reminders",
    "help": "mide-help",
    "accessories-dictionary": "mide-dictionary",
    "accessories-podcast": "mide-podcast",
    "access": "mide-accessibility",
    "accessories-camera": "mide-camera",
    "accessories-system-cleaner": "mide-cleaner",
    "internet-mail": "mide-mail",
    "eog": "mide-image-viewer",
    "gnome-disks": "mide-disks",
    "deja-dup": "mide-backup",
    "cheese": "mide-camera",
    "org.gnome.Totem": "mide-video-player",
    "org.gnome.PowerStats": "mide-system-monitor",
    "system-software-update": "mide-software-store",
    "org.gnome.Software.Generic": "mide-software-store",
    "org.gnome.Terminal.Preferences": "mide-terminal",
    # Painéis de configurações que recriavam os da Apple (um com o logo dela).
    "preferences-desktop-icons": "mide-default-app",
    "preferences-desktop-navigation": "mide-web-browser",
    "preferences-desktop-peripherals": "mide-mouse",
    "preferences-desktop-notification": "mide-notifications",
    # Revisão das 1.446 folhas de apps (2026-10-21).
    "safari": "mide-web-browser",
    "softwarecenter-debian": "mide-software-store",
    "softwarecenter-ubuntu": "mide-software-store",
    "software-properties": "mide-software-store",
    "terminix": "mide-terminal",
    "input-mouse": "mide-mouse",
    "vmware-netcfg": "mide-settings",
    "jockey": "mide-settings",
    "preferences-system-backup": "mide-backup",
    "org.gnome.Loupe": "mide-image-viewer",
    "Showtime": "mide-video-player",
    "cantata": "mide-music",
    "elisa": "mide-music",
    "juk": "mide-music",
    "playmymusic": "mide-music",
    "lx-music-desktop": "mide-music",
    "podcast-amarok": "mide-podcast",
    "polari": "mide-chat",
    "pidgin": "mide-chat",
    "gnome-sound-recorder": "mide-recorder",
    "fonts": "mide-fonts",
    "embellish": "mide-fonts",
    "calligrawords": "mide-text-editor",
    "words": "mide-text-editor",
    "indicator-weather": "mide-weather",
}

# Nomes dos apps do mide (os `.desktop` do mide usam estes) → ícone.
MIDE_APPS = {
    "mide-terminal": "mide-terminal.svg",
    "mide-text": "mide-text-editor.svg",
    "mide-files": "mide-file-manager.svg",
    "mide-settings": "mide-settings.svg",
    "mide-screenshot": "mide-screenshot.svg",
    "mide-calculator": "calc.svg",
    "mide-about": "../../devices/scalable/computer.svg",
}

# Símbolo de modelo de documento, na mesma área do "A" das pastas (≈ 5,2–11,6 x 6,6–11,1).
TEMPLATE_GLYPH = (
    "M6.35 6.6h3.1l1.5 1.5v3.05c0 .3-.25.55-.55.55H6.35a.55.55 0 0 1-.55-.55V7.15c0-.3.25-.55.55-.55z"
    "m.35.75v3.65h3.5V8.45h-.95a.4.4 0 0 1-.4-.4v-.7zm.55 1.25h1.4v.42h-1.4zm0 .95h2.4v.42h-2.4z"
)

MARK = (
    '<path d="M8 2.2A5.8 5.8 0 1 0 8 13.8 5.8 5.8 0 0 0 8 2.2zm0 1.75a4.05 4.05 0 1 1 0 8.1 4.05 4.05 0 0 1 0-8.1z"/>'
    '<circle cx="9.55" cy="6.45" r="1.75"/>'
)


# Desenhos de iMac com a maçã no queixo.
APPLE_ON_MONITOR = [
    "src/devices/scalable/computer.svg",
    "src/devices/scalable/video-television.svg",
    "src/apps/scalable/variety.svg",
    "src/apps/scalable/variety-slideshow.svg",
    "src/apps/scalable/xwaylandvideobridge.svg",
    "src/apps/scalable/putty.svg",
]


def path_bbox(d):
    """Caixa aproximada de um caminho SVG (pelos pontos de cada comando)."""
    tokens = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|-?(?:\d+\.?\d*|\.\d+)(?:e-?\d+)?", d)
    counts = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}
    x = y = sx = sy = 0.0
    xs, ys = [], []
    i, cmd = 0, None
    while i < len(tokens):
        if tokens[i].isalpha():
            cmd = tokens[i]
            i += 1
            if cmd in "Zz":
                x, y = sx, sy
                continue
        n = counts[cmd.upper()]
        args = [float(t) for t in tokens[i : i + n]]
        i += n
        rel = cmd.islower()
        up = cmd.upper()
        if up == "H":
            x = x + args[0] if rel else args[0]
        elif up == "V":
            y = y + args[0] if rel else args[0]
        else:
            pts = [(args[j], args[j + 1]) for j in range(0, n, 2)] if up != "A" else [(args[5], args[6])]
            for px, py in pts:
                ax, ay = (x + px, y + py) if rel else (px, py)
                xs.append(ax)
                ys.append(ay)
            x, y = (x + pts[-1][0], y + pts[-1][1]) if rel else pts[-1]
        xs.append(x)
        ys.append(y)
        if up == "M":
            sx, sy = x, y
            cmd = "l" if rel else "L"
    return min(xs), min(ys), max(xs), max(ys)


def mark_svg(size, color="#363636"):
    k = size / 16
    return (
        f'<svg width="{size}" height="{size}" version="1.1" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">\n'
        f' <defs>\n  <style id="current-color-scheme" type="text/css">.ColorScheme-Text {{ color:{color}; }}</style>\n </defs>\n'
        f' <g class="ColorScheme-Text" fill="currentColor" transform="scale({k})">{MARK}</g>\n</svg>\n'
    )


def write(path, text):
    path = Path(path)
    if path.is_symlink():
        path.unlink()
    path.write_text(text)


def size_of(path):
    m = re.search(r'<svg[^>]*\swidth="(\d+)', Path(path).read_text())
    return int(m.group(1)) if m else 16


def main():
    # 1. Recriações de ícones da Apple → ícones do mide.
    for target, source in REPLACE.items():
        write(APPS / f"{target}.svg", (ICONS / f"{source}.svg").read_text())
        # Um atalho com o mesmo nome em `links/` seria copiado por cima na instalação.
        link = LINKS / f"{target}.svg"
        if link.is_symlink():
            link.unlink()
    for icon in ICONS.glob("mide-*.svg"):
        if icon.name != "mide-mark.svg":
            write(APPS / icon.name, icon.read_text())

    # 2. Logo da Apple → marca do mide.
    for path in ROOT.glob("src/**/start-here*.svg"):
        # Só o logo do sistema (o da Apple); outros, como o do KDE, ficam.
        if path.is_symlink() or path.name not in ("start-here.svg", "start-here-symbolic.svg"):
            continue
        text = path.read_text()
        color = re.search(r"color:\s*(#[0-9a-fA-F]{3,6})", text)
        write(path, mark_svg(size_of(path), color.group(1) if color else "#363636"))
    # A maçã nos desenhos de iMac (um caminho escuro no queixo do monitor): a marca do
    # mide no mesmo lugar e tamanho.
    for rel in APPLE_ON_MONITOR:
        path = ROOT / rel
        text = path.read_text()
        def to_mark(m):
            x0, y0, x1, y1 = path_bbox(m.group(1))
            size = max(x1 - x0, y1 - y0)
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            k = size / 11.6  # a marca ocupa 11,6 da grade de 16
            return f'<g fill="#1e1f28" transform="translate({cx - 8 * k:.3f} {cy - 8 * k:.3f}) scale({k:.4f})">' + MARK + "</g>"
        text = re.sub(r'<path fill="#1e1f28" d="([^"]+)"/>', to_mark, text)
        write(path, text)
    for path in ROOT.glob("src/places/**/folder-apple*.svg"):
        plain = path.with_name(path.name.replace("folder-apple", "folder"))
        if plain.exists():
            write(path, plain.read_text())

    # 3. "A" das pastas de modelos → modelo de documento (o último caminho é o símbolo).
    for path in list(ROOT.glob("src/places/scalable/*folder-templates.svg")) + list(ROOT.glob("colors/*/folder-templates.svg")):
        if path.is_symlink():
            continue
        text = path.read_text()
        last = text.rfind("<path ")
        end = text.find("/>", last) + 2
        glyph = text[last:end]
        fill = re.search(r'fill="([^"]+)"', glyph)
        opacity = re.search(r'opacity="([^"]+)"', glyph)
        # Pastas em outra grade (viewBox de 64): o símbolo acompanha a escala.
        box = re.search(r'viewBox="0 0 ([\d.]+)', text)
        k = float(box.group(1)) / 16.933 if box else 64 / 16.933
        scale = f' transform="scale({k:.4f})"' if abs(k - 1) > 0.01 else ""
        new = f'<path d="{TEMPLATE_GLYPH}" fill="{fill.group(1) if fill else "#000"}"' + (f' opacity="{opacity.group(1)}"' if opacity else "") + scale + "/>"
        write(path, text[:last] + new + text[end:])

    # 4. Nomes dos apps do mide.
    for name, target in MIDE_APPS.items():
        link = LINKS / f"{name}.svg"
        if link.exists() or link.is_symlink():
            link.unlink()
        # O ícone já tem esse nome em `src` (mide-terminal...): atalho não precisa.
        if target != f"{name}.svg":
            os.symlink(target, link)
    print("mudanças do mide aplicadas")


if __name__ == "__main__":
    main()
