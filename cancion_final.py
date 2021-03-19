# Ejemplo con la duración 
from music21 import note, stream

notes = ['A3','D4','E4','D4','A3','D4','E4','D4','A3','D4','E4','D4','A3','D4','E4','D4'] # Notas con misma duración

st = stream.Stream()

for n in notes:
  new_note = note.Note(n) 
  new_note.duration.quarterLength = 1 # Duración
  st.append(new_note)

new_note = note.Note('A2') # Nota con diferente duración
new_note.duration.quarterLength = 16 # Duración
st.append(new_note)

st.write('midi', fp = 'cancion13.mid')
