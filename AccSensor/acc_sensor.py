#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wiringpi as pi
import time, math
import lis3dh

def main():
  count = 0
  SPI_CS = 0
  SPI_SPEED = 100000
  pi.wiringPiSPISetup (SPI_CS, SPI_SPEED)
  accel = lis3dh.lis3dh( SPI_CS )

  while True:
    ( acc_x, acc_y, acc_z ) = accel.get_accel()
    ( x_angle, y_angle ) = accel.get_angle()
    print (count, "  A_X : ", acc_x, " A_Y : ", acc_y, "A_Z : ", acc_z )
    print ("X_angle : ", x_angle, " Y_angle : ", y_angle, "\n" )
    #time.sleep(0.5)
    count += 1

if __name__== "__main__":
  main()


