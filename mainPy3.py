import math
print("Por favor digite su ecuación cuadratica de la forma= ax^2+bx+c")
a=int(input("Digite el numero a"))
b=int(input("Digite el numero b"))
c=int(input("Digite el numero c"))
lel=b^2
lal=a*c   
xD=4*lal
lul= lel-xD
d= math.sqrt(lul)
if d>0:
    xd= math.sqrt(d)
    lmao= xd-b
    jua= 2*a
    x1= lmao/jua
    lawea= b + xd
    x2= lawea/jua
    print("Las dos respuestas son:")
    print("x1=",x1)
    print("x2=",x2)
elif d==0:
    print("entonces se tienen que x1 y x2 son iguales y corresponden")
elif d<0:
    print("No existe solución en los numeros reales")

