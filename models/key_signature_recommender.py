import json

class KeySignatureRecommender:
    def __init__(self):
        with open('data/key_signatures.json', 'r') as f:
            self.key_signatures = json.load(f)
    
    def recommend(self, style):
        return self.key_signatures.get(style, 'C Major')
