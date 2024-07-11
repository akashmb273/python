#Completed
data={
    "latte":{
        "ingridients":{
            "Milk": 50,
            "Water": 100,
            "Coffee": 75},
        "Rate": 25},
    "espresso":{
        "ingridients":{
            "Milk": 50,
            "Water": 100,
            "Coffee": 100},
        "Rate": 85},
    "cappuchino":{
        "ingridients":{
            "Milk": 100,
            "Water": 50,
            "Coffee": 100},
        "Rate": 125}
}

profit=0
stock={
        "Milk": 750,
        "Water": 1000,
        "Coffee": 500
    }
def calculate(de):
    global profit
    c5 = int(input("Enter No. of 5 Ruppee coins  :"))
    c10 = int(input("Enter No. of 10 Ruppee coins  :"))
    c20 = int(input("Enter No. of 20 Ruppee coins  :"))
    total=(c5*5)+(c10*10)+(c20*20)
    if total>=de:
        change=total-de
        print(f"Remaining change = Rs.{change}")
        profit+=de
        #coffee()
    else:
        print("Money not enough \n Money refunded ...\n Enter coins again...")
        calculate(de)
def update(ce):
    m=stock["Milk"] - ce["Milk"]
    w=stock["Water"] - ce["Water"]
    c=stock["Coffee"] - ce["Coffee"]
    st={
        "Milk": m,
        "Water": w,
        "Coffee": c
    }
    stock.update(st)
def check_resources(ce):
    if stock["Milk"]>ce["Milk"] and stock["Water"]>ce["Water"] and stock["Coffee"]>ce["Coffee"]:
       print("Wait a minute...")
    else:
        print("Not enough Resources")
        return False

def coffee():
    while True:
        ch=input("Enter Your Choice (latte/espresso/cappuchino)  :  ").lower()
        if ch=="off":
            break
        elif ch=="report":
            print(f"Milk = {stock['Milk']}ml")
            print(f"Water = {stock['Water']}ml")
            print(f"Coffee = {stock['Coffee']}g")
            print(f"Profit = Rs.{profit}")
        else:
            type=data[ch]
            #print(type)
            ce= type["ingridients"]
            check_resources(ce)
            if check_resources(ce)==False:
                continue
            update(ce)
            de=type["Rate"]
            calculate(de)
            print(f"Here is Your {ch}")

coffee()

