def calculo (x, y):
    if not str(x).isdigit() or  not str(y).isdigit() :
        return 'not number'
    result = x*y
    return result