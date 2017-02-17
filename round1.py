def round1(x):
    y = str(x + 0.5)
    point = y.find('.')
    return y[:point]

