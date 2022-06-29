#!/usr/bin/env python3
import os

def main():
  file = input('filepath?(/path/to/file.py)\n')
  os.system('cython '+file+' --embed')
  os.system('PYTHONLIBVER=python$(python3 -c \'import sys; print(\".\".join(map(str, sys.version_info[:2])))\')$(python3-config --abiflags)')
  c_file = input('filename?(example.c)\n')
  b_file = input('filename?(example)(example.exe)\n')
  os.system('gcc -Os $(python3-config --includes) '+c_file+' -o '+b_file+' $(python3-config --ldflags) -l$PYTHONLIBVER')
if __name__ == "__main__": main()

'''
PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)
gcc -Os $(python3-config --includes) example_file.c -o output_bin_file $(python3-config --ldflags) -l $PYTHONLIBVER
'''
