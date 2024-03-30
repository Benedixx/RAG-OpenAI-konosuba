import os
from llama_index.core.tools import FunctionTool

note_path = os.path.join('data', 'notes.txt')

def save_note(note):
    if not os.path.exists(note_path):
        os.makedirs(note_path)
    
    with open(note_path, 'a') as f:
        f.write(note + '\n')
        
    return "Note saved!"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name='note_saver',
    description='save generated text to notes.txt'
)