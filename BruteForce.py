# Bubble Sort-un Python tətbiqi

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for a in range(0, n-i-1):

            # Arrayi 0-dan n-i-1-ə çevirin
             # Tapılan element növbəti elementdən böyükdürsə, dəyişdirin
            if arr[a] > arr[a+1]:
                arr[a], arr[a+1] = arr[a+1], arr[a]

        print(arr)


arr = [3, 8, 2, 5, 6, 1, 9, 4, 7]
bubble_sort(arr)
print("Sorted array is:", arr)


# Linear_Search-in Python tətbiqi

def linear_search(kitab, qelem):
    for position, item in enumerate(kitab):
        if item == qelem:
            return position
    return -1
print(linear_search([4, 5, 2, 7, 1, 8], 7))


# Linear_Search-in  Minimum Dəyəri Tapmaq Python tətbiqi

def minimum_deyer(lst):
      min = None
      for el in lst:
          if min == None or el > min:
              min = el
              return min
test = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
print(minimum_deyer(test))