def heartrate(fc):
    """
    Returns your type of cardiovascular train based on inputed BPM
    args: Int BPM
    """
    if 50 <= fc <= 79:
        return "treino aeróbico"
    elif 80 <= fc <= 99:
        return "treino cardiovascular"
    elif 100 <= fc <= 119:
        return "treino anaeróbico ideal"
    elif 120 <= fc <= 140:
        return "treino anaeróbico"
    else:
        return "Outro tipo"

bpm = int(input("Insira o seu número de bpm: "))
print(heartrate(bpm))