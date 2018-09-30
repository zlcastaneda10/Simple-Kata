class Estadistica:

    def dar_estadistica(self,cadena):
        if (cadena == ""):
            return [0,0,0,0]
        else:
            cantidad = 0
            numeros = cadena.split(",")

            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for numero in numeros:

                cantidad = cantidad + 1
                if (int(numero) < minimo):
                    minimo = int(numero)

                if (int(numero) > maximo):
                    maximo =int(numero)


            return [cantidad,int(minimo),int(maximo),0]