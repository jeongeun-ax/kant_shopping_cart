class Product:

    # 새 상품의 초기 정보 저장 
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock 

    def __str__(self):
        return f"{self.name} {self.price} {self.stock}"

earphone = Product("무선 이어폰", 80_000, 3)
tumbler = Product("텀블러", 30_000, 10)

print(earphone.name, earphone.price, earphone.stock)
print(tumbler.name, tumbler.price, tumbler.stock)

print(earphone)
print(tumbler)

if __name__ == "__main__":
    products = [
        Product("무선 이어폰", 89_000, 3),
        Product("텀블러", 15_000, 10),
        Product("보조 배터리", 32_000, 5),
        Product("마우스패드", 9_000, 0),
        Product("USB 허브", 18_000, 4)
    ]

    for p in products: print(p)