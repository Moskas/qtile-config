#!/usr/bin/env python3


def get_linux_distribution():
    try:
        with open("/etc/os-release", "r") as f:
            lines = f.readlines()
            info = {}
            for line in lines:
                parts = line.strip().split("=")
                if len(parts) == 2:
                    info[parts[0]] = parts[1].strip('"')
            dist_name = info.get("PRETTY_NAME", "Unknown")
            return dist_name
    except FileNotFoundError:
        return ":thinking:"


def get_distro_logo():
    match get_linux_distribution().split(" ")[0]:
        case "NixOS":
            return ""
        case "Void":
            return ""
        case "Arch":
            return "󰣇"
        case _:
            return ""
