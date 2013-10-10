#!/usr/bin/env python3

import subprocess

class Pactl:

  sources = {}
  sinks   = {}
  source_output = {}
  sink_input = {}

def parse_pactl(next):

  while 1:
    
    line = next()
    
    if line ...

def pactl():

  # Get pactl output
  output = subprocess.check_output(['pactl', 'list']).decode('utf-8')
  
  lines = output.split('\n')

  data = parse_pactl(lines.next)

    
    if line.startswith('Source'):

      currentSource = Source()

    elif line.startswith('\tDescription:'):

      _, _, name = line.partition(': ')
      currentSource.name = name

    elif line.startswith('\tDescription:'):

      _, _, name = line.partition(': ')
      currentSource.name = name



if __name__ == '__main__':
  
  pactl()

