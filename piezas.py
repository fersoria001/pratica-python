#errores conocidos:
#el codigo de componente puede hacer bypass si es identico a CP
#la suma de los componentes se expresa como total y no por cada pieza
#la lista de componentes y piezas podria mostrarse de forma vertical.
#la posibilidad de ingreso es infinita hasta que se ingrese 0
PrP = []
componentes = []
piezas = []
componentes_p = []
pieza = []
number = int(input("Escriba 1 para ingresar y 0 para salir: "))
while number != 0:
  piezas.append (pieza)
  CP = int(input("id de la pieza: "))
  if CP >= 1 and CP <=99:
    valid = int(1)
  elif CP==0:
    print (f"{componentes}Precio de los componentes: $ {componentes_p} Total: ${total_comp}")
    print (f"{piezas}Precio de la pieza: ${PrP}")
    break
  else:
    valid = int(0)
  while valid == 1:       
       CC = int(input("codigo de componente: "))
       componente = str(CC)
       pieza = str(CP)
       comparo_c = componente[-2:]
       comparo_p = pieza[:3]
       if CC == 0:
         break
       while comparo_c == comparo_p:
         print("#" , CC)
         PrC= float(input("Precio del componente: "))
         if PrC >=10 and PrC <= 999.99:
           componentes.append (componente)
           componentes_p.append (PrC)
           
           total_comp = sum(componentes_p)
 
           PrP.append (total_comp)
           
           #PrC_uno = str(PrC)
          # for i in componentes:
               
           break
      








