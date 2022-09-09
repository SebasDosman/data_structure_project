class Menu():
    def __opcionesMenu__():
        print("Que Metodo de Ordenamiento deseas usar?")
        
        print("1. BubbleSort \n",
              "2. BubbleSort Better \n",
              "3. BubbleSort Bidirreccional \n",
              "4. InsertionSort \n",
              "5. SelectionSort \n",
              "6. QuickSort \n",
              "7. MergeSort \n",
              "8. RadixSort \n",
              "9. CountSort \n",
              "10. ShellSort \n",
              "11. BucketSort \n",
              "12. TimSort")

        opcion = int(input("Digite el numero segun la opcion: \n"))
        return opcion
    
    def __ordenamientoSeries__():
        print("\n Como deseas Organizar las Series? \n",
              "1. Por Genero \n",
              "2. Valoracion de Usuario \n")
        
        opcion = int(input("Digite el numero segun la opcion: \n"))
        return opcion
    
    def __bienvenida__():
        print("Bienvenido a Netflix \n")