def temp_first(n):
    n1 = n / 3
    n2 = n / 2
    n3 = n - 1
    if n1 == 1 or n2 == 1 or n3 == 1:
        return 0
    else:
        return n1, n2, n3
    
def temp_list(li):
    temp = []
    for i in li:
        n1 = i / 3
        n2 = i / 2
        n3 = i-1
        if n1 == 1 or n2 == 1 or n3 == 1:
            return 0
        else:
            if n1 % 1 == 0:
                temp.append(n1)
            if n2 % 1 == 0:
                temp.append(n2)
            temp.append(n3)

    return temp
    

def sol(n):
    li = []
    count = -1
    while True:
        count += 1
        if count == 0 : k = temp_first(n)
        else: k = temp_list(li[-1])

        if k == 0:
            return count
        else:
            li.append(list(k))
            
        if count > 1:
            li.remove(li[0])

n = int(input())
print(sol(n))

#미완성
