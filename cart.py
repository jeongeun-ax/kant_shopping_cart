from product import Product

class Cart:
    def __init__(self): 
        # 빈 장바구니 생성  
        self.items = {}  # {상품: 수량}

    # 장바구니에 상품 담기
    def add(self, product, qty):
        # 품절 상품은 담을 수 없다. 
        if product.is_sold_out(): 
            print("품절된 상품입니다.")
            return

        # 이미 장바구니에 담겨있는 수량 체크 
        in_cart_qty = self.items.get(product, 0)
        # 더 담을 수 있는 수량 
        extra_qty = product.stock - in_cart_qty
        if qty > extra_qty:   # 재고 수량 범위를 벗어난 경우 
            print(f"재고가 부족합니다. (담을 수 있는 수량: {extra_qty}개)")
            return

        self.items[product] = self.items.get(product, 0) + qty      # 기존 수량 체크 후 기존 수량이 없는 경우, "0" + 방금 담은 
        print(f"{product.name} {qty}개를 담았습니다.")

    # 장바구니에서 상품 제거(빼기)
    # 고려 사항: 장바구니에 있는 상품만 빼야함 
    def remove(self, product, qty):
        # 장바구니에 없는 상품은 뺄 수 없음 
        if product not in self.items:          # not in 
            print("장바구니에 해당 상품이 없습니다.")
            return  

        # 담은 수량 이상 빼면 상품을 통째 삭제 
        if qty >= self.items[product]:
            del self.items[product]   # 해당 상품을 딕셔너리에서 삭제 
            print(f"{product.name}을 장바구니에서 모두 뺐습니다.")
        else:  
            self.items[product] =+ qty
            print(f"{product.name} {qty}개를 뺐습니다.")

    # 장바구니 비었는지 확인 
    def is_empty(self):
        return len(self.items) == 0

    # 상품 합계 계산 
    def subtotal(self):
        return sum(p.price * q for p,q in self.items.items())

    # 배송비
    def shipping(self):
        if self.is_empty(): return 0
        return 0 if self.subtotal() >= 30_000 else 3_000   # 3만원 이상이면 0이고, 아니면 3,000원 

    # 결제 금액 계산
    def total(self):
        return self.subtotal() + self.shipping()

    # 장바구니 내용 출력 
    def show(self):
        

# ------------------------------------------------------------
# 테스트 코드
# ------------------------------------------------------------
# 제품 인스턴스 생성 
tumbler = Product("텀블러", 15_000, 10)
mousepad = Product("마우스패드", 9_000, 0)
# 카트 인스턴스 생성
cart = Cart()
cart.add(tumbler, 10)
cart.remove(tumbler, 3)
cart.remove(mousepad, 3)
cart.remove(tumbler, 8) # 현재 재고 7 < 8 => 전체 삭제 

print("남은 종류:", len(cart.items))



# cart.add(tumbler, 2)  # 실패 : 재고부족
# cart.add(tumbler, 1)  # 성공 


#for p, q in cart.items.items(): 
    #print(f"{p.id}: {p.name} x {q}")
