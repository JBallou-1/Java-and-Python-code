#Pigs
#
#Jacob Ballou
#balloujm@g.cofc.edu
#csci 180
#Homework 3
#Friday, Feb 21
#play "Pigs (Three different ones), by Pink Floyd
#Sheet music from url: https://musescore.com/user/6835446/scores/3992996
#Input: none
#Output: music
from music import *
score = Score("Pigs",129)
#This part is an acoustic guitar according to the sheet music,
#but the sound isn't the same. Rock Organ is more like the original music.
orgPart = Part(ROCK_ORGAN,0)

guitarPart = Part(ELECTRIC_GUITAR,1)
bassPart = Part(BASS,2)
pianoPart = Part(PIANO,3)

orgPhrase0 = Phrase(0.0)
bassPhrase0 = Phrase(0.0)
guitarPhrase0 = Phrase(0.0)
pianoPhrase0 = Phrase(0.0)
#basic pattern for Pigs intro.
orgPitches0 =   [REST,[E6,G5],[FS6,A5],[G6,B5],[FS6,A5],[E6,G5],[FS6,A5],[G6,B5]]*2
orgDurations0 = [EN,   EN,      EN,      EN,      EN,     EN,     EN,     EN]*2

bassPitches0 =   [E4,REST,E4,REST,C4,REST,C4,B4,A4,B4,B4]
bassDurations0 = [HN,HN,  HN,HN,  HN,HN,  EN,SN,SN,SN,SN]
bassPitches1 =   [REST,B4,A4,B4,B4,REST,A4,REST,G4,F4,E4,D4,E4,REST,REST,E4]
bassDurations1 = [SN,  EN,EN,EN,EN,SN,  SN,SN,  SN,EN,EN,EN,HN,QN,  EN,  EN]
bassPitches2 =   [E4,D5,A4, A4]
bassDurations2 = [HN,QN,DQN,QN]
bassPitches3 =   [C5,C5,B4,REST,A4,G4,A4,G4,F4,G4,F4,E4, F4,D4,REST,G3,C4]
bassDurations3 = [HN,SN,SN,SN,  SN,SN,SN,SN,SN,SN,SN,DHN,SN,SN,SN,  SN,WN]

guitarPitches0 =   [REST,REST,C4]
guitarDurations0 = [WN,  HN,  HN]
guitarPitches1 =   [C4,REST,C5,C5,C5,C5]
guitarDurations1 = [HN,HN,  HN,QN,EN,EN]
guitarPitches2 =   [B4,REST,REST]
guitarDurations2 = [HN,QN,  QN]
guitarPitches3 =   [REST,C5,B4,REST,A4,REST,A4,G4,E4, REST]
guitarDurations3 = [HN,  SN,SN,SN,  SN,TN,  EN,EN,DHN,QN]

pianoPitches0 =   [REST,REST,REST,REST,B3,A3,B3,B3]
pianoDurations0 = [WN,  WN,  WN,  QN,  EN,EN,EN,EN]
#contains treble and bass notes from bar 3 to bar 5
pianoPitches1 =   [C3,B3,A3,B3,B3,REST,A3,REST,G3,FS3,E3,D3,[E3,C4],[REST,C4],[REST,C4],[E3,C4]]
pianoDurations1 = [HN,EN,EN,EN,EN,SN,  SN,SN,  SN,EN,EN,EN, HN,     QN,       EN,       EN]
#treble and bass notes from bar 5 to bar 6
pianoPitches2 =   [[B3,G3],[REST,D4],B3, [REST,B3]]
pianoDurations2 = [HN,      QN,      DQN,  QN]
#treble and bass notes from bar 6 to bar 9
pianoPitches3 =   [C4,C4,B3,REST,A3,G3,A3,G3,F3,G3,F3,E3, F3,D3,REST,G2,C3]
pianoDurations3 = [HN,SN,SN,SN,  SN,SN,SN,SN,SN,SN,SN,DHN,SN,SN,SN,  SN,WN]

orgPhrase0.addNoteList(orgPitches0,orgDurations0)
orgPhrase0.addNoteList(orgPitches0,orgDurations0)
orgPhrase0.addNoteList(orgPitches0,orgDurations0)
orgPhrase0.addNoteList(orgPitches0,orgDurations0)
orgPhrase0.addNoteList(orgPitches0,orgDurations0)

bassPhrase0.addNoteList(bassPitches0,bassDurations0)
bassPhrase0.addNoteList(bassPitches1,bassDurations1)
bassPhrase0.addNoteList(bassPitches2,bassDurations2)
bassPhrase0.addNoteList(bassPitches3,bassDurations3)

guitarPhrase0.addNoteList(guitarPitches0,guitarDurations0)
guitarPhrase0.addNoteList(guitarPitches1,guitarDurations1)
guitarPhrase0.addNoteList(guitarPitches2,guitarDurations2)
guitarPhrase0.addNoteList(guitarPitches3,guitarDurations3)

pianoPhrase0.addNoteList(pianoPitches0,pianoDurations0)
pianoPhrase0.addNoteList(pianoPitches1,pianoDurations1)
pianoPhrase0.addNoteList(pianoPitches2,pianoDurations2)
pianoPhrase0.addNoteList(pianoPitches3,pianoDurations3)

orgPart.addPhrase(orgPhrase0)
bassPart.addPhrase(bassPhrase0)
guitarPart.addPhrase(guitarPhrase0)
pianoPart.addPhrase(pianoPhrase0)

score.addPart(orgPart)
score.addPart(bassPart)
score.addPart(guitarPart)
score.addPart(pianoPart)
Play.midi(score)
