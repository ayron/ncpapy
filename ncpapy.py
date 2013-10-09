#!/usr/bin/env python3

import curses

def main(stdscr):

  # Keep background transperant
  curses.use_default_colors()

  # Hide cursor
  curses.curs_set(False)

  # Clear screen
  stdscr.clear()

  # Draw menu
  menuBorder = curses.newwin(3, curses.COLS, 0, 0)
  menuBorder.border()
  menuBorder.noutrefresh()
  menu = curses.newpad(1, 50)
  menu.addstr(0, 0, "  1: Playback  2: Recording  3: Config")
  menu.noutrefresh( 0,0, 1,1, 1,curses.COLS-2)

    

  curses.doupdate()
  menu.getkey()

if __name__ == '__main__':
  
  curses.wrapper(main)


