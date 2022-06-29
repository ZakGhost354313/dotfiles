import os
def l(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
def main():
  file = input('filepath?(/path/to/file.py)?\n')
  os.system('chmod a+x '+file)
  l(file,"#!/usr/bin/env python3")
if __name__ == "__main__": main()
