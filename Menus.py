class Menu():
    def __opcionesMenu__():
        print("Que Metodo de Ordenamiento deseas usar?")
        
        print("1. BubbleSort \n",
              "2. BubbleSort Better \n",
              "3. BubbleSort Bidirreccional \n",
              "4. InsertionSort \n",
              "5. SelectionSort \n",
              "6. ShellSort \n", 
              "-1. Salir")

        opcion = int(input("Digite el numero segun la opcion: \n"))
        return opcion
    
    def __opcionesMenuReq__():
        print("Que requerimientos desea ver?")
        
        print("1. Informacion de la serie Stranger Things \n",
              "2. Serie con mayor cant. de temporadas y capitulos \n",
              "3. Cant. de series disponibles y promedio de temporadas \n",
              "4. Promedio de cap. de la serie Breaking Bad \n",
              "5. Top 5 de series con mejor valoracion \n",
              "6. Series con 3 o menos temporadas")
        
        opcion = int(input("Digite el numero segun la opcion: \n"))
        return opcion
    
    def __ordenamientoSeries__():
        print("\n Como deseas Organizar las Series? \n",
              "1. Por Genero \n",
              "2. Valoracion de Usuario")
        
        opcion = int(input("Digite el numero segun la opcion: \n"))
        return opcion
    
    def __bienvenida__():
        print("Bienvenido a Netflix \n")