# Terminal Glyph Patcher
Patch your own glyphs to your terminal fonts (e.g., extra powerline separators).

Enjoy your original statusline in the terminal!

![statusline.png](https://raw.githubusercontent.com/wiki/s417-lama/terminal-glyph-patcher/images/statusline.png)

## Characteristics

- Your own **SVG** files (`.svg`) can be used to generate glyphs.
    - Preset glyphs below are also pure SVG files.
- Generated glyphs are always **half-width**.
    - It is less likely to cause problems related with [ambiguous-width characters](http://www.unicode.org/reports/tr11/tr11-36.html).
- The position of separator glyphs can be finely adjusted.

## Try it

### 1. Clone this repo

```
git clone https://github.com/s417-lama/terminal-glyph-patcher.git
```

### 2. Patch your font by using preset glyphs

`python-fontforge` package is required. Install instruction: [Installing FontForge](http://designwithfontforge.com/en-US/Installing_Fontforge.html)
```
cd terminal-glyph-patcher
fontforge -script terminal-glyph-patcher.py /path/to/your/font.ttf
```
Then install the patched font to your system, and apply it to your terminal.

### 3. Show statusline

```
./statusline_test.sh
```
Then statuslines like the top image should be shown.

## Patch your own glyphs

For now you should modify `terminal-glyph-patcher.py` directly.
What you should modify is `symbols` list in the source code.
This list looks like the below.

```python
{'unicode': 0xe0b0, 'align': 'l', 'stretch': 'xy', 'overlap': 0.05, 'path': 'svg/arrow_right.svg'     },
{'unicode': 0xe0b1, 'align': 'l', 'stretch': 'xy', 'overlap': 0.05, 'path': 'svg/arrow_right_thin.svg'},
{'unicode': 0xe0b2, 'align': 'r', 'stretch': 'xy', 'overlap': 0.01, 'path': 'svg/arrow_left.svg'      },
{'unicode': 0xe0b3, 'align': 'r', 'stretch': 'xy', 'overlap': 0.01, 'path': 'svg/arrow_left_thin.svg' },
```

------------------------------

#### `unicode` :: int
Unicode number to be register. If a glyph already exists in the font, it will be overwritten.

#### `align` :: `'l'`, `'r'`, or `'c'`.
If `l` is set, the glyph is aligned to the left edge. If `r`, it is aligned to the right.
If `c` is set, the glyph is aligned in the center.

#### `stretch` :: `''`, `'x'`, `'y'`, or `'xy'`.
If `x` is set, the glyph is expanded to fill up the entire horizontal space. `y` is for the vertical space.

#### `overlap` :: float
Sometimes there exists a gap between glyphs. To fill it up, `overlap` parameter is used.
The output glyph width will be `Glyph width * (1 + overlap)`, which means the glyph will be a bit leaked from the normal bounding box.
If `align` parameter is `l`, the overflow goes to the left side. If `r`, it goes to the right side.

#### `path` :: string
Path to your SVG file.

------------------------------

For example, `U+E0B0` glyph should align to the left(`align='l'`), and it should fill up the entire glyph space (`stretch='xy'`).
To fill up the left gap, `overlap` parameter is set to some value (this parameter is decided in an ad-hoc way).

## Preset Glyphs

The glyphs below are included in `svg/` directory by default.
These glyphs are pure SVG files.

Basically it follows the layout convention of [Powerline Extra Symbols](https://github.com/ryanoasis/powerline-extra-symbols) (not exactly same, though).

|        |        |        |        |        |        |        |        |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| U+E0B0 | U+E0B1 | U+E0B2 | U+E0B3 | U+E0B4 | U+E0B5 | U+E0B6 | U+E0B7 |
| ![U+E0B0](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/arrow_right.svg?sanitize=true) | ![U+E0B1](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/arrow_right_thin.svg?sanitize=true) | ![U+E0B2](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/arrow_left.svg?sanitize=true) | ![U+E0B3](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/arrow_left_thin.svg?sanitize=true) | ![U+E0B4](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/circle_right.svg?sanitize=true) | ![U+E0B5](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/circle_right_thin.svg?sanitize=true) | ![U+E0B6](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/circle_left.svg?sanitize=true) | ![U+E0B7](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/circle_left_thin.svg?sanitize=true) |
| U+E0B8 | U+E0B9 | U+E0BA | U+E0BB | U+E0BC | U+E0BD | U+E0BE | U+E0BF |
| ![U+E0B8](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_left_bottom.svg?sanitize=true) | ![U+E0B9](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_left_bottom_thin.svg?sanitize=true) | ![U+E0BA](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_right_bottom.svg?sanitize=true) | ![U+E0BB](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_right_bottom_thin.svg?sanitize=true) | ![U+E0BC](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_left_top.svg?sanitize=true) | ![U+E0BD](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_left_top_thin.svg?sanitize=true) | ![U+E0BE](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_right_top.svg?sanitize=true) | ![U+E0BF](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/slant_right_top_thin.svg?sanitize=true) |
| U+E0C0 | U+E0C1 | U+E0C2 | U+E0C3 | U+E0C4 | U+E0C5 | | |
| ![U+E0C0](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/cross.svg?sanitize=true) | ![U+E0C1](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/cross_left.svg?sanitize=true) | ![U+E0C2](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/cross_right.svg?sanitize=true) | ![U+E0C3](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/cross_thin.svg?sanitize=true) | ![U+E0C4](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/diamond.svg?sanitize=true) | ![U+E0C5](https://raw.githubusercontent.com/s417-lama/terminal-glyph-patcher/master/svg/diamond_thin.svg?sanitize=true) | | |

# Reference

- [Powerline Extra Symbols](https://github.com/ryanoasis/powerline-extra-symbols)
    - Part of [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts). This project (terminal-glyph-patcher) was inspired by it.
- [vim-powerline](https://github.com/Lokaltog/vim-powerline)
    - Terminal-glyph-patcher is based on `vim-powerline`'s patcher script.
- [powerline/fontpatcher](https://github.com/powerline/fontpatcher)
    - The original font patcher of Powerline.
