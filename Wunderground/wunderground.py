#!/usr/bin/env python
#-*- cording: utf-8 -*-
import requests

def main():
  ApiUrl = 'http://api.wunderground.com/api/7129c16bae9ee521/forecast/q/JP/Susenji.json'
  r = requests.get(ApiUrl)
  forecast = r.json
  list = ['forecast','simpleforecast','forecastday','0']

  year =  forecast()[list[0]][list[1]][list[2]][int(list[3])]['date']['year']
  year = int(year)
  month =  forecast()[list[0]][list[1]][list[2]][int(list[3])]['date']['month']
  month = int(month)
  day =  forecast()[list[0]][list[1]][list[2]][int(list[3])]['date']['day']
  day = int(day)
  day_week =  forecast()[list[0]][list[1]][list[2]][int(list[3])]['date']['weekday_short']
  weather = forecast()[list[0]][list[1]][list[2]][int(list[3])]['conditions']
  high_temp = forecast()[list[0]][list[1]][list[2]][int(list[3])]['high']['celsius']
  high_temp = int(high_temp)
  low_temp = forecast()[list[0]][list[1]][list[2]][int(list[3])]['low']['celsius']
  low_temp = int(low_temp)
  humidity  = forecast()[list[0]][list[1]][list[2]][int(list[3])]['avehumidity']
  humidity = int(humidity)
  rain_prob  = forecast()[list[0]][list[1]][list[2]][int(list[3])]['pop']
  rain_prob = int(rain_prob)

  print (year, '/', month, '/',day, '(', day_week, ')')
  print ('Weather  : ', weather)
  print ('High temp: ', high_temp)
  print ('Low temp : ', low_temp)
  print ('Humidity : ', humidity)
  print ('Rain prob: ', rain_prob)

if __name__ == "__main__":
  main()
