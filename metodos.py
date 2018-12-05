class Simplex(object):
    
    def __init__(self, Z="", e1 = "", e2 = ""):

        def metodo(self):
            num=0
            n=-1
            ecuaciones=[Z, e1, e2]
            N=0
            X=0
            for i in ecuaciones[0]:
                if(i == "X" or i == "x"):
                    N=N+2#Contamos la cantidad de X y la sumamos para saber la cantidad de columnas pero hay que sumar 2 por Z y el lado derecho
                    X=X+1#Contamos la cantidad de X para saber la cantidad de variables de holgura
            N=N+2
            M=len(ecuaciones)#La longitud del vector sera la cantidad de filas
            matriz=[[0.0 for x in range(N)] for x in range(M)]
            num=0
            for E in ecuaciones:
                digito=""
                n=n+1
                for i in range(len(E)):
                    if(E[i] == "Z"):
                            matriz[n][0]=1.0
                            num=1
                    if(E[i] == "X" or E[i] == "x"):
                        matriz[n][int(E[i+1])]=float(digito)
                        num=1
                    digito=digito+E[i]
                    if(num == 1 or E[i] == "+"):
                        digito=""
                        num=0
            cont=X+1#Contador que agregara una columna mas para las variables de holgura
            for i in range (X):
                matriz[i+1][cont]=1.0
                cont=cont+1
            i=0#Contador para guardar en la ultima columna los valores que le siguen al =
            for E in ecuaciones:
                pos = E.index("=")
                matriz[i][cont]=float(E[(pos+1):])
                i=i+1
            NEWM=BusquedaPiv(matriz,N,M,X)
            return NEWM

        def BusquedaPiv(matriz,N,M,X):
            #Metodo para hallar la posicion del mas negativo
            pivo=0
            minimo=matriz[0][0]
            for t in range (N):
                if(matriz[0][t]<minimo):
                    minimo=matriz[0][t]
                    b=t
            elvalormenor=[0.0 for y in range (X)]
            for o in range (X):#la fila tendra de valor 2
                if(matriz[o+1][b]!=0):
                    elvalormenor[o]=matriz[o+1][N-1]/matriz[o+1][b]
                if(matriz[o+1][b]==0):
                    elvalormenor[o]=9999
                #la b es la columna donde encontro el valor menor
            #Metodo para saber la posicion del menor en el resultado de la divicion
            minimoP=elvalormenor[0]
            for n in range(X):
                if(elvalormenor[n]<minimoP):
                    minimoP=elvalormenor[n]
                    pivo=n
            return Simpl(matriz,pivo+1,b,N,M,X)
    

        def Simpl(matriz, pivotei,pivotej,N,M,X):
            newM=[[0.0 for x in range(N)] for x in range(M)]
            for j in range(N):
                newM[pivotei][j]=matriz[pivotei][j]/matriz[pivotei][pivotej]
            for i in range (M):
                for j in range (N):
                    if(i != pivotei):
                        if(newM[pivotei][pivotej] == matriz[i][pivotej]*-1):
                            newM[i][j]=(newM[pivotei][j])+matriz[i][j]
                            if(newM[i][j] == -0.0):
                                newM[i][j]=0.0
                        elif(newM[pivotei][pivotej] != matriz[i][pivotej]):
                            newM[i][j]=((((newM[pivotei][j]*matriz[i][pivotej])-matriz[i][j]))*-1)
                            if(newM[i][j] == -0.0):
                                newM[i][j]=0.0
            cont=0
            for i in range(M):
                if(newM[0][i]<0):
                    cont+=1
            filaterminada=cont
            if(filaterminada > 0):
                newM=BusquedaPiv(newM,N,M,X)
            return newM

        self.matriz=metodo(self)
    def resultado(self):
        return self.matriz


class Simplex1(object):
    def __init__(self, Z="", e1 = "", e2 = "", e3 = ""):

        def metodo1(self):
            num=0
            n=-1
            ecuaciones=[Z, e1, e2, e3]
            N=0
            X=0
            for i in ecuaciones[0]:
                if(i == "X" or i == "x"):
                    N=N+2#Contamos la cantidad de X y la sumamos para saber la cantidad de columnas pero hay que sumar 2 por Z y el lado derecho
                    X=X+1#Contamos la cantidad de X para saber la cantidad de variables de holgura
            N=N+2
            M=len(ecuaciones)#La longitud del vector sera la cantidad de filas
            matriz=[[0.0 for x in range(N)] for x in range(M)]
            num=0
            for E in ecuaciones:
                digito=""
                n=n+1
                for i in range(len(E)):
                    if(E[i] == "Z"):
                            matriz[n][0]=1.0
                            num=1
                    if(E[i] == "X" or E[i] == "x"):
                        matriz[n][int(E[i+1])]=float(digito)
                        num=1
                    digito=digito+E[i]
                    if(num == 1 or E[i] == "+"):
                        digito=""
                        num=0
            cont=X+1#Contador que agregara una columna mas para las variables de holgura
            for i in range (X):
                matriz[i+1][cont]=1.0
                cont=cont+1
            i=0#Contador para guardar en la ultima columna los valores que le siguen al =
            for E in ecuaciones:
                pos = E.index("=")
                matriz[i][cont]=float(E[(pos+1):])
                i=i+1
            NEWM=BusquedaPiv1(matriz,N,M,X)
            return NEWM

        def BusquedaPiv1(matriz,N,M,X):
            #Metodo para hallar la posicion del mas negativo
            pivo=0
            minimo=matriz[0][0]
            for t in range (N):
                if(matriz[0][t]<minimo):
                    minimo=matriz[0][t]
                    b=t
            elvalormenor=[0.0 for y in range (X)]
            for o in range (X):#la fila tendra de valor 2
                if(matriz[o+1][b]!=0):
                    elvalormenor[o]=matriz[o+1][N-1]/matriz[o+1][b]
                if(matriz[o+1][b]==0):
                    elvalormenor[o]=9999
                #la b es la columna donde encontro el valor menor
            #Metodo para saber la posicion del menor en el resultado de la divicion
            minimoP=elvalormenor[0]
            for n in range(X):
                if(elvalormenor[n]<minimoP):
                    minimoP=elvalormenor[n]
                    pivo=n
            return Simpl1(matriz,pivo+1,b,N,M,X)
    

        def Simpl1(matriz, pivotei,pivotej,N,M,X):
            newM=[[0.0 for x in range(N)] for x in range(M)]
            for j in range(N):
                newM[pivotei][j]=matriz[pivotei][j]/matriz[pivotei][pivotej]
            for i in range (M):
                for j in range (N):
                    if(i != pivotei):
                        if(newM[pivotei][pivotej] == matriz[i][pivotej]*-1):
                            newM[i][j]=(newM[pivotei][j])+matriz[i][j]
                            if(newM[i][j] == -0.0):
                                newM[i][j]=0.0
                        elif(newM[pivotei][pivotej] != matriz[i][pivotej]):
                            newM[i][j]=((((newM[pivotei][j]*matriz[i][pivotej])-matriz[i][j]))*-1)
                            if(newM[i][j] == -0.0):
                                newM[i][j]=0.0
            cont=0
            for i in range(M):
                if(newM[0][i]<0):
                    cont+=1
            filaterminada=cont
            if(filaterminada > 0):
                newM=BusquedaPiv1(newM,N,M,X)
            return newM

        self.matriz=metodo1(self)
    def resultado1(self):
        return self.matriz