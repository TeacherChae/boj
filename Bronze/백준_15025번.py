#Judging Moose
l, r = map(int, input().split())
if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print("Even", str(l+r))
else:
    odd = 2*max(l,r)
    print("Odd", str(odd))

