# 21. Eng ko‘p takrorlangan element
from collections import Counter
lst = list(map(int, input().split()))
print(Counter(lst).most_common(1))

# 22. 2D list yig‘indisi
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(sum(sum(row) for row in matrix))

# 23. Listdan musbat sonlar
lst = list(map(int, input().split()))
print([x for x in lst if x > 0])

# 24. Harf chastotasi
from collections import Counter
s = input()
print(Counter(s))

# 25. Eng kichik 2 ta son
lst = sorted(list(map(int, input().split())))
print(lst[:2])
