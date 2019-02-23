#!/usr/bin/env python
#-*- cording: utf-8 -*-
from datetime import datetime
from time import sleep

def now_time():
  d = datetime.now()
  year = d.year
  month = d.month
  day = d.day
  hour = d.hour
  minute = d.minute
  second = d.second
  datetime_str = d.strftime('%Y/%m/%d %H:%M:%S')
  print(datetime_str)
  return

def main():
  while True:
    now_time()
    sleep(1)

if __name__ == "__main__":
  main()
