#!/usr/bin/env python
#-*- cording: utf-8 -*-
from datetime import datetime
from time import sleep
import random

def main():
  log = open("time_output.txt", "w")

  for i in range(10):
    now = str(datetime.now())
    data = random.randint(0, 1024)
    log.write(now + " " + str(data) + "\n")
    print(".")
    sleep(.9)
  log.flush()
  log.close

if __name__ == "__main__":
  main()
