def orSubset():
    size = int(input("\nEnter number of elements: "))
    arr = []
    for i in range(size):
        el = int(input("\nEnter element: "))
        arr.append(el)
    arr.sort(reverse=True)
    binarr = []
    for el in arr:
        binstr = bin(el).replace("0b","")
        binarr.append(binstr)
    print(binarr)
    index = len(binarr[0])
    #print(index)
    pos = 1
    update = '0'*index
    #print(update)
    count = 999
    finarr = []
    for i in range(index):
        flag1 = 0
        for j in range(len(update)):
            if update[j] == '0':
                count = len(update)-j
                #print(j)
                break
        upperlim = 2**(count+1)
        lowerlim = 2**count
        maxel = 0
        if update!=('1'*index):
        
            for el in binarr:
                value = 0
                power = len(el)
                pos = power - count
                flag2 = 0
                for j in range(len(el)):
                    if el[j] == '1':
                        value = value + (2**power)
                        #print(value)
                        if j == pos:
                            flag2 = 1
                    power = power - 1
                if (value > maxel) and (value >= lowerlim) and (flag2 == 1):
                    maxel = value
                    ins = el
                    flag1 = 1
            #print("flag: ",flag1)
            if flag1 == 1:
                binarr.remove(ins)
                #print(binarr)
                x = len(update)-len(ins)
                y = 0
                new = ''
                for i in range(len(update)):
                    if i>=x:
                        temp1 = int(update[i])
                        temp2 = int(ins[y])
                        replace = str(temp1 or temp2)
                        new = new+replace
                        y = y + 1
                    else:
                        new = new+update[i]
                update = new
                        
                #print(int(update,2))
                finarr.append(int(ins,2))
                #print(finarr)
        else:
            break
    print(int(update,2))
    print(finarr)
#main environment
orSubset()