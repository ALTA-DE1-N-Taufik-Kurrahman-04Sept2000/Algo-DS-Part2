def maximum_buy_product(money, product_price):
    # Mengurutkan harga produk dari yang termurah
    product_price.sort()
    
    # Membuat sebuah set kosong untuk melacak produk yang sudah dibeli
    bought_products = set()
    
    # Menghitung jumlah produk yang dapat dibeli
    count = 0

    for price in product_price:
        if price <= money and price not in bought_products:
            money -= price
            bought_products.add(price)
            count += 1
        else:
            break

    return count

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0