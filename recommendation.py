#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
It gives the best recomendation
Created on 27/02/2017

Using json

alba.v.lamas@gmail.com
'''

class Recommendation(object):
	recommendations = {"Rain":"Don't forget your umbrella",
					 	"Chance of a Thunderstorm":\
					 	"Don't forget your raincoat!",
					 	"Thunderstorm":\
					 	"Don't forget your raincoat!",
					 	"Snow Showers":"Wear gloves, scarf, hat, anorak...",
					 	"Clear":"Don't forget sun glasses and sunscreen",
                        "Cloudy":"Leave your sungasses at home, otherwise tou look like a fool",
				 	 	"Mostly Cloudy":"Leave your sungasses at home, otherwise tou look like a fool",
					 	"Partly Cloudy":"Wear what you want, today is your day ;)",
					 	"Chance of Rain":"Take your umbrella, just in case",
					 	}
	def recommend(self, condition):
		return Recommendation.recommendations[condition]
