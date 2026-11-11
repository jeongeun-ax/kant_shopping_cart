class Coupon:
    def __init__(self, name):
        self.name = name 

    # 할인 금액 반환 
    def discount_amount(self, total):
        return  0


# 10% 할인 부폰
class PercentCoupon(Coupon):
    # 할인율과 최대 할인율 적용 
    def __init__(self, rate, max_discount):
        super.__init__("웰컴 쿠폰")
        self.rate = rate
        self.max_discount = max_discount

    def discount_amount(self, total):
        pass
        # return # 로직 구현 


# 정액 할인 쿠폰 
class FixedCoupon(Coupon):
    def __init__(self, amount, min_total)
        super.__init__(f"첫 구매 {amount}원 할인 쿠폰({min_total}만원 이상 구매시)")
        self.amount = amount
        self.min_total = min_total

    def discount_amount(self, total):
        pass
        # return # 로직 구현 