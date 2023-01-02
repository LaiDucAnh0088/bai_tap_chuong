distance = int(input("nhập số km đã đi: "))
type_car = int(input("nhập loại xe đã sử dụng: "))
time_watting = int(input("nhập thời gian chờ: "))
total_fare = 0

if time_watting <= 5 :
    print("tiền chờ được miễn phí nha bro")
else:
    charge_watting = (time_watting - 5) * 800
    total_fare += charge_watting
    print("số tiền chờ phải trả là:", charge_watting, "đồng")

match type_car:
    case 4:
        total_money = 0
        if distance > 20:
            total_money += 10000 * (distance - 20)
            distance -= distance - 20
        if distance > 0.8:
            total_money += 12100 * (distance - 0.8)
            distance -= distance - 0.8

        # tính giá mở cửa
        total_money += 11000 * distance

        print("tiền di chuyển bạn phải trả cho tôi là:", total_money, "đồng")
        total_fare += total_money
    case 7:
        total_money = 0
        if distance > 30:
            total_money += 12000 * (distance - 30)
            distance -= distance - 30
        if distance > 0.8:
            total_money += 14100 * (distance - 0.8)
            distance -= distance - 0.8

        # tính giá mở cửa
        total_money += 13000 * distance

        print("tiền di chuyển bạn phải trả cho tôi là:", total_money, "đồng")
        total_fare += total_money

print("Tổng tiền cước của bạn là:", total_fare)