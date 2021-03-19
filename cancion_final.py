from music21 import note, stream

#notes = ['E','D#','E','B3','D','C','A3'] # Nombre de las notas
notes = ['E','D#','E','B3','D','C'] # Notas con misma duración

st = stream.Stream()

for n in notes:
  new_note = note.Note(n) 
  new_note.duration.quarterLength = 1/2 # Duración
  st.append(new_note)

new_note = note.Note('A3') # Nota con diferente duración
new_note.duration.quarterLength = 2 # Duración
st.append(new_note)

st.write('midi', fp = 'cancion11.mid') 
