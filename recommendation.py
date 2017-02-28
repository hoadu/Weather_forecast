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
					 	"Today is not the day to hang clothes",
					 	"Thunderstorm":\
					 	"Stay at home, make popcorn and watch a good movie",
					 	"Snow Showers":"It's cold, but it's funny and beauty ;)",
					 	"Clear":"Don't forget sun glasses and sunscreen",
				 	 	"Mostly Cloudy":"Leave your sungasses at home, otherwise tou look like a fool",
					 	"Partly Cloudy":"Había alguna nuvecilla... pero ha escampao",
					 	"Chance of Rain":"Take your umbrella, just in case",
					 	}
	def recommend(self, condition):
		return Recommendation.recommendations[condition]