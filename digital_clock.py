mins = 170

def convert(mins):
    hours = mins//60
    secs = mins%60
    
    if secs<10:
        secs = f"0{secs}"
    print(f"{hours}:{secs}")
    
convert(mins)