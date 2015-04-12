for x in range(input()):
 S=map(int,raw_input().split()[1])
 print'Case #%d: %d'%(x+1,max(i-sum(S[:i])for i,m in enumerate(S)if m))
