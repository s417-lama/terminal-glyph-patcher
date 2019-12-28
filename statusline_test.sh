#!/bin/bash

print_line() {
  name=$1
  primary_separator_left=$2
  secondary_separator_left=$3
  primary_separator_right=$4
  secondary_separator_right=$5
  primary_color=$6
  secondary_color=$7

  set_primary_line=$(tput sgr0 && tput bold && tput setaf $secondary_color && tput setab $primary_color)
  set_secondary_line=$(tput sgr0 && tput setaf $primary_color && tput setab $secondary_color)
  set_background=$(tput sgr0 && tput setaf $secondary_color)
  set_end_line=$(tput sgr0)

  left_line="${set_primary_line} ${name} ${set_secondary_line}${primary_separator_left} Terminal ${secondary_separator_left} Glyph ${secondary_separator_left} Patcher ${set_background}${primary_separator_left}${set_end_line}"
  right_line="${set_background}${primary_separator_right}${set_secondary_line} Terminal ${secondary_separator_right} Glyph ${secondary_separator_right} Patcher ${primary_separator_right}${set_primary_line} ${name} ${set_end_line}"

  let n_wchar=$(expr ${#primary_separator_left} \* 2 \* 2)+$(expr ${#secondary_separator_left} \* 2 \* 2)
  let n_left_columns=${#left_line}-${#set_primary_line}-${#set_secondary_line}-${#set_background}-${#set_end_line}
  let n_columns=$(tput cols)+${#set_primary_line}+${#set_secondary_line}+${#set_background}+${#set_end_line}+${n_wchar}-${n_left_columns}

  printf "$left_line%${n_columns}s\n\n" "$right_line"
}

print_line Arrow                81  240
print_line Circle               157 240
print_line Slant1               222 240
print_line Slant2               210 240
print_line Diamond1         218 240
print_line Diamond2     183 240
