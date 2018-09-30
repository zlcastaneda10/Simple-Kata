class Estadistica:

    def dar_estadistica(self,cadena):
        if (cadena == ""):
            return [0,0,0,0]
        else:
            cantidad = 0
            numeros = cadena.split(",")

            minimo = int(numeros[0])
            maximo = int(numeros[0])
            promedio = 0.0
            for numero in numeros:

                cantidad = cantidad + 1
                promedio = float(numero)+promedio
                if (int(numero) < minimo):
                    minimo = int(numero)

                if (int(numero) > maximo):
                    maximo =int(numero)

            promedio = promedio / cantidad
            return [cantidad,int(minimo),int(maximo),promedio]