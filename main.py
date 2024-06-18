from config.settings import load_config
from services.tempo_analyzer import analyze_tempo
from services.style_analyzer import analyze_style
from models.lyric_generator import LyricGenerator
from models.key_signature_recommender import KeySignatureRecommender

def main():
    config = load_config()
    
    tempo = config['project_tempo']
    style = config['music_style']
    
    analyzed_tempo = analyze_tempo(tempo)
    analyzed_style = analyze_style(style)
    
    lyric_gen = LyricGenerator()
    lyrics = lyric_gen.generate(analyzed_tempo, analyzed_style)
    
    key_recommender = KeySignatureRecommender()
    key_signature = key_recommender.recommend(analyzed_style)
    
    print(f"Generated Lyrics: \n{lyrics}")
    print(f"Recommended Key Signature: {key_signature}")

if __name__ == "__main__":
    main()
