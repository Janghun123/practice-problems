def calculate_sale(price):
    if price >= 100000:
        return 0.1
    elif price >= 50000:
        return 0.05
    else:
        return 0
    
def calculate_sale_price(price, sale_rate):
    return price * sale_rate

price = int(input("상품 가격을 입력하세요: "))
sale_rate = calculate_sale(price)
sale_price = calculate_sale_price(price, sale_rate)
print(f"할인율: {sale_rate * 100}")
print(f"할인 금액: {sale_price}원")
print(f"최종 결제 금액: {price - sale_price}")