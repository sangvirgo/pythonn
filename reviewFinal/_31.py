class Customer:
    def __init__(self, name, old_num, new_num, ma_kh):
        self.name=name
        self.old_num=old_num
        self.new_num=new_num
        self.ma_kh=ma_kh
        s=self.new_num-self.old_num
        money=0
        if s<=50:
            money=s*100
            money+=money*0.02
        elif s<=100:
            money=50*100+(s-50)*150
            money+=money*0.03
        else:
            money=50*100 + 50*150 + (s-100)*200
            money+=money*0.05
        self.tien=round(money)
    def print_cus(self):
        print(self.ma_kh, self.name, self.tien)


def solve():
    t=int(input())
    customers=[]
    for i in range(t):
        name = input()
        old_num = int(input())
        new_num = int(input())
        ma_kh="KH"+f'{i+1:02d}'
        cus = Customer(name, old_num, new_num, ma_kh)
        customers.append(cus)
    customers.sort(key=lambda cust:(-cust.tien))
    for cuss in customers:
        cuss.print_cus()

solve()
'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''