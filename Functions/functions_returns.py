def hypotenuse(p,b):
    hyp = (p**2 + b**2) ** .5
    return hyp
ans = hypotenuse(3,4)
print("Answer",ans)
out = hypotenuse(10,10) + hypotenuse(4,5) * 5
print(out)