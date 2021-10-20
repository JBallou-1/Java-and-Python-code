#Processing power over time
#
#Jacob Ballou
#balloujm@g.cofc.edu
#csci 180
#Homework 5
#Wednesday April 1
#this program sonifies computing power over time. This information was sourced from the wikipedia list of vacuum tube computers
#and an infographic on Moore's law. The information is important because it shows a trend where processing power becomes exponentially
#greater over time. While quantum mechanical effects prevent the miniaturization of transistors beyond a certain point, other forms of
#computation are possible, which allow for even more processing power.
from music import *
from math import *
#vacuum tube computers
tubeNum = [280,1600,2300,5000,9800,25000,49000]
#time that computer was constructed
compTime = [1942,1943,1950,1951,1954,1956,1958]
#convert number of tubes into musical scale
minTubeNum = min(tubeNum)
maxTubeNum = max(tubeNum)
i = 0
for i in range(len(tubeNum)):
   tubeNum[i] = mapScale(tubeNum[i],minTubeNum,maxTubeNum,30,60)
#convert compTime into note lengths
#get length of list
compTimeLen = len(compTime)
#copy list so that the subtract operation can use the original values.
origVals1 = compTime [:]
#loop from the second index to the end
for i in range(1,compTimeLen):
   #subtract previous value from current value
   compTime[i] = origVals1[i]-origVals1[i-1]
compTime[0] = 1
#now, compTime is a list of integers ranging from 1 to 7. This is perfect for note durations, ranging from QN to 1 3/4 notes.
#transistor computers
transistorNum = [3500,  29000,134000,3100000,28000000,42000000,291000000,731000000]
#size in nanometers
transistorSize = [10000, 3000,  1500,    350,     180,      65,       45,       32]
#time that the processor was released
processorTime = [1974,   1979,  1982,   1993,    1999,    2001,     2006,     2008]
#convert number of transistors into musical scale
minTransistorNum = min(transistorNum)
maxTransistorNum = max(transistorNum)
for i in range(len(transistorNum)):
   transistorNum[i] = mapScale(transistorNum[i],minTransistorNum,maxTransistorNum,60,100)
#convert transistor size into volume, ranging from 80 to 127
minTransistorSize = min(transistorSize)
maxTransistorSize = max(transistorSize)
for i in range(len(transistorSize)):
   transistorSize[i] = mapValue(transistorSize[i],minTransistorSize,maxTransistorSize,80,127)
   #make volume discreet
   transistorSize[i] = int(transistorSize[i])
#convert processorTime into note lengths
#get length of list
procTimeLen = len(processorTime)
#copy list so subtract operation uses original numbers
origVals2 = processorTime [:]
#loop from the second index to the end
for i in range(1,procTimeLen):
   #subtract previous value from current value
   processorTime[i] = origVals2[i]-origVals2[i-1]
processorTime[0] = 1
#now, processorTime is a list of integers ranging from 2 to 8. This is a bit high for note durations, but still works.
#turn data into music
#create score with 60 bpm
score = Score(60.0)
#sonify tubeNum and compTime
vacPart = Part(ACOUSTIC_BASS,0)
vacPhrase = Phrase(0.0)
vacPhrase.addNoteList(tubeNum,compTime)
vacPart.addPhrase(vacPhrase)
#sonify transPart, processorTime, and transistorSize
transPart = Part(GUITAR,1)
transPhrase = Phrase(16.0)
transPhrase.addNoteList(transistorNum,processorTime,transistorSize)
transPart.addPhrase(transPhrase)
score.addPart(vacPart)
score.addPart(transPart)
Play.midi(score)
View.notation(score)