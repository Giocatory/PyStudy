def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

var1 = max(numbers, key=abs)
var2 = min(map(abs, numbers))

print(var1 + var2)