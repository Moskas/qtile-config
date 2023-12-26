#!/usr/bin/env python3

import subprocess


def get_colors():
    try:
        # Run the xrdb command to get the base-16 colors
        result = subprocess.run(
            ["xrdb", "-query"], capture_output=True, text=True, check=True
        )

        # Extract the color lines from the command output
        color_lines = [
            line.strip()
            for line in result.stdout.splitlines()
            if line.startswith("*color")
        ]

        # Extract and return the color values
        colors = {}
        for line in color_lines:
            parts = line.split(":")
            if len(parts) == 2:
                color_name = parts[0].strip()
                color_value = parts[1].strip()
                colors[color_name] = color_value

        return colors

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


# Example usage
colors = get_colors()
if colors:
    for color_name, color_value in colors.items():
        print(f"{color_name}: {color_value}")
