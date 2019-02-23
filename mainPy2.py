import math
menu=input("Digite //1// para sumar 2 numeros o digite //2// para calcular potencia y raiz")
if menu=="1":
    print("Digite dos numeros para calcular el producto de la multilicación entre ellos, Pls que sean enteros")
    a=int(input("Digite un numero"))
    c=int(input("Digite un numero para multiplicarlo con el numero anterirormente digitado"))
    lel=a*c 
    doble=a*2
    print("El producto de la multiplicación de",a,"y",c,"es",lel,"y el doble del numero",a,"es",doble)
elif menu=="2":
    lul=input("Aqui digite //1// para calcular la potencia de un numero, digite //2// para calcular raiz de un numero")
    if lul=="1":
        xD=int(input("Digite un numero para calcular su potencia al cuadrado"))
        maincra=xD^2
        print("La potencia de",xD,"es",maincra)
    elif lul=="2":
        f=int(input("Digite un numero para hallarle la raiz cuadrada"))
        lmao= math.sqrt(f)
        print("La raiz cuadrada es:",lmao)