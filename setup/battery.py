import psutil

def battery_exists():
    if psutil.sensors_battery() != None:
        return True
    else:
        return False
