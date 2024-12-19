class Employee:
    def __init__(self, name, lt, th, ms, tb):
        self.name=name
        self.ms=ms
        self.lt=lt
        self.th=lt
        self.tb=tb
        if float(self.tb)<5:
            self.result="TRUOT"
        elif float(self.tb)<8:
            self.result="CAN NHAC"
        elif float(self.tb)<=9.5:
            self.result="DAT"
        else:
            self.result="XUAT SAC"

    def print_e(self):
        print(self.ms+' '+ self.name+' '+ f"{self.tb:.2f}"+' '+ self.result)

def solve():
    t=int(input())
    employees=[]
    for i in range(t):
        name = input()
        lt = float(input())
        if lt>10:
            lt=lt/10.0
        th = float(input())
        if th>10:
            th=th/10.0
        tb=(lt+th)/2.0
        ms = "TS0"+str(i+1)
        employees.append(Employee(name, lt, th, ms, tb))
    employees.sort(key=lambda x:-float(x.tb))
    for i in employees:
        i.print_e()

solve()



'''
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''
