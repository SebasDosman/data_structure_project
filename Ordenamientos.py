class Ordenamientos():
    list = []
    MIN_MERGE = 32
    
    def __init__(self, list):
        self.list = list
    
    
    # <-- BubbleSort -->
    def __bubbleSort__(self):
        for i in range(0, len(self.list) - 1):
            for j in range(0, len(self.list) - i - 1):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
        return self.list
    
    
    # <-- Bubble Sort Better -->
    def __bubbleSortBetter__(self):
        i = 0
        control = True
        
        while (i <= len(self.list) - 2) and control:
            control = False
            
            for j in range(0, len(self.list) - i - 1):
                if (self.list[j] > self.list[j + 1]):
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
                    
                    control = True
            i += 1
        return self.list
    
    
    # <-- Bubble Sort Bidirectional -->
    def __bubbleSortBidirectional__(self):
        left = 0
        right = len(self.list) - 1
        control = True
        
        while (left < right) and control:
            control = False
            
            for i in range(left, right):
                if (self.list[i] > self.list[i + 1]):
                    control = True
                    
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
            right -= 1
            
            for j in range(right, left, -1):
                if (self.list[j] < self.list[j - 1]):
                    control = True
                    
                    self.list[j], self.list[j - 1] = self.list[j - 1], self.list[j]
            left += 1
        return self.list
    
    
    # <-- Insertion Sort -->
    def __insertionSort__(self):
        for i in range(1, len(self.list) + 1):
            k = i - 1
        
        while (k > 0) and (self.list[k] < self.list[k - 1]):
            self.list[k], self.list[k - 1] = self.list[k - 1], self.list[k]
            k -= 1
        return self.list
    
    
    # <-- Selection Sort -->
    def __selectionSort__(self):
        for i in range(0, len(self.list) - 1):
            minimal = i
        
        for j in range(i + 1, len(self.list)):
            if(self.list[j] < self.list[minimal]):
                minimal = j    
        self.list[i], self.list[minimal] = self.list[minimal], self.list[i]
        return self.list
    
    
    # <-- Shell Sort -->
    def __shellSort__(self):
        interval = len(self.list) // 2
    
        while interval > 0:
            for i in range(interval, len(self.list)):
                temp = self.list[i]
                j = i
                
                while j >= interval and self.list[j - interval] > temp:
                    self.list[j] = self.list[j - interval]
                    j -= interval
                self.list[j] = temp
            interval //= 2
        return self.list
    
    
    # <-- Busqueda Binaria -->
    def __binaria__(list, found):
        position = -1
        first = 0
        last = len(list) - 1
        
        while (first <= last) and (position == -1):
            middle = (first + last) / 2
            
            if (list[middle] == found):
                position = middle
            else:
                if (found < list[middle]):
                    last = middle - 1
                else: 
                    first = middle + 1
        return position