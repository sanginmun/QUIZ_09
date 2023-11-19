
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")

if selected_beverage not in ["커피", "녹차", "아이스티"]:
    print("잘못된 음료를 선택하셨습니다.")
else:
    quantity = int(input("수량을 입력하세요: "))  # 음료의 수량 입력

    if selected_beverage == "커피":
        total_price = coffee.calculate(quantity)
    elif selected_beverage == "녹차":
        total_price = green_tea.calculate(quantity)
    elif selected_beverage == "아이스티":
        total_price = ice_tea.calculate(quantity)

    print(f"{selected_beverage} {quantity}잔을 주문하셨습니다. 총 가격은 {total_price}원 입니다.")