#!/bin/bash

# docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py fonts/Ricty-Regular.ttf
# docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py fonts/Ricty-Bold.ttf
# cp Ricty* ~/.fonts
# fc-cache -fv

# docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJP35Console/PlemolJP35Console-Regular.ttf
# docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJP35Console/PlemolJP35Console-Bold.ttf

docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJPConsole/PlemolJPConsole-Regular.ttf
docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJPConsole/PlemolJPConsole-Bold.ttf
docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJPConsole/PlemolJPConsole-Italic.ttf
docker run -it --rm -v $HOME:$HOME --workdir=$PWD jess/fontforge fontforge -script terminal-glyph-patcher.py PlemolJP_v0.2.2/PlemolJPConsole/PlemolJPConsole-BoldItalic.ttf

cp Plemol* ~/.fonts
fc-cache -fv
