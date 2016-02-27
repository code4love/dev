n = int(input("input an integer:"))
print(n, "=", sep="", end="")
while True:
    for i in range(2, n//2 + 1):
        if n%i == 0:
            print(i, "*", sep="", end="")
            n = n // i
            break
    else:
        print(n)
        break

