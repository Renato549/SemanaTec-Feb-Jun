# Ejemplo con la duración 
from music21 import note, chord, stream

st = stream.Stream()

notes = ['A3','D4b','E4','D4','A3','D4b','E4','D4','A3','D4b','E4','D4','A3','D4b','E4','D4'] # Notas con misma duración

for n in notes:
  new_note1 = note.Note('A2') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración
  new_note1.offset = 0 
  new_note = note.Note(n) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

notes2 = ['A3b','D4b','E4','D4b','A3b','D4b','E4','D4b','A3b','D4b','E4','D4b','A3b','D4b','E4','D4b',] # Notas con misma duración

for n2 in notes2:
  new_note1 = note.Note('D3b') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración 
  new_note1.offset = 16
  new_note = note.Note(n2) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

notes3 = ['F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b']

for n3 in notes3:
  new_note1 = note.Note('F2#') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración 
  new_note1.offset = 32
  new_note = note.Note(n3) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

notes4 = ['A3','D4','F4#','D4','A3','D4','F4#','D4','A3','D4','F4#','D4','A3','D4','F4#','D4']

for n4 in notes4:
  new_note1 = note.Note('D3') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración 
  new_note1.offset = 48
  new_note = note.Note(n4) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

la1 = note.Note('A2')
st.append(la1)
la1.duration.quarterLength = 12

mi1 = note.Note('E5')
st.append(mi1)
mi1.duration.quarterLength = 2

re1 = note.Note('D5b')
st.append(re1)
re1.duration.quarterLength = 2

si1 = note.Note('B4')
st.append(si1)
si1.duration.quarterLength = 1/2

la2 = note.Note('A4')
st.append(la2)
la2.duration.quarterLength = 4

re2 = note.Note('D3b')
st.append(re2)
re2.duration.quarterLength = 2

mi2 = note.Note('E5')
st.append(mi2)
mi2.duration.quarterLength = 1/2

mi3 = note.Note('E5')
st.append(mi3)
mi3.duration.quarterLength = 1

re3 = note.Note('D5b')
st.append(re3)
re3.duration.quarterLength = 2

rest1 = note.Rest()
st.append(rest1)
rest1.duration.quarterLength = 1/2

si2 = note.Note('B4')
st.append(si2)
si2.duration.quarterLength = 1/2

la3 = note.Note('A4')
st.append(la3)
la3.duration.quarterLength = 2

fa1 = note.Note('F2#')
st.append(fa1)
fa1.duration.quarterLength = 2

mi4 = note.Note('E5')
st.append(mi4)
mi4.duration.quarterLength = 1

mi5 = note.Note('E5')
st.append(mi5)
mi5.duration.quarterLength = 1/2

re4 = note.Note('D5b')
st.append(re4)
re4.duration.quarterLength = 2

rest2 = note.Rest()
st.append(rest2)
rest2.duration.quarterLength = 1/2

si3 = note.Note('B4')
st.append(si3)
si3.duration.quarterLength = 1/2

la4 = note.Note('A4')
st.append(la4)
la4.duration.quarterLength = 2

re5 = note.Note('D3')
st.append(re5)
re5.duration.quarterLength = 2

mi6 = note.Note('E5')
st.append(mi6)
mi6.duration.quarterLength = 1/2

mi7 = note.Note('E5')
st.append(mi7)
mi7.duration.quarterLength = 1

re6 = note.Note('D5b')
st.append(re6)
re6.duration.quarterLength = 2

si4 = note.Note('B4')
st.append(si4)
si4.duration.quarterLength = 2

la5 = note.Note('A4')
st.append(la5)
la5.duration.quarterLength = 1/2

la6 = note.Note('A2')
st.append(la6)
la6.duration.quarterLength = 2

mi8 = note.Note('E5')
st.append(mi8)
mi8.duration.quarterLength = 1

re7 = note.Note('D5b')
st.append(re7)
re7.duration.quarterLength = 1

si5 = note.Note('B4')
st.append(si5)
si5.duration.quarterLength = 1/2

la7 = note.Note('A4')
st.append(la7)
la7.duration.quarterLength = 2

chord1 = chord.Chord(['D3b','F5#'])
st.append(chord1)
chord1.duration.quarterLength = 2

re8 = note.Note('D5b')
st.append(re8)
re8.duration.quarterLength = 2

la8 = note.Note('A4')
st.append(la8)
la8.duration.quarterLength = 2

rest3 = note.Rest()
st.append(rest3)
rest3.duration.quarterLength = 1/2

si6 = note.Note('B4')
st.append(si6)
si6.duration.quarterLength = 1

la9 = note.Note('A4')
st.append(la9)
la9.duration.quarterLength = 1/2

chord2 = chord.Chord(['F2#','B4'])
st.append(chord2)
chord2.duration.quarterLength = 1

fa2 = note.Note('F4#')
st.append(fa2)
fa2.duration.quarterLength = 1/2

la10 = note.Note('A4')
st.append(la10)
la10.duration.quarterLength = 4

mi9 = note.Note('E4')
st.append(mi9)
mi9.duration.quarterLength = 1/2

mi10 = note.Note('E4')
st.append(mi10)
mi10.duration.quarterLength = 1/2

fa3 = note.Note('F4#')
st.append(fa3)
fa3.duration.quarterLength = 1/2

chord3 = chord.Chord(['D3','B4'])
st.append(chord3)
chord3.duration.quarterLength = 1/2

la11 = note.Note('A4')
st.append(la11)
la11.duration.quarterLength = 1/2

si7 = note.Note('B4')
st.append(si7)
si7.duration.quarterLength = 1

re9 = note.Note('D5b')
st.append(re9)
re9.duration.quarterLength = 4

rest4 = note.Rest()
st.append(rest4)
rest4.duration.quarterLength = 2

mi11 = note.Note('E4')
st.append(mi11)
mi11.duration.quarterLength = 1/2

chord3 = chord.Chord(['E3','B4'])
st.append(chord3)
chord3.duration.quarterLength = 1/2

re10 = note.Note('D5b')
st.append(re10)
re10.duration.quarterLength = 1/2

re11 = note.Note('D5b')
st.append(re11)
re11.duration.quarterLength = 1/2

re12 = note.Note('D5b')
st.append(re12)
re12.duration.quarterLength = 1

si8 = note.Note('B4')
st.append(si8)
si8.duration.quarterLength = 1/2

si9 = note.Note('B4')
st.append(si9)
si9.duration.quarterLength = 1/2

la12 = note.Note('A4')
st.append(la12)
la12.duration.quarterLength = 1/2

chord4 = chord.Chord(['F3#','B4'])
st.append(chord4)
chord4.duration.quarterLength = 1

si10 = note.Note('B4')
st.append(si10)
si10.duration.quarterLength = 1/2

la13 = note.Note('A4')
st.append(la13)
la13.duration.quarterLength = 1/2

si11 = note.Note('B4')
st.append(si11)
si11.duration.quarterLength = 1/2

la14 = note.Note('A4')
st.append(la14)
la14.duration.quarterLength = 1/2

la15 = note.Note('A4')
st.append(la15)
la15.duration.quarterLength = 1/2

la16 = note.Note('A4')
st.append(la16)
la16.duration.quarterLength = 1

chord5 = chord.Chord(['D3','A4'])
st.append(chord5)
chord5.duration.quarterLength = 1/2

si12 = note.Note('B4')
st.append(si12)
si12.duration.quarterLength = 1/2

la17 = note.Note('A4')
st.append(la17)
la17.duration.quarterLength = 1/2

si13 = note.Note('B4')
st.append(si13)
si13.duration.quarterLength = 1/2

la18 = note.Note('A4')
st.append(la18)
la18.duration.quarterLength = 1/2

si14 = note.Note('B4')
st.append(si14)
si14.duration.quarterLength = 2

chord6 = chord.Chord(['D3','A4'])
st.append(chord6)
chord6.duration.quarterLength = 1/2

si15 = note.Note('B4')
st.append(si15)
si15.duration.quarterLength = 1/2

la19 = note.Note('A4')
st.append(la19)
la19.duration.quarterLength = 1/2

si16 = note.Note('B4')
st.append(si16)
si16.duration.quarterLength = 1/2

la20 = note.Note('A4')
st.append(la20)
la20.duration.quarterLength = 1/2

la21 = note.Note('A4')
st.append(la21)
la21.duration.quarterLength = 1





st.write('midi', fp = 'cancion37.mid')