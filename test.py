# n - wymiar
n = 3
tablica = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            tablica[i][j] = 3
        else:
            tablica[i][j] = 2
if n % 2 != 0:
    tablica[n//2][n//2] = 4
                        
for t in tablica:
    print(t)