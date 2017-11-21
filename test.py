def hanoi(level, _from, _pass, _to):
    if level == 1:
        print(_from + "->" + _to)
    else:
        hanoi(level - 1, _from, _to, _pass)
        print(_from + "->" + _to)
        hanoi(level - 1, _pass, _from, _to)


hanoi(10, "A", "B", "C")
