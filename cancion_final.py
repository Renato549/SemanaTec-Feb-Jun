# Ejemplo con la duración 
from music21 import note, stream, chord

st = stream.Stream()

notes = ['A3','D4','E4','D4','A3','D4','E4','D4','A3','D4','E4','D4','A3','D4','E4','D4'] # Notas con misma duración

for n in notes:
  new_note1 = note.Note('A2') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración
  new_note1.offset = 0 
  new_note = note.Note(n) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

notes2 = ['A2','D4','E4','D4','A2','D4','E4','D4','A2','D4','E4','D4','A2','D4','E4','D4'] # Notas con misma duración

for n2 in notes2:
  new_note1 = note.Note('D3') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración 
  new_note1.offset = 16
  new_note = note.Note(n2) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

notes3 = ['F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b','F3#','D4b','F4#','D4b']

for n3 in notes3:
  new_note1 = note.Note('F2#') # Nota con diferente duración
  new_note1.duration.quarterLength = 16 # Duración 
  new_note1.offset = 16
  new_note = note.Note(n3) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

st.write('midi', fp = 'cancion28.mid')