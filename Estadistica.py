class Estadistica:

    def dar_estadistica(self,cadena):
        if (cadena == ""):
            return [0,0,0,0]
        else:
            cantidad = 0
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            maximo = minimo
            for numero in numeros:
                cantidad = cantidad + 1
                if (int(numero) < minimo):
                    minimo =numero
                if (int(numero) > maximo):
                    maximo =numero
            return [cantidad,int(minimo),int(maximo),0]