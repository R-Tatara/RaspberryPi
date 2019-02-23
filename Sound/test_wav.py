#!/usr/bin/env python
#-*- cording: utf-8 -*-
import pygame
from pygame.locals import *

#Play sound.wav
def main():
  pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 1024)
  sound = pygame.mixer.Sound("../../sound/8bit_2.wav")
  sound.play()

  try:
    while True:
      pass
  except KeyboardInterrupt:
          pygame.mixer.quit()

if __name__ == "__main__":
  main()
