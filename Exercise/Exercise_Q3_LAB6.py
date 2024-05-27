for i in range(1,10):
    if i==3:
        continue
    if i==7:
        break
    print("outer loop:", i)
    for j in range(1,4):
        if j==3:
            continue
        print("inner loop:", j)