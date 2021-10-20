from music import *
tempInF = input("Enter the temperature in Fahrenheit, from 0 to 127 degrees.")
tempInF = int(tempInF)
wSpeed = input("Enter wind speed in MPH")
wDirection = input("Enter the wind direction (From 0.0 to 1.0).")
note = Note(tempInF, wSpeed, 127, wDirection)
Play.midi(note)
print(tempInF,wSpeed,wDirection,)