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

### Etapa 2: os outros apps que recriavam ícones da Apple

Depois de revisar as 1.446 imagens de apps do tema, ganharam desenho próprio:

| Recriação da Apple | Desenho do mide | Nomes no tema |
|---|---|---|
| Calendário (o "26") | Folha com argolas e a grade dos dias | `calendar`, `org.gnome.Calendar`... |
| Relógio | Mostrador claro no azul-esverdeado | `preferences-system-time`, `org.gnome.clocks`... |
| Contatos | Cartão de visita | `addressbook`, `org.gnome.Contacts`... |
| Música (nota rosa) | Disco de vinil | `gnome-music`, `elisa`, `juk`, `cantata`... |
| Fotos (flor) | Três fotos em leque | `shotwell`, `org.gnome.Photos`... |
| Monitor de Atividade (ECG) | Barras de uso e a linha de carga | `utilities-system-monitor`, `org.gnome.PowerStats`... |
| Mapas | Mapa dobrado com o alfinete | `gnome-maps`, `org.gnome.Maps`... |
| Lembretes | Lista com caixas marcadas | `basket`, `notes`... |
| Ajuda | Balão com "?" | `help`, `yelp`... |
| Dicionário ("Aa" vermelho) | Livro aberto com a fita | `accessories-dictionary`... |
| Podcasts | Microfone de estúdio | `accessories-podcast`, `podcast-amarok` |
| Acessibilidade | Símbolo universal no anel | `access`... |
| Captura de Imagem / Photo Booth | Câmera | `accessories-camera`, `cheese`... |
| Utilitário de Sistema (estetoscópio) | Vassoura com brilhos | `accessories-system-cleaner`... |
| Mail | Envelope com o selo | `internet-mail`, `evolution`... |
| Pré-Visualização | Foto com o selo de ampliar | `eog`, `org.gnome.Loupe`... |
| Utilitário de Disco | Unidade com a barra de uso | `gnome-disks`... |
| Time Machine | Caixa com a seta circular | `deja-dup`, `preferences-system-backup`... |
| QuickTime ("Q") | Quadro de filme com o botão de tocar | `org.gnome.Totem`, `Showtime` |
| Magic Mouse | Mouse de dois botões | `preferences-desktop-peripherals`, `input-mouse` |
| Mensagens (balões) | Dois balões, um digitando | `preferences-desktop-notification` (sino), `polari`, `pidgin` |
| Gravador de Voz | Ondas com o botão de gravar | `gnome-sound-recorder`, `org.gnome.SoundRecorder` |
| Catálogo de Fontes ("Aa") | "F" e "f" sobre a folha | `fonts`, `embellish` |
| Tempo | Sol atrás da nuvem, cores de fim de tarde | `indicator-weather`, `org.gnome.Weather` |
| Safari / App Store / Preferências (variantes) | Globo / sacola / controles | `safari`, `softwarecenter-ubuntu`, `vmware-netcfg`... |
| Maçã em desenhos de iMac | Marca do mide | `computer`, `video-television`, `variety`, `putty`, `xwaylandvideobridge` |
| Logo da Apple em `preferences-desktop-icons` | Quatro blocos | |

Ficaram, por serem símbolos comuns e não desenhos da Apple: o ⌘ (tecla), a lixeira,
as pastas azuis e o estilo arredondado em geral. Ícones de serviços da própria Apple
usados por apps de terceiros (como `icloud`) mostram a marca do serviço, como os do
Google ou da Microsoft.

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

### Etapa 4: tipos de arquivo e símbolos (2026-10-21)

Revisão dos 298 tipos de arquivo (`src/mimes/scalable`) e de 565 símbolos (apps,
aparelhos, lugares, categorias, tipos e emblemas), com folhas de contato feitas pelo
`examples/mide-folha-de-icones` do mide.

| Recriação da Apple | No mide-icons | Nomes no tema |
|---|---|---|
| Caixa marrom com fita do instalador de pacotes | Caixa verde-azulada lisa, o mesmo cartão e símbolo | `application-software`, `application-x-executable`, `application-x-alpm-package`, `system-component-*` (também em `alternative/`), `file-roller` |
| Nota do Apple Music | Nota do próprio tema (`application-audio`) | `audio-x-generic` |
| Xcode (planta com martelo) | Folha de código do tema (`text-x-script`) | `text-x-makefile` |
| Rosto do Finder (símbolo) | Pasta | `system-file-manager-symbolic` (Nautilus, Arquivos do GNOME) |
| Bússola do Safari (símbolo) | Globo | `web-browser-symbolic` (e os atalhos de navegador) |
| "A" da App Store (símbolo) | Sacola com seta | `software-store-symbolic`, `gnome-software-symbolic` |
| "A" das pastas de modelos (símbolo e 16 px) | Pasta de documentos | `folder-templates-symbolic`, `places/16/folder-templates` |
| Pássaro do Swift | Folha de código | `text-swift-symbolic` |

Ficam como estão: logos de outras empresas em tipos de arquivo (Office, Adobe, linguagens),
o símbolo ⌘ (é o da tecla, não um logo) e os ícones de apps de terceiros que usam caixas
como marca própria (BoxBuddy, Warehouse, Boxflat, Shelly).

