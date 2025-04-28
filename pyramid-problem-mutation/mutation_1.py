def pyramid_volume(l, w, h):
    '''
    volume miscalculated
    '''
    v = (l*w*h/2)
    if v < 25:
        return "Baby pyramid"
    elif 25 <= v < 40:
        return "I mean, it's alright..."
    else: 
        return "That's a big pyramid!"
