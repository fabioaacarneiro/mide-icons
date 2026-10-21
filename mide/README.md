# mide-icons

Tema de ícones do [mide](https://github.com/fabioaacarneiro/mide), um fork do
[WhiteSur icon theme](https://github.com/vinceliuice/WhiteSur-icon-theme) de
Vince Liuice (GPL-3.0, veja `COPYING` e `AUTHORS`). Todo o trabalho de arte do
WhiteSur é dele; aqui ficam só as mudanças do mide.

## Por que um fork

O mide é inspirado no macOS, mas não copia nada da Apple. O WhiteSur, por padrão,
traz o logo da Apple e recriações de ícones de apps da Apple. Este fork troca essas
partes por desenhos próprios, no mesmo acabamento do tema (mesma sombra, mesmo
quadrado arredondado, grade de 64 px).

## O que muda

| No WhiteSur | No mide-icons |
|---|---|
| Logo da Apple (`start-here`, todos os tamanhos) | Marca do mide (anel com ponto) |
| Maçã no iMac (`computer`) | Marca do mide |
| Rosto do Finder (`file-manager`, Nautilus, Nemo, Dolphin...) | Pasta do próprio tema sobre um quadrado claro |
| Bússola do Safari (`web-browser`) | Globo de vidro |
| "A" da App Store (`softwarecenter`, `system-software-install`) | Sacola com seta |
| Engrenagem das Preferências do Sistema (`preferences-system`, `applications-system`) | Três controles deslizantes |
| Ícone padrão de app (engrenagem) | Quatro blocos |
| Terminal do macOS (`terminal`) | Tela escura com o prompt ❯ e o cursor em bloco |
| TextEdit (`accessories-text-editor`, `text-editor`) | Folha com linhas e cursor de texto |
| Captura de Tela do macOS (`accessories-screenshot`) | Seleção tracejada com a mira |
| "A" das pastas de modelos (`folder-templates`, todas as cores) | Modelo de documento |
| `folder-apple` | Pasta comum |

E nomes para os apps do mide: `mide-terminal`, `mide-text`, `mide-files`,
`mide-settings`, `mide-screenshot`, `mide-calculator`, `mide-about`.

Outros ícones no estilo do macOS ainda recriam apps da Apple (Fotos, Música, Notas,
Mapas, Contatos...). Eles vão sendo trocados aos poucos, começando pelos que mais
aparecem.

## Como funciona

- `mide/build_icons.py` gera os ícones do mide em `mide/icons/` (SVG escrito à mão,
  com a sombra do WhiteSur em `mide/base-shadow.svgpart`).
- `mide/apply.py` aplica as trocas nos arquivos do tema. Depois de trazer uma versão
  nova do WhiteSur (`git fetch upstream && git merge upstream/master`), rode os dois
  de novo e confira os ícones.

```sh
python3 mide/build_icons.py && python3 mide/apply.py
./install.sh -n mide        # instala mide, mide-light e mide-dark em ~/.local/share/icons
```

Não use as opções `-a` (redesenhos de apps do macOS) nem `-p` (logo do KDE no lugar
do da Apple, que aqui já é a marca do mide).
