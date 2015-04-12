'''
Problem statement:
https://code.google.com/codejam/contest/6224486/dashboard#s=p3

Explanation for my solution:
For X>7, Richard can use an X-omino with a hole, so Gabriel can only win X<7.
In all cases, Gabriel needs the area to be divisible by X. Furthermore:
- For X=3, a 1-stripe won't do because Richard could use the L-shape.
- For X=4, a 2-stripe won't do because Richard could use the T-shape.
- For X=5, a 2-stripe won't do because Richard could use the W-shape.
  The W-shape also beats a 5*3 grid.
- For X=6, a 3-stripe won't do because Richard could use the T-shape
  that's a horizontal four cells plus vertical two cells under it.
You can check that in all larger grids, Gabriel indeed wins.
Possible pieces:
http://en.wikipedia.org/wiki/Pentomino
http://en.wikipedia.org/wiki/Hexomino
'''

for x in range(1, int(input()) + 1):
    X, R, C = map(int, input().split())
    area, mini = R * C, min(R, C)
    gabriel = area % X == 0 and \
              (X <= 2 or
               X == 3 and mini > 1 or
               X == 4 and mini > 2 or
               X == 5 and mini > 2 and area > 15 or
               X == 6 and mini > 3)
    print('Case #{}: {}'.format(x, 'GABRIEL' if gabriel else 'RICHARD'))
