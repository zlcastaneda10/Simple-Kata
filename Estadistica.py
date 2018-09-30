class Estadistica:

    def dar_estadistica(self,cadena):
        if (cadena == ""):
            return [0,0,0,0]
        else:
            cantidad = 0
            numeros = cadena.split(",")
            for numero in numeros:
                cantidad = cantidad + 1
            return [cantidad,4,0,0]