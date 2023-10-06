import textwrap

def wrap(string, max_width):
    n = len(string)
    
    S = ""
    for i in range(0, n, max_width):
        S += string[i:i+max_width] + "\n"
    
    return S
