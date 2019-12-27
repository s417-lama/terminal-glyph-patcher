#!/usr/bin/env python

# Forked from: https://github.com/Lokaltog/vim-powerline/blob/develop/fontpatcher/fontpatcher

"""Terminal Glyph Patcher

Patch your own glyphs to your terminal fonts. Requires FontForge with Python bindings.
"""

from __future__ import division

import argparse
import os
import sys
import re

try:
    import fontforge
    import psMat
except ImportError:
    sys.stderr.write('The required FontForge modules could not be loaded.\n\n')

    if sys.version_info.major > 2:
        sys.stderr.write('FontForge only supports Python 2. Please run this script with the Python 2 executable - e.g. "python2 {0}"\n'.format(sys.argv[0]))
    else:
        sys.stderr.write('You need FontForge with Python bindings for this script to work.\n')

    sys.exit(1)

# Handle command-line arguments
parser = argparse.ArgumentParser(description='Terminal Glyph Patcher')

parser.add_argument('fonts', help='font file to patch', metavar='font', nargs='+')
parser.add_argument('--no-rename', help='don\'t add " with Terminal Glyphs" to the font name', default=True, action='store_false', dest='rename')
parser.add_argument('--fix-mono', help='fixes some mono-fonts which have glyphs of 0 widths', default=False, action='store_true', dest='fixmono')
parser.add_argument('--fix-win', help='modifies font names such that Windows correctly recognizes font families', default=False, action='store_true', dest='fixwin')

args = parser.parse_args()

symbols = [
    # Right/left-aligned glyphs will have their advance width reduced in order to overlap the next glyph slightly
    {'unicode': 0xe0b0, 'align': 'l', 'stretch': 'xy', 'overlap': True, 'path': 'svg/arrow_right.svg'     },
    {'unicode': 0xe0b1, 'align': 'l', 'stretch': 'xy', 'overlap': True, 'path': 'svg/arrow_right_thin.svg'},
    {'unicode': 0xe0b2, 'align': 'r', 'stretch': 'xy', 'overlap': True, 'path': 'svg/arrow_left.svg'      },
    {'unicode': 0xe0b3, 'align': 'r', 'stretch': 'xy', 'overlap': True, 'path': 'svg/arrow_left_thin.svg' },
]

def get_font_dim(font):
    # Initial font dimensions
    font_dim = {
        'xmin'  : 0,
        'ymin'  : -font.descent,
        'xmax'  : 0,
        'ymax'  : font.ascent,
        'width' : 0,
        'height': 0,
    }

    # Find the biggest char width and height
    #
    # 0x00-0x17f is the Latin Extended-A range
    # 0x2500-0x2600 is the box drawing range
    for glyph in range(0x00, 0x17f) + range(0x2500, 0x2600):
        try:
            (xmin, ymin, xmax, ymax) = font[glyph].boundingBox()
        except TypeError:
            continue

        if font_dim['width'] == 0:
            font_dim['width'] = font[glyph].width

        if ymin < font_dim['ymin']: font_dim['ymin'] = ymin
        if ymax > font_dim['ymax']: font_dim['ymax'] = ymax
        if xmax > font_dim['xmax']: font_dim['xmax'] = xmax

    # Calculate font height
    font_dim['height'] = abs(font_dim['ymin']) + font_dim['ymax']

    return font_dim

def get_glyph_dim(glyph):
    (xmin, ymin, xmax, ymax) = glyph.boundingBox()

    return  {
        'xmin'  : xmin,
        'ymin'  : ymin,
        'xmax'  : xmax,
        'ymax'  : ymax,
        'width' : xmax + (-xmin),
        'height': ymax + (-ymin),
    }

# Patch provided fonts
for font_path in args.fonts:
    try:
        font = fontforge.open(font_path)
    except EnvironmentError:
        sys.exit(1)

    # Rename font
    if args.rename:
        font.familyname += ' with Terminal Glyphs'
        font.fullname += ' with Terminal Glyphs'
        font.fontname += 'WithTerminalGlyphs'
        font.appendSFNTName('English (US)', 'Preferred Family', font.familyname)
        font.appendSFNTName('English (US)', 'Compatible Full', font.fullname)
    if args.fixwin:
        font.fontname = re.sub(r'\W', '', font.familyname)

    font_dim = get_font_dim(font)

    # Update the font encoding to ensure that the Unicode glyphs are available
    font.encoding = 'ISO10646'

    # Fetch this property before adding outlines
    onlybitmaps = font.onlybitmaps

    # Create glyphs from symbol font
    for symbol in symbols:
        # Import svg glyph
        glyph = font.createChar(symbol['unicode'])
        glyph.importOutlines(symbol['path'])

        # Prepare symbol glyph dimensions
        sym_dim = get_glyph_dim(glyph)

        # Select and paste symbol to its unicode code point
        font.selection.select(symbol['unicode'])

        # Handle glyph stretching
        if 'x' in symbol['stretch']:
            # Stretch the glyph horizontally
            scale_ratio = font_dim['width'] / sym_dim['width']

            font.transform(psMat.scale(scale_ratio, 1))
        if 'y' in symbol['stretch']:
            # Stretch the glyph vertically
            scale_ratio = font_dim['height'] / sym_dim['height']

            font.transform(psMat.scale(1, scale_ratio))

        # Use the dimensions from the pasted and stretched glyph
        sym_dim = get_glyph_dim(font[symbol['unicode']])

        # Center-align the glyph vertically
        font_ycenter = font_dim['height'] / 2
        sym_ycenter  = sym_dim['height'] / 2

        # First move it to the ymax (top)
        font.transform(psMat.translate(0, font_dim['ymax'] - sym_dim['ymax']))

        # Then move it the y center difference
        font.transform(psMat.translate(0, sym_ycenter - font_ycenter))

        # Ensure that the glyph doesn't extend outside the font's bounding box
        if sym_dim['width'] > font_dim['width']:
            # The glyph is too wide, scale it down to fit
            scale_matrix = psMat.scale(font_dim['width'] / sym_dim['width'], 1)

            font.transform(scale_matrix)

            # Use the dimensions from the stretched glyph
            sym_dim = get_glyph_dim(font[symbol['unicode']])

        # Handle glyph alignment
        if symbol['align'] == 'c':
            # Center align
            align_matrix = psMat.translate(font_dim['width'] / 2 - sym_dim['width'] / 2 , 0)
        elif symbol['align'] == 'r':
            # Right align
            align_matrix = psMat.translate(font_dim['width'] - sym_dim['width'], 0)
        else:
            # No alignment (left alignment)
            align_matrix = psMat.translate(0, 0)

        font.transform(align_matrix)

        if symbol['overlap'] is True:
            overlap_width = font.em / 48

            # Stretch the glyph slightly horizontally if it should overlap
            font.transform(psMat.scale((sym_dim['width'] + overlap_width) / sym_dim['width'], 1))

            if symbol['align'] == 'l':
                # The glyph should be left-aligned, so it must be moved overlap_width to the left
                # This only applies to left-aligned glyphs because the glyph is scaled to the right
                font.transform(psMat.translate(-overlap_width, 0))

        # Ensure the font is considered monospaced on Windows
        font[symbol['unicode']].width = font_dim['width']

    if font.bitmapSizes and not onlybitmaps:
        # If this is an outline font with bitmaps, regenerate bitmaps for the changed glyphs
        font.selection.changed()

        for size in font.bitmapSizes:
            font.regenBitmaps((size, ))

    output_name, extension = os.path.split(font_path)[1].rsplit('.', 1)
    if extension.lower() not in ['ttf', 'otf']:
        # Default to OpenType if input is not TrueType/OpenType
        extension = 'otf'
    if args.fixmono:
        for glyph in font.glyphs():
            if glyph.width == 0: glyph.width = font_dim['width']

    if onlybitmaps:
        # Generate BDF font
        font.generate('{0}-with-Terminal-Glyphs.bdf'.format(output_name, bitmap_type='bdf'))
    else:
        # Generate OTF/TTF font
        font.generate('{0}-with-Terminal-Glyphs.{1}'.format(output_name, extension))
