def rgb(amplitude, max_value):
    n = abs(amplitude) / max_value
    n *= 3 

    if n >= 3:
        r = 1
        g = 1
        b = 1
    elif n >= 2:
        r = 1
        g = 1
        b = n - 2
    elif n >= 1:
        r = 1
        g = n - 1
        b = 0
    else:
        r = n
        g = 0
        b = 0

    print(f"amplitude: {amplitude}, max_value: {max_value}, n: {n}, r: {r}, g: {g}, b: {b}")
    return r, g, b