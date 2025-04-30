def pyramid_problem_mutation(l, w, h):
    '''
    spelling errors in any of the strings
    '''
    v = (l*w*h/3)
    if v < 25:
        return "Baby pyrmid"
    elif 25 <= v < 40:
        return "I mean, its alright..."
    else: 
        return "Thats a big pyramid!"
