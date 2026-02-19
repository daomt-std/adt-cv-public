import math

def vypocitej_preponu(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)

def prvni_zadani() -> None:
    a = 3
    b = 4
    c = vypocitej_preponu(a, b)
    print(c)

def druhe_zadani() -> None:
    data = 3,7,6,11,5,5,8,9
    prev = 0

    for value in data:
        if (value - prev) == 0:
            continue
        print(value/(value - prev))
        prev = value

def treti_zadani() -> None:
    scores = [50, 80, 45, 90, 30, 60]
    i = 0
    while i < len(scores):
        if scores[i] < 50:
            scores.pop(i)
            i-= 1
        i += 1
    print(scores)

treti_zadani()
