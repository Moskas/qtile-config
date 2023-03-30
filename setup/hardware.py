import cpuinfo as cpu
from battery import battery_exists
class processor():
    vendor = cpu.get_cpu_info()['vendor_id_raw']

print(processor.vendor)

def cpu_color():
    if processor.vendor == 'GenuineIntel':
        (gruvbox['blue'])
    else:
        (gruvbox['red'])

print(battery_exists())
