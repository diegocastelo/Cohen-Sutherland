import consts as c


def calc_code(x, y):
    code = c.IN
    if x < c.X_MIN:
        code |= c.LEFT
    elif x > c.X_MAX:
        code |= c.RIGHT
    elif y < c.Y_MIN:
        code |= c.BOTTOM
    elif y > c.Y_MAX:
        code |= c.TOP
    return code


def cohen_sutherland(x1: int, y1: int, x2: int, y2: int):
    code1 = calc_code(x1, y1)
    code2 = calc_code(x2, y2)
    inside = False  # Variável que controla se a reta é aceita

    while True:
        if code1 == 0 and code2 == 0:
            inside = True
            break
        elif code1 & code2 != 0:
            break
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & c.TOP:
                x = x1 + (x2 - x1) * (c.Y_MAX - y1) / (y2 - y1)
                y = c.Y_MAX
            elif code_out & c.BOTTOM:  # Abaixo da janela
                x = x1 + (x2 - x1) * (c.Y_MIN - y1) / (y2 - y1)
                y = c.Y_MIN
            elif code_out & c.RIGHT:  # À direita da janela
                y = y1 + (y2 - y1) * (c.X_MAX - x1) / (x2 - x1)
                x = c.X_MAX
            elif code_out & c.LEFT:  # À esquerda da janela
                y = y1 + (y2 - y1) * (c.X_MIN - x1) / (x2 - x1)
                x = c.X_MIN

            if code_out == code1:
                x1, y1 = x, y
                code1 = calc_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = calc_code(x2, y2)

    if inside:
        return f"Parte da reta que está dentro da janela: ({int(x1)}, {int(y1)}) até ({int(x2)}, {int(y2)})"
    else:
        return "Reta completamente fora da janela"
