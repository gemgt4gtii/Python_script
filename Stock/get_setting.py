#6-1自訂函式
def get_setting():
    res = []
    try:
        with open('stock.txt') as f:
            slist = f.readlines()
            print('讀入:',slist)
            for lst in slist:
                s = lst.split(',')
                res.append([s[0].strip(),float(s[1]),float(s[2])])
    except:
        print('stock.txt 讀取錯誤')
    return res
stock = get_setting()
print('傳回:',stock)

