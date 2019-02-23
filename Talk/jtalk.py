#!/usr/bin/env python
# coding: UTF-8
import subprocess

#Speak with female voice of jtalk
def jtalk(text):
  word = '"' + text + '"'
  command = "echo \"%s\"" % word
  command += " | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m ./Voice_mei/mei_normal.htsvoice -ow /dev/stdout"
  command += " | aplay --quiet"

  proc= subprocess.Popen(
    command,
    shell  = True,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE)
  print (word)

def main():
  text = 'おはようございます。ただいま、12月24日日曜日22時23分、今日の天気はくもり、気温は11度、降水確率は10パーセントです。'
  jtalk(text)

if __name__ == "__main__":
  main()
