#program to 
university_is_far_away=4 #miles
bus_speed=25 #mph
bus_wait=2 #minutes each of the 10 stops
bus_wait_stops=10 #times
total_time_taken=(university_is_far_away/bus_speed)*60
total_time_taken_after_stops=total_time_taken+(bus_wait*bus_wait_stops)

mile_1=7
mile_2and3=15
mile4=7

total_time_taken_by_jogging=((1/7)*60)+((2/15)*60)+((1/7)*60)

if(total_time_taken_after_stops>total_time_taken_by_jogging):
    print("jogging is faster")
else:
    print("taking a bus is faster")
