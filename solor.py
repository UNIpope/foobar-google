import math

def round_root(area):
    areaRoot = math.sqrt(area)
    rounded = int(areaRoot)
    out = rounded * rounded

    if out:
        return out

if __name__ == "__main__":
    area = 15324

    ls = [] 
    if area >= 1 and area <= 1000000:
        x = round_root(area)
        area = area - x
        ls.append(x)
        while x:
            x = round_root(area)
            try:
                area = area - x
                ls.append(x)
            except:
                pass
    
    print(ls)

