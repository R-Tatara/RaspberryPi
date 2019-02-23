#!/usr/bin/env python
#-*- cording: utf-8 -*-
import sys

#Read file
def main():
  if (len(sys.argv) != 2):
    print("Usage : $ python file_input.py filename")
    sys.exit

  scriptname = sys.argv[0]
  filename = sys.argv[1]

  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  for line in lines:
    print(line, end = "")

if __name__ == "__main__":
  main()
