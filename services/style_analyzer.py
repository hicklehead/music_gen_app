import json

def analyze_style(style):
    with open('data/music_styles.json', 'r') as f:
        music_styles = json.load(f)
    
    if style not in music_styles:
        raise ValueError(f"Unknown music style: {style}")
    
    return music_styles[style]
