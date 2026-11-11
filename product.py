class Product:
    next_id = 1 # 클래스 변수 

    # 새 상품의 초기 정보 저장 
    def __init__(self, name, price, stock):
        self.id = Product.next_id
        Product.next_id += 1 # 다음 상품을 위해 Index 값 +1
        self.name = name
        self.price = price
        self.stock = stock 

    def is_sold_out(self): 
        return self.stock == 0 

    def __str__(self):
        stock_text = "품절" if self.is_sold_out() else f"재고 {self.stock}개"
        return f"{self.id}: {self.name:<10} {self.price:>8,} {stock_text}"








# ------------------------------------------------------------
# 테스트 코드
# ------------------------------------------------------------
# 이 파일을 직접 실행 시켰을 때만 코드가 실행 되도록하는 로직 
# uv run product.py
if __name__ == "__main__":
    products = [
        Product("무선 이어폰", 89_000, 3),
        Product("텀블러", 15_000, 10),
        Product("보조 배터리", 32_000, 5),
        Product("마우스패드", 9_000, 0),
        Product("USB 허브", 18_000, 4)
    ]

    for p in products: print(p)

# earphone = Product("무선 이어폰", 80_000, 3)
# tumbler = Product("텀블러", 30_000, 10)

# print(earphone.name, earphone.price, earphone.stock)
# print(tumbler.name, tumbler.price, tumbler.stock)   # ctrl + shift + l = 해당 페이지에 있는 단어를 전체 선택할 때 (단어 셀렉 후 단축키) # ctrl + d : 한줄내 ?

#print(earphone)
#print(tumbler)
 