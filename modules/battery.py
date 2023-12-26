def has_battery():
    try:
        with open("/sys/class/power_supply/BAT0/present", "r") as file:
            content = file.read().strip().lower()
            if content == "1":
                return True
            else:
                return False
    except Exception:
        return False
