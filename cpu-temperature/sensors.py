import psutil

sensors = psutil.sensors_temperatures()
print(sensors)
