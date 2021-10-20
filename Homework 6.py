#L.H.O.O.Q.
#
#Jacob Ballou
#balloujm@g.cofc.edu
#csci 180
#Homework 6
#Wednesday 4/15/2020
#Create a graphical reproduction of Duchamp's 1919 L.H.O.O.Q.
#Duchamp lived from 
#28 July 1887 to 2 October 1968.
#https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Marcel_Duchamp%2C_1919%2C_L.H.O.O.Q.jpg/465px-Marcel_Duchamp%2C_1919%2C_L.H.O.O.Q.jpg
from gui import *
d = Display("",600,550,200,200)
#Element 1
monaLisa = Icon("mona_lisa_portrait_painting_postcard-rf7df6556aaaa4c11ba3cd09453be794d_vgbaq_8byvr_540.jpg")
d.add(monaLisa)
#Goatee contains elements 2-8
gline1 = Line(248,210,240,181,Color.BLACK,3)
gline2 = Line(248,210,244,183,Color.BLACK,3)
gline3 = Line(248,210,246,182,Color.BLACK,3)
gline4 = Line(248,210,248,182,Color.BLACK,3)
gline5 = Line(248,210,250,183,Color.BLACK,3)
gline6 = Line(248,210,252,183,Color.BLACK,3)
gline7 = Line(248,210,254,180,Color.BLACK,3)
d.add(gline1)
d.add(gline2)
d.add(gline3)
d.add(gline4)
d.add(gline5)
d.add(gline6)
d.add(gline7)
#Moustache contains elements 9-12
marc1 = Arc(252,186,268,170,45,135,Color.BLACK,False,5)
marc2 = Arc(239,186,227,170,45,135,Color.BLACK,False,5)
marc3 = Arc(268,170,283,178,-45,-135,Color.BLACK,False,3)
marc4 = Arc(227,170,218,178,-45,-135,Color.BLACK,False,3)
d.add(marc1)
d.add(marc2)
d.add(marc3)
d.add(marc4)
#Label is the 13th element.
label1 = Label("L. H. O. O. Q.")
d.add(label1,240,520)
