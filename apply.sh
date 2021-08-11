#!/bin/bash

# PROF_ID=33af96b1-496d-4bf3-a3ec-79daa1f46d93 # got by `gsettings get org.gnome.Terminal.ProfilesList list`
PROF_ID=$(gsettings get org.gnome.Terminal.ProfilesList default | sed "s/'//g")
# fc-list

# FONT_NAME="Ricty with Terminal Glyphs"
# gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:${PROF_ID}/ font "$FONT_NAME 10"

FONT_NAME="PlemolJP Console with Terminal Glyphs"
gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:${PROF_ID}/ font "$FONT_NAME 9"

# FONT_NAME="PlemolJP35 Console with Terminal Glyphs"
# gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:${PROF_ID}/ font "$FONT_NAME 8"
