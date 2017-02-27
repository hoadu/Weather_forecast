#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
Get weather from weather underground
Created on 27/02/2017

Using json

alba.v.lamas@gmail.com
'''

import sys
import requests
import json



class WeatherClient(object):
	'''get the weather iformation in WeatherUnderground's API 
	(http://www.wunderground.com/weather/api)'''

	url_base = 'http://api.wunderground.com/api'
	url_services= {
		"hourly":"/hourly/q/CA/"
	}

	def __init__(self, apikey):
		self.apikey = apikey


	def hourly(self, location)
		answer_format = "json"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_services["hourly"] + location + "." + answer_format

        r = requests.get(url)

        jsondata = json.loads(r.text)
        return jsondata["almanac"]
