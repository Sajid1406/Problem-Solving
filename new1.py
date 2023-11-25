t=int(input())

for i in range(t):
    n=int(input())
    result=(((n * 567) // 9 + 7492) * 235 // 47) - 498
    #print(result)
    print(abs(result) // 10 % 10)
    