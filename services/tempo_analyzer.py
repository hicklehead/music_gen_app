def analyze_tempo(tempo):
    # Simple analysis logic; can be extended
    if tempo < 60 or tempo > 200:
        raise ValueError("Tempo should be between 60 and 200 BPM")
    return tempo
