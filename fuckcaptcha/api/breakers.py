import math
from random import random


def get_location(tile):
    return [
        (tile % 3) * 100 + (tile % 3) * 3 + 3 + 10 + math.floor(random() * 80),
        math.floor(tile / 3) * 100 + math.floor(tile / 3) * 3 + 3 + 10 + math.floor(random() * 80),
    ]


def fix_answer(method, c):
    if 'method_1' in method:
        return {'x': c[1], 'y': c[0]}
    elif 'method_2' in method:
        return {'x': c[0], 'y': (c[1] + c[0]) * c[0]}
    elif 'method_3' in method:
        return {'x': c[0], 'b': c[1]}
    elif 'method_4' in method:
        return [c[0], c[1]]
    elif 'method_5' in method:
        return [math.sqrt(c[1]), math.sqrt(c[0])]
    else:
        return {
            'px': round(c[0] / 300, 2),
            'py': round(c[1] / 200, 2),
            'x': c[0],
            'y': c[1],
        }
