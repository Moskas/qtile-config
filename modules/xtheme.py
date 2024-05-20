import os

# xres_path = os.environ["HOME"] + "/.Xresources"
# xres_file = open(xres_path, "r")
# xres = []
# for x in xres_file:
#    xres.append(x.strip().split(" "))
#
XRESOURCE_FILEPATH = os.environ["HOME"] + "/.Xresources"
xres = [line.strip().split(" ") for line in open(XRESOURCE_FILEPATH, "r")]


def get_colors(xres, index):
    # it's parsed as ['*background' : '#282828']
    # and I only need the rgb value so it's only returning first index
    return xres[index][1]


# the most unoptimal enum declaration lmao
colors = {
    "bg": get_colors(xres, 0),
    "bg1": get_colors(xres, 1),
    "red": get_colors(xres, 2),
    "dark-green": get_colors(xres, 3),
    "dark-yellow": get_colors(xres, 4),
    "dark-blue": get_colors(xres, 5),
    "dark-magenta": get_colors(xres, 6),
    "dark-cyan": get_colors(xres, 7),
    "fg1": get_colors(xres, 8),
    "green": get_colors(xres, 9),
    "yellow": get_colors(xres, 10),
    "blue": get_colors(xres, 11),
    "dark-magenta": get_colors(xres, 12),
    "cyan": get_colors(xres, 13),
    "fg2": get_colors(xres, 14),
    "gray": get_colors(xres, 15),
    "dark-red": get_colors(xres, 16),
    "fg": get_colors(xres, 17),
}

print(colors)
