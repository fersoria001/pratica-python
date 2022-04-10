#errores conocidos:
#el codigo de componente puede hacer bypass si es identico a CP
#la lista de componentes y piezas podria mostrarse de forma mas ordenada.
#la posibilidad de ingreso es infinita hasta que se ingrese 0
total = []
piezas_p= []
PrP = []
componentes = []
piezas = []
componentes_p = []
pieza = []
comps = []
number = int(input("Escriba 1 para ingresar y 0 para salir: "))
while number != 0:
  piezas.append (pieza)
  comps.append (componentes_p)
  PrP = sum(componentes_p)
  piezas_p.append (PrP)
  total = sum(piezas_p)
  componentes_p = []
  PrP = []
  CP = int(input("id de la pieza: "))
  if CP >= 1 and CP <=99:
    valid = int(1)
  elif CP==0:
    print(f"Precio individual de cada componente en $ {comps}")
    print(f"Codigo de los componetes ingresados {componentes}")
    print(f"Codigo de Pieza               {piezas}")
    print(f"Precio individual de cada pieza en ${piezas_p}")
    print(f"Suma total de las piezas ${total}")
    break
  else:
    valid = int(0)
    print("Ingrese un codigo de pieza valido")
  while valid == 1: 
             
       CC = int(input("codigo de componente: "))
       componente = str(CC)
       pieza = str(CP)
       comparo_c = componente[-2:]
       comparo_p = pieza[:3]
       if CC == 0:
         break
       elif comparo_c != comparo_p:
         print("Ingrese un codigo de comoponente valido") 
       while comparo_c == comparo_p:
         print("#" , CC)
         PrC= float(input("Precio del componente: "))
         if PrC >=10 and PrC <= 999.99:
           componentes.append (componente)
           componentes_p.append (PrC)    
           break
      








