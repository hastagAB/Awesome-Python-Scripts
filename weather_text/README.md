# WeatherTextApp
Using Twilio &amp; Openweather API

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a simple Weather App that sends you a text according to the location specified. 
	
## Technologies
Project is created with:
* Twilio
* OpenWeather

	
## Setup
To run this project, git pull into a directory and run the script.
Setup a Cron job if you want it to run every Morning before you wake up, just remember to hard-code:
* Zip Code
* Region
* From Number
* To Number

```
$ python3 weatherapp.py
```
