#!/usr/bin/env python
def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()
            info = {}
            for line in lines:
                parts = line.strip().split('=')
                if len(parts) == 2:
                    info[parts[0]] = parts[1].strip('"')
            dist_name = info.get('PRETTY_NAME', 'Unknown')
            return dist_name
    except FileNotFoundError:
        return "Not a Linux distribution"

print(get_linux_distribution().split(' ')[0])

