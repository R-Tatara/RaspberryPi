#!/usr/bin/env python
#-*- cording: utf-8 -*-
import serial

#Read 1 byte from Arduino
def main():
  port = "/dev/ttyACM0"
  serialFromArduino = serial.Serial(port, 9600)
  serialFromArduino.flushInput()
  while True:
    input = serialFromArduino.readline()
    input_value = int(input)
    print(input_value)

if __name__ == "__main__":
  main()
