state = True
while(state):
    
    binaryNum = input("Ingrese su numero de 16 bits: ")
    binaryList = binaryNum[::]
    sgnList = binaryNum[0]
    expList = binaryNum[1:8]
    manList = binaryNum[9:16]
    
    if(len(binaryNum)> 16 or len(binaryNum)< 16):
        print("INGRESE 16 NUMEROS")
        
    else:     
        print("--------------------------------------------------")
        print("Numero Binario: ",binaryNum)
        print("Signo: ",sgnList)
        print("Exponente: ",expList)
        print("Mantisa: ",manList)
        print("--------------------------------------------------")
        print("TRADUCCION")
        
        #Evaluadores de Signo
        
        if(int(binaryNum[0]) == 1):
            sgn = "-"
            print("Signo: ", sgn)
            
        elif(int(binaryNum[0]) == 0):
            sgn = "+"
            print("Signo: ", sgn)
        
        #Evaluadores de Exponente
            
        j = 0
        k = 0
        
        while j < len(expList):
            if int(expList[j]) == 1:
                k += int(expList[j])*pow(2,j)
            j += 1
            exp = k-127
        
        print("Exponente: ",exp)
        
        #Evaluador Mantisa
        
        m = 0
        n = 0
        
        for i in range(len(manList)):
            if int(manList[m]) == 1:
                n += int(manList[m])*pow(2, -i)
            m += 1
            
        print("Mantisa: ",n)
        
        dec = n*pow(2, exp)
        
        print("Numero Decimal: ", sgn,dec)
        
        msg = input("Escriba 'cls' si desea finalizar el programa o presione enter si desea continuar: ")
        
        if msg == "cls":
            state = False
            print("FIN DEL PROGRAMA")
        
        print("--------------------------------------------------")
            
    
        
    
    
    
        

    
        
    
    




    

    


        


    
