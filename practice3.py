size = int(input("size of diamond : "))

#상부다이아
for upper_diamond in range(1, size*2, 2): #1, 3, 5, 7, 9
    print((" " * ((size*2 - 1 - upper_diamond // 2)) + ("*"*upper_diamond)))

#하부다이아
for lower_diamond in range(size*2-3, 0, -2):
    print((" " * ((size*2 - 1 - lower_diamond // 2)) + ("*"*lower_diamond)))
