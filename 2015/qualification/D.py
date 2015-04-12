for x in range(1, int(input()) + 1):
    X, R, C = map(int, input().split())
    area, mini = R * C, min(R, C)
    gabriel = area % X == 0 and \
              (X == 1 or
               X == 2 or
               X == 3 and mini >= 2 or
               X == 4 and mini >= 3 or
               X == 5 and mini >= 3 and area > 15 or
               X == 6 and mini >= 4)
    print('Case #{}: {}'.format(x, 'GABRIEL' if gabriel else 'RICHARD'))
