#!/usr/bin/env python3

import curses

def draw_menu(w):

  w.addstr(1, 1, "1: Playback  2: Recording  3: Config")

def main(stdscr):

  # Keep background transperant
  curses.use_default_colors()

  # Hide cursor
  curses.curs_set(False)

  # Clear screen
  stdscr.clear()

  stdscr.border()

  draw_menu(stdscr)

  stdscr.refresh()
  stdscr.getkey()

if __name__ == '__main__':
 
  curses.wrapper(main)


