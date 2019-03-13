import itertools

TOP='TOP'
LEFT='LEFT'
RIGHT='RIGHT'
BOTTOM='BOTTOM'
ELSEWHERE='ELSEWHERE'

PLACES = [TOP, LEFT, RIGHT, BOTTOM, ELSEWHERE]
EDGEPLACES = [TOP, LEFT, RIGHT, BOTTOM]

EDGES = {
    TOP:    [3, 2, 3, 4, 3, 3, 7, 5, 13, 3],
    LEFT:   [5, 2, 2, 4, 4, 6, 3, 6,  2, 3],
    RIGHT:  [3, 5, 4, 4, 3, 6, 5, 2,  2, 9],
    BOTTOM: [1, 4, 7, 4, 5, 3, 3, 2, 13, 4],
}

HEIGHT=11
WIDTH =18

PIECECOUNT = 10
assert all(len(x) == PIECECOUNT for x in EDGES.values())
