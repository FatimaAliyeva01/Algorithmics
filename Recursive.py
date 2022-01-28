# Verilmiş ədədin faktorialını tapmaq funksiyası
def faktorial(n):
    if n == 0:
        return 1
    return n * faktorial(n-1)
num = 5;
print("Faktorial", num, "eded", faktorial(num))

#-------------------------------------------

#Bu kod Fibonacci seriyasında n-ci ədədi verir - {0,1,1,2,3,5,......}.
def Fibonacci(n, second_last, last):
    if n-1 == 0:
        return second_last
    else:
        new_last = second_last + last
        second_last = last
        return Fibonacci(n-1, second_last, new_last)
if __name__ == "__main__":
    print(Fibonacci(10, 0, 1))


#__________________________________________

#Hanoy qalasını həll etmək üçün ,Rekursiv Python funksiyası
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B çubuqların adıdır.
