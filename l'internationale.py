#l'Internationale.py
#Jacob Ballou
#Balloujm@g.cofc.edu
#CSCI 180
#Homework 2
#2/10/20
#Plays the leftist anthem, L'Internationale
#Input: none
#Output: sound
from music import *
#Used addNoteList to save space
pitches1 =   [D4,G4,FS4,A4,G4,D4,B3,E4,C4,E4,A4,G4,FS4,E4,D4,C4,B3,REST,D4]
durations1 = [EN,DQN,EN,EN,EN,EN,EN,HN,DQN,EN,DQN,EN,EN,EN,EN,EN,HN,QN,QN]

pitches2 =   [G4,FS4,A4,G4,D4,B3,E4,C4,A4,G4,FS4,A4,C5,FS4,G4,REST,B4,A4]
durations2 = [DQN,EN,EN,EN,EN,EN,HN,QN,EN,EN,QN,QN,QN,QN,HN,QN,EN,EN]

pitches3 =   [FS4,E4,FS4,G4,E4,FS4,D4,CS4,D4,E4,A3,A4,G4,FS4,REST,REST,A4]
durations3 = [HN,EN,EN,EN,EN,HN,QN,EN,EN,DQN,EN,DQN,EN,HN,QN,EN,EN]

pitches4 =   [A4,FS4,D4,D4,CS4,D4,B4,G4,G4,FS4,E4,FS4,A4,G4,E4,D4,REST,REST]
durations4 = [DQN,EN,EN,EN,EN,EN,HN,EN,EN,EN,EN,QN,QN,QN,QN,QN,QN,QN]

music = Phrase()   

music.addNoteList(pitches1, durations1)
music.addNoteList(pitches2, durations2)
music.addNoteList(pitches3, durations3)
music.addNoteList(pitches4, durations4)

Play.midi(music)