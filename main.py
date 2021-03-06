#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
Get weather from weather underground
Created on 27/02/2017

Using json

alba.v.lamas@gmail.com
'''
from getweather import WeatherClient
from recommendation import Recommendation
import sys

api_key = None


def print_forecast(json_info, location):
    '''
    prints de temperature and the precipitations
    '''
    print "WEATHER FORECAST (" + location + ")"
    print "TEMPERATURE:" + json_info["temp"]["metric"] + " C"
    print "PRECIPITATION'S PROBABILITY: " + json_info["pop"] +"%"
    print "CONDITION: " + json_info["condition"]
    print "RECOMENDATION: " + Recommendation().recommend(json_info["condition"], json_info["temp"]["metric"])

if __name__ == "__main__":

    if len(sys.argv)<2:
		print "Must provide api key in code or cmdline arg"
		sys.exit(-1)
    else:
        api_key = sys.argv[1]

    wc = WeatherClient(api_key)
    location = "Lleida"
    json = wc.hourly(location)
    print_forecast(json[0], location)
