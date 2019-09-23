

def main():
    n = int(input())
    a_L = list(map(int,input().split(" ")))

    a_L.reverse()

    c = a_L[0]
    
    for val in a_L:
        # -1する場合
        if c - 1 > val+1:
            return "No"
        elif c - 1 == val:
            c = val
        elif c - 1 ==val + 1:
            pass

        # 何もしない場合
        elif c == val:
            c = val
        elif c == val-1:
            c = val
        #elif c < val - 1:
        #    return "No"
        elif c - val < -2:
            return "No"


    
    return "Yes"

if __name__=="__main__":
    print(main())
