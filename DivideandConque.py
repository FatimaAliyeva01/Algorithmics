#Binary Search.

# Əgər varsa massivdəki x indeksini qaytarır, əks halda -1

def binarySearch(arr, l, r, x):
	if r >= l:

		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid

		# Element ortadan kiçikdirsə, o zaman
        # yalnız sol alt massivdə mövcud ola bilər
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		# Əks halda element yalnız mövcud ola bilər
        # sağ alt massivdə
		else:
			return binarySearch(arr, mid + 1, r, x)

	else:
		# Element massivdə yoxdur
		return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element indeksdə mövcuddur % d" % result)
else:
	print("Element massivdə yoxdur")

#-----------------------------------------


# QuickSort

# Bu Funksiya tez siralanma hissəsinin siralanmasini idarə edir
# başlanğıc və son elementin birinci və son elementi
# müvafiq olaraq massiv
def partition(start, end, array):
    # Başlamaq üçün pivot indeksi işə salınır
	pivot_index = start
	pivot = array[pivot_index]
	# Bu dövrə başlanğıc göstəricisi keçənə qədər davam edir
    # son göstərici və o olduqda biz onu dəyişdiririk
    #Son göstəricidə elementi olan pivot
	while start < end:
		# Başlanğıc göstəricisini tapana qədər artırın
        # element pivotdan böyükdür
		while start < len(array) and array[start] <= pivot:
			start += 1
		# Son göstəricini tapana qədər azaldın
        # element pivotdan azdır
		while array[end] > pivot:
			end -= 1
		if(start < end):
			array[start], array[end] = array[end], array[start]
	# Son göstəricidəki elementlə pivot elementini dəyişdirin.
    # Bu, pivotu düzgün çeşidlənmiş yerə qoyur.
	array[end], array[pivot_index] = array[pivot_index], array[end]
	return end
# QuickSort tətbiq edən əsas funksiya
def quick_sort(start, end, array):
	if (start < end):
		p = partition(start, end, array)
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')




#------------------------
#MergeSort
# MergeSort tətbiqi Python
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        ## Məlumatları L[] və R[] müvəqqəti massivlərinə köçürün
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
# Hər hansı bir elementin qalıb-qalmadığını yoxlamaq        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  
