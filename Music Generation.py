# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Melody Section
import random
from pyknon.music import Note

duration=[1,.5,.25,.125]
octave=[3,4,6]

C_note = Note(0, 5, random.choice(duration))
D_note = Note(2, 5, random.choice(duration)) 
E_note = Note(4, 5,random.choice(duration)) 
F_note = Note(5, 5, random.choice(duration)) 
G_note = Note(7, 5, random.choice(duration)) 
A_note = Note(9, 5, random.choice(duration)) 
B_note = Note(11, 5, random.choice(duration)) 

C_Major=[C_note,D_note,E_note,F_note,G_note,A_note,B_note]

from pyknon.music import Rest

quarter_rest = Rest(0) # quarter rest

from pyknon.music import NoteSeq

# create a sequence of notes and rests
seq = NoteSeq(random.choices(C_Major,k=30)) 



from pyknon.genmidi import Midi

midi = Midi(1, tempo=120)
midi.seq_notes(seq, track=0)
midi.write("E:\Python\simple_noteseq.mid")


#Harmony Section

c = Note(0, random.choice(octave), random.choice(duration))
d = Note(2, random.choice(octave), random.choice(duration)) 
e = Note(4, random.choice(octave),random.choice(duration)) 
f = Note(5, random.choice(octave), random.choice(duration)) 
g = Note(7, random.choice(octave), random.choice(duration)) 
a = Note(9, random.choice(octave), random.choice(duration)) 
b = Note(11, random.choice(octave), random.choice(duration)) 

c_scale=[c,d,e,f,g,a,b]

seq = NoteSeq(random.choices(c_scale,k=30)) 

midi1 = Midi(1, tempo=120)
midi1.seq_notes(seq, track=0)
midi1.write("E:\Python\harmony.mid") 