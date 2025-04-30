def pyramid_problem_mutation(l, w, h):
    '''
    boolean operation inversed (> instead of <)
    '''
    v = (l*w*h/3)
    if v > 25:
        return "Baby pyramid"
    elif 25 <= v < 40:
        return "I mean, it's alright..."
    else: 
        return "That's a big pyramid!"
