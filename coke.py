price = 50
print(f"Amount Due:",price)
coin = int(input("Coin: "))
price = price - coin

while price <= 50:
    print(f"Amount Due:",price)
    coin = int(input("Coin: "))
    price = price - coin
    if price < 0:
        price = price * -1
        print(f"Change owed:",price)
        break
    elif price == 0:
        break
    else:
        pass