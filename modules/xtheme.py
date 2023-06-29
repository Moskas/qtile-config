import os

xres_path = os.environ["HOME"] + "/.Xresources"
xres_file = open(xres_path, "r")
xres = []
for x in xres_file:
    xres.append(x.strip().split(" "))


def get_colors(xres, index):
    # it's parsed as ['*background' : '#282828']
    # and I only need the rgb value so it's only returning first index
    return xres[index][1]


# the most unoptimal enum declaration lmao
colors = {
    "bg": get_colors(xres, 0),
    "fg": get_colors(xres, 1),
    "black": get_colors(xres, 2),
    "gray1": get_colors(xres, 3),
    "dark-red": get_colors(xres, 4),
    "red": get_colors(xres, 5),
    "dark-green": get_colors(xres, 6),
    "green": get_colors(xres, 7),
    "dark-yellow": get_colors(xres, 8),
    "yellow": get_colors(xres, 9),
    "dark-blue": get_colors(xres, 10),
    "blue": get_colors(xres, 11),
    "dark-magenta": get_colors(xres, 12),
    "magenta": get_colors(xres, 13),
    "dark-cyan": get_colors(xres, 14),
    "cyan": get_colors(xres, 15),
    "fg1": get_colors(xres, 16),
    "fg2": get_colors(xres, 17),
    "dark-gray": get_colors(xres, 18),
    "gray": get_colors(xres, 19),
}

print(colors)
