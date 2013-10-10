#!/usr/bin/env python3

import curses
import subprocess

def pactl():

  output = subprocess.check_output(['pactl', 'list']).decode('utf-8')

  for line in output.split('\n'):
    print(line)

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



  # Draw a source
  sname = "Mplayer"
  ssink = "HDA Intel Audio"
  svol = "95%"

  source = curses.newwin(4, curses.COLS, 4, 0)
  source.border()
  source.addstr(1, 1, sname)
  source.addstr(2, 1, ssink)
  source.addstr(2, curses.COLS-len(svol)-1, svol)
  source.noutrefresh()



  curses.doupdate()
  menu.getkey()

if __name__ == '__main__':
  
  #curses.wrapper(main)

  pactl()

