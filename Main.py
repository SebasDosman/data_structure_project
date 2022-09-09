from Series import Series
from Ordenamientos import Ordenamientos
from Menus import Menu
from CalculosSeries import CalculosSeries


# <-- Instancias De Clases -->
strangerThings = Series("Stranger Things", "Accion", 4.5, 3, 5)
lucifer = Series("Lucifer", "Comedia", 3, 5, 3)
breakingBad = Series("Breaking Bad", "Ficcion", 4, 3, 64)
bettyLaFea = Series("Betty La Fea", "Romance", 2.5, 3, 10)
bobEsponja = Series("Bob Esponja", "Cartoon", 5, 4, 8)
sandMan = Series("Sand Man", "Comedia", 2.5, 6, 2)

series = [strangerThings, lucifer, breakingBad, bettyLaFea, bobEsponja, sandMan]
valoracionSeries = [strangerThings.__getValoracion__(), lucifer.__getValoracion__(), breakingBad.__getValoracion__(), bettyLaFea.__getValoracion__(), bobEsponja.__getValoracion__(), sandMan.__getValoracion__()]
generoSeries = [strangerThings.__getGenero__(), lucifer.__getGenero__(), breakingBad.__getGenero__(), bettyLaFea.__getGenero__(), bobEsponja.__getGenero__(), sandMan.__getGenero__()]
nombreSeries = [strangerThings.__getNombre__(), lucifer.__getNombre__(), breakingBad.__getNombre__(), bettyLaFea.__getNombre__(), bobEsponja.__getNombre__(), sandMan.__getNombre__()]
tempSeries = [strangerThings.__getCantTemp__(), lucifer.__getCantTemp__(), breakingBad.__getCantTemp__(), bettyLaFea.__getCantTemp__(), bobEsponja.__getCantTemp__(), sandMan.__getCantTemp__()]


ordenamiento = Ordenamientos(generoSeries)
ordenamiento2 = Ordenamientos(valoracionSeries)
calculoSeries = CalculosSeries(series)


Menu.__bienvenida__()
calculoSeries.__printSeries__()
calculoSeries.__promedioTemp__()
calculoSeries.__seriesMin__()
opcion = Menu.__opcionesMenu__()


# <-- Menu -->
while (opcion != -1):
    if (opcion == 1):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__bubbleSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__bubbleSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 2):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__bubbleSortBetter__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__bubbleSortBetter__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 3):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__bubbleSortBidirectional__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__bubbleSortBidirectional__()), "\n"
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 4):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__insertionSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__insertionSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 5):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__selectionSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__selectionSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 6):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__quickSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__quickSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 7):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__mergeSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__mergeSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 8):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__radixSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__radixSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 9):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__countSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__countSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 10):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__shellSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__shellSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 11):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__bucketSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__bucketSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 12):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            print(ordenamiento.__timSort__(), "\n")
        elif (opcion2 == 2):
            print(ordenamiento2.__timSort__(), "\n")
        
        opcion = Menu.__opcionesMenu__()