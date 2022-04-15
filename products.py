from unicodedata import name


products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:    # 將資料讀取出來後當作python檔
    for line in f:
        name, price = line.strip().split(',')              # 原資料讀取出來後還有\n的指令，因此需加入.strip()去除換行符號(\n)
        products.append([name, price])


print(products)




with open('products.csv', 'w', encoding = 'utf-8') as f:
    while True:
        name = input('請輸入商品:')
        if name == 'q':
            break

        price = input('請輸入價格:')
        products.append([name, int(price)])  # 若不加上[]使.append()括弧內成為清單，會無法加入，因append內只能加入一種type資料型態
    if products[0] != ['商品', '價格']:
        f.write('商品,價格\n')                   # 此處於價格後直接加入\n也會於讀取時執行指令
    for p in products:                      # 此時的p為products內的一個清單(元素)
        f.write(p[0] + ',' + str(p[1]) + '\n')                       # .write()括弧內只能加入str，因此需轉換型別 ; 
                                                                    # 要對寫入資料做指令也需加上''轉換為str
        
print(products)
print(products[0], products[1])
print(p)
print(p[0], p[1])
