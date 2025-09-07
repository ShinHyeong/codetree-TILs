product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
#상품 정보
class Product:
    def __init__(self, product_name,product_code):
        self.name = product_name
        self.code = product_code

#상품1 : 정보 초기화 (상품명 - "codetree", 상품코드 - 50)
#상품2 : 입력받은 값
p1 = Product("codetree",50)
p2 = Product(product_name,product_code)

#형식에 맞추어 출력
print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")