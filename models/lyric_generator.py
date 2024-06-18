import json

class LyricGenerator:
    def __init__(self):
        with open('data/lyrics_templates.json', 'r') as f:
            self.templates = json.load(f)
    
    def generate(self, tempo, style):
        template = self.templates.get(style, self.templates['default'])
        # Logic to adjust template based on tempo
        return template.format(tempo=tempo, style=style)
