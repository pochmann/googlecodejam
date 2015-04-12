for x in range(input()):
 X,R,C=map(int,raw_input().split())
 print'Case #%d: %s'%(x+1,['RICHARD','GABRIEL'][R*C%X<(X<7)&(R>X-2-X/5<C)&(R*C>X/5*15)])
