def bill(unit):
    if(unit>100):
        print("bill=", unit * 2)
    elif(unit>200):
        print("bill=", (unit-100)* 4)
    else:
        print("bill=",(200+400+(unit-200)* 5))