def message(l,t):
    for i in range(0,len(l)):
        total = l[i]
        fn = 0
        st = i

        while total != t:
            try:
                total = total + l[i+1]
                i += 1
                fn = i
            except IndexError:
                break

        if total == t:
            return [st,fn]
        
    return [-1,-1]

def check_contents_ls(l):
    result = True
    for i in l:
        if type(i) != int:
            result = False 
            break
        if i not in range(1, 101):
            result = False 
            break
    
    if type(l) != list:
        result = False
        
    return result

def check_contents_t(t):
    if type(t) != int:
        return False
    if t not in range(1, 251):
        return False
    
    return True

def solution(l,t):
    if len(l) in range(1, 101):
        if check_contents_ls(l):
            if check_contents_t(t):
                return message(l,t)

    return [-1,-1]

if __name__ == "__main__":
    print(solution([101,50,50,49], 250))
    print(solution([-1,-2,-3,-4], -10))
    print(solution([4, 3, 10, 2, 8], 12))
    print(solution(["a", 3, 5, 7, 13], 20))
    print(solution([1], 1))
    print(solution([2.1,3.9], 6))
    print(solution([99,1], 100))

    x = list(range(1,51)) + list(range(1,51))
    print(solution(x, 250))

    print(solution([1,100], 251))