a = int(input())#number of stations
stations = []#stations list which will include value as well stored in tuples
for i in range(a):
    station_name = input("Station name: ")
    station_value = int(input("Station value: "))
    stations.append((station_name, station_value))
top_name = stations[0][0]
top_value = stations[0][1]
above_45_value = 0
for sataion_name, station_value in stations:
    if station_value > top_value:
        top_value = station_value
        top_name = station_name
    if station_value > 45:
        above_45_value += 1
print(f"Top: ({top_name},{top_value})")
print(f"above_45: {above_45_value}")