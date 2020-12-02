def check_val_list(e):
    result = True 
    if type(e) != int:
        result = False 
    if e not in range(1, 101):
        result = False 
    
    return result


def solve(l,t):
    for i,ival in enumerate(l):
        if check_val_list(ival):
            for j,_ in enumerate(l):
                if sum(l[i:j+1]) == t:
                    return [i, j]

    return [-1,-1]

def check_contents_t(t):
    if type(t) != int:
        return False
    if t not in range(1, 251):
        return False
    
    return True

def solution(l,t):
    if type(l) == list and check_contents_t(t):
        return solve(l,t)
    else:
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