#calculadora
def preguntaNumero():
  n=float(input("Numero1? "))
  return n

salir=False
opc=0
x=0
y=0
while (salir==False):
  opc=int(input("CALCULADORA. Elija opcion 1:+,2:-,3:*,4:/,5:salir :"))
  if (opc==1):
    x=preguntaNumero()
    y=preguntaNumero()
    print("la suma es "+ str(round(x+y,2)))
  elif (opc==2):
    x=preguntaNumero()
    y=preguntaNumero()
    print("la resta es "+ str(round(x-y,2)))
  elif (opc==3):
    x=preguntaNumero()
    y=preguntaNumero()
    print("la multip es "+ str(round(x*y,2)))
  elif (opc==4):
    x=preguntaNumero()
    y=preguntaNumero()
    print("la division es "+ str(round(x/y,2)))
  elif (opc==5):
    salir=True
    print("Gracias y adios")
  else:
    print("Opcion incorrecta")



