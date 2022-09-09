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
    
    
    # <-- Quick Sort -->
    def __quickSort__(self, first, last):
        left = first
        right = last - 1
        pivot = last
        
        while (left < right):
            while (self.list[left] < self.list[pivot]) and (left <= right):
                left += 1
            
            while (self.list[right] > self.list[pivot]) and (right >= left):
                right -= 1
            
            if (left < right):
                self.list[left], self.list[right] = self.list[right], self.list[left]
            
        if (self.list[pivot] < self.list[left]):
                self.list[left], self.list[pivot] = self.list[pivot], self.list[left]
            
        if (first < left):
            self.__quickSort__(self.list, first, left - 1)
            
        if (last > left):
            self.__quickSort__(self.list, left + 1, last)
        return self.list
    
    
    # <-- Merge Sort -->
    def __mergeSort__(self):
        if (len(self.list) <= 1):
            return self.list
        else:
            middle = len(self.list) // 2
            left = []
            
            for i in range(0, middle):
                left.append(self.list[i])
            
            right = []
            
            for i in range(middle, len(self.list)):
                right.append(self.list[i])
            
            left = self.__mergeSort__(left)
            right = self.__mergeSort__(right)
            
            if (left[middle - 1] <= right[0]):
                left += right
            
            result = self.__merge__(left, right)
            return result

    def __merge__(left, right):
        newList = []
        
        while (len(left) > 0) and (len(right) > 0):
            if (left[0] < right[0]):
                newList.append(left.pop(0))
            else:
                newList.append(right.pop(0))
        
        if (len(left) > 0):
            newList += left
        
        if (len(right) > 0):
            newList += right
        return newList
    
    
    # <-- Radix Sort -->
    def __radixSort__(self):
        max_element = max(self.list)
        space = 1

        while max_element // space > 0:
            self.__countingSort__(self.list, space)
            space *= 10
    
    def __countingSort__(oddList, space):
        length = len(oddList)
        output = [0] * length
        count = [0] * 10
        
        for i in range(0, length):
            index = oddList [i] // space
            count[index % 10] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = length - 1
        
        while i >= 0:
            index = oddList[i] // space
            output[count[index % 10] - 1] = oddList [i]
            count[index % 10] -= 1
            i -= 1
            
        for i in range(0, length):
            oddList [i] = output[i]
    
    # <-- Count Sort -->
    def __countSort__(self, index):
        countList = [0] * (index + 1)
        orderList = [None] * len(self.list)
        
        for i in self.list:
            countList[i] += 1
        total = 0
        
        for i in range(len(countList)):
            countList[i], total = total, total + countList[i]
        
        for index in self.list:
            orderList[countList[index]] = index
            countList[index] += 1
        
        return orderList
    
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
    
    # <-- Bucket Sort -->
    def __bucketSort__(self):
        max_value = max(self.list)
        size = max_value/len(self.list)
        buckets_list = []

        for x in range(len(self.list)):
            buckets_list.append([]) 

        for i in range(len(self.list)):
            j = int (self.list[i] / size)

            if j != len (self.list):
                buckets_list[j].append(self.list[i])
            else:
                buckets_list[len(self.list) - 1].append(self.list[i])

        for z in range(len(self.list)):
            i = self.__insertionSort__(buckets_list[z])

        final_output = []

        for x in range(len (self.list)):
            final_output = final_output + buckets_list[x]
        return final_output
    
    # <-- Tim Sort -->
    def __timSort__(self):
        n = len(self.list)
        minRun = self.__calcMinRun__(n)
    
        for start in range(0, n, minRun):
            end = min(start + minRun - 1, n - 1)
            self.__insertionSort__(self.list, start, end)

        size = minRun
        while size < n:
    
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
    
                if mid < right:
                    self.__merge__(self.list, left, mid, right)
            size = 2 * size
        return self.list
    
    def __calcMinRun__(self, n):
        r = 0

        while n >= self.MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r
    
    def __merge__(arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])
    
        i, j, k = 0, 0, l

        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
    
            else:
                arr[k] = right[j]
                j += 1
    
            k += 1
    
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1
    
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