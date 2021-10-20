#Symphony in the key of YTP
#
#Jacob Ballou
#balloujm@g.cofc.edu
#csci 180
#Homework 4
#Monday, March 9
#A glorified soundboard for a "live coding" assignment.
#Unlike most assignments, this is not meant to be played all the way through.
#I can execute the code line by line, instead of continuously.
from music import *

#Sound files:
#Godleftmeunfinished.wav
#Source: https://www.youtube.com/watch?v=Hv1mXXzZPMU
godLeftMe = AudioSample("Godleftmeunfinished.wav",G4)
#AMANHASFALLENINTOTHERIVERINLEGOCITY.wav
#Source: https://www.youtube.com/watch?v=vQWAvuTAV0E
legoCity = AudioSample("AMANHASFALLENINTOTHERIVERINLEGOCITY.wav",D4)
#FlexTape.wav
#Source: https://www.youtube.com/watch?v=Td5Oa3vj0nU
flexTape = AudioSample("FlexTape.wav",E4)
#PhilSwift.wav
#Source: https://www.youtube.com/watch?v=rSMJ-fn3PSE
philSwift = AudioSample("PhilSwift.wav",F4)
#MormonJebus.wav
#Source: https://www.youtube.com/watch?v=46PXaJxzuDE
mormonJebus = AudioSample("MormonJebus.wav",G4)
#SWOOCE.wav
#Source: https://www.youtube.com/watch?v=fMERkOR5d4c
swooce = AudioSample("SWOOCE.wav",A4)


#Start of live programming section
#God Left Me Unfinished
godLeftMe.loop(-1,0,-1)
godLeftMe.pause()
godLeftMe.resume()
godLeftMe.setPitch(G4)
#Lego City
legoCity.loop(1,0,-1)
legoCity.pause()
legoCity.resume()
legoCity.setPitch(A4)
#Flex Tape
flexTape.loop(-1,0,-1)
flexTape.pause()
flexTape.resume()
flexTape.setPitch(A4)
#Phil Swift
philSwift.loop(-1,0,-1)
philSwift.pause()
philSwift.resume()
philSwift.setPitch(A4)
#Mormon Jesus/M.C.Hammer remix
mormonJebus.loop(-1,0,-1)
mormonJebus.pause()
mormonJebus.resume()
mormonJebus.setPitch(A4)
#Swooce
swooce.loop(-1,0,-1)
swooce.pause()
swooce.resume()
swooce.setPitch(A4)