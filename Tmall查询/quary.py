def quaryTotal(path = '.'):
    infodict = {}
    Total = 0
    Curquary = 0
    for line in open(path + '/quary2.txt'):
        (action, num, price) = line.split(" ")[0:3]
        num = int(num)
        price = int(price)
        if action == 'up':
            if price in infodict:
                infodict[price] += num
            else:
                infodict[price] = num
        elif action == 'down':
            if price in infodict:
                if num >= infodict[price]:
                    infodict[price] = 0
                else:
                    infodict[price] -= num
        else:
            Curquary = 0
            for i in infodict:
                if i >= num and i <= price:
                    Curquary += infodict[i]
            Total += Curquary
    return Total
        #infodict[price] = num  3334590479
        
