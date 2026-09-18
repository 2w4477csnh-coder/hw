v=int(input('вес'))
r=int(input('рост'))
v1=v*0.45359237
r1=r*0.0254
i=v1/(r1**2)
print(round(i, 2))