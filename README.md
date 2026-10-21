# mide-icons

Tema de ícones do [mide](https://github.com/fabioaacarneiro/mide), o ambiente de
desktop para Linux feito em Rust sobre Wayland.

![Ícones próprios do mide](mide/preview.png)

O mide-icons é um fork do excelente
[WhiteSur icon theme](https://github.com/vinceliuice/WhiteSur-icon-theme), de
**Vince Liuice**. Todo o trabalho de arte do WhiteSur é dele (licença GPL-3.0, veja
`COPYING` e `AUTHORS`); o README original continua em
[`README.WhiteSur.md`](README.WhiteSur.md). Se gostar do tema, apoie o autor original.

## O que muda em relação ao WhiteSur

O mide é inspirado no macOS, mas não copia nada da Apple. O WhiteSur, por padrão, traz
o logo da Apple e recriações dos ícones de vários apps da Apple. Este fork troca essas
partes por desenhos próprios, no mesmo acabamento do tema (mesma sombra, mesmo
quadrado arredondado, grade de 64 px):

- **Sem o logo da Apple:** o menu do sistema (`start-here`) e os desenhos de iMac usam
  a marca do mide (o anel com o ponto).
- **Desenhos próprios** (os da imagem acima) no lugar das recriações do Finder, Safari,
  App Store, Preferências do Sistema, Terminal, TextEdit, Captura de Tela, Calendário,
  Relógio, Contatos, Música, Fotos, Monitor de Atividade, Mapas, Lembretes, Mail,
  Mensagens, Tempo e outros, depois de revisar as 1.446 imagens de apps do tema.
- **Nomes para os apps do mide:** `mide-terminal`, `mide-files`, `mide-text`,
  `mide-settings`, `mide-screenshot`, `mide-calculator`, `mide-about`.

A lista completa, com os nomes de cada ícone trocado, fica em
[`mide/README.md`](mide/README.md).

## Instalar

No mide, o `data/mide-atualizar` instala este tema sozinho, na versão fixada pelo
projeto. Para instalar à mão:

```sh
./install.sh -n mide        # instala mide, mide-light e mide-dark em ~/.local/share/icons
```

Não use as opções `-a` (redesenhos de apps do macOS) nem `-p` (logo do KDE no lugar do
da Apple, que aqui já é a marca do mide). As outras opções do WhiteSur continuam
valendo (`./install.sh --help`).

## Atualizar a partir do WhiteSur

As mudanças do mide ficam em `mide/` e são reaplicadas depois de trazer uma versão
nova do original:

```sh
git fetch upstream && git merge upstream/master
python3 mide/build_icons.py && python3 mide/apply.py
```

Depois, confira os ícones renderizados e se nenhum atalho ficou quebrado
(`find <tema instalado> -xtype l`).
