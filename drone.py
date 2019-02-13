import sys, datetime, random, string, datetime
from utility import cardinal_to_2d_cartesian_coordinates as coordinates, time_traveled_by_drone_in_minutes as time_traveled, determine_customer_promoter_detractor_rating as NPS_helper

def order_deliveries(ordered_bank, start_time, end_time, bank, origin, speed):
    result = []
    current_time = start_time
    while len(ordered_bank) > 0:
        index = 0
        length = len(ordered_bank)
        while index < length:
            if (current_time-ordered_bank[index][1][1]).days >= 0:
                total_time_traveled = 2 * time_traveled(origin, ordered_bank[index][1][0], speed)
                if(end_time-(current_time + datetime.timedelta(minutes=total_time_traveled))).days < 0:
                    return result
                order_id = ordered_bank[index][0]
                result.append(order_id)
                bank[order_id].append(current_time)
                current_time += datetime.timedelta(minutes=total_time_traveled)
                del ordered_bank[index]
                break
            else:
                index += 1
        if index == length:
            total_time_traveled = 2 * time_traveled(origin, ordered_bank[0][1][0], speed)
            if (end_time - (current_time + datetime.timedelta(minutes=total_time_traveled))).days < 0:
                return result
            order_id = ordered_bank[0][0]
            result.append(order_id)
            bank[order_id].append(current_time)
            current_time += datetime.timedelta(minutes=total_time_traveled)
            del ordered_bank[0]

    return result

def drone(argv):
    inputName = argv[0]
    output = "output_" + ''.join(random.choices(string.ascii_letters + string.digits, k=10))+".txt"
    print("input: ",inputName,", output: ", output)
    bank = {}
    with open(inputName, "r") as r:
        for line in r:
            temp = line.rstrip("\n").split(" ")[:3]
            bank[temp[0]] = [coordinates(temp[1]), datetime.datetime.strptime(temp[2], "%H:%M:%S")]
    warehouse = [0, 0]
    drone_speed = [1, 1]
    ordered_bank = sorted(bank.items(), key=lambda element: time_traveled(warehouse, element[1][0], drone_speed))
    start_time = "06:00:00"
    end_time = "22:00:00"
    order_of_delivery = order_deliveries(ordered_bank, datetime.datetime.strptime(start_time, "%H:%M:%S"), datetime.datetime.strptime(end_time, "%H:%M:%S"), bank, warehouse, drone_speed)
    customers = {"promoter": 0, "neutral": 0, "detractor": 0}
    # those customers who couldn't be served within operation hours
    rest_of_detractors = len(bank)-len(order_of_delivery)
    with open(output, "w") as w:
        for order_id in order_of_delivery:
            w.write(order_id+" "+bank[order_id][2].strftime("%H:%M:%S")+"\n")
            customers[NPS_helper(bank[order_id][2]-bank[order_id][1])] += 1
        customers["detractor"] += rest_of_detractors
        net_promoter_score = int(100*(customers["promoter"]-customers["detractor"])/len(bank))
        w.write("NPS "+str(net_promoter_score))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise Exception("Missing input file path as argument")
    drone(sys.argv[1:])