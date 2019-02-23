#!/usr/bin/env python
#-*- cording: utf-8 -*-

class MyClass:
  def __init__(self):
    self.data1 = 1
    self.data2 = []

  def func(self, data):
    self.data2.append(data)
    return 'Hi!'

def main():
  c = MyClass()
  print (c.data1)
  print (c.func('Python!'))
  print (c.data2)

if __name__ == "__main__":
  main()
