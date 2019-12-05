def test():
    list = []
    list.append(10.00) #light level, 10.00 lx
    list.append(83.7)  #humidity level 83.7%
    list.append(999.1) #pressure level 999.1 hPa
    list.append(24.4) #temperature 24.4C
    return list

def test2():
    print ('d')

print (str(test())[1:-1])