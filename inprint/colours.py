import re
from functools import partial

COLOURS = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
STYLES = (
    "bold",
    "faint",
    "italic",
    "underline",
    "blink",
    "blink2",
    "negative",
    "concealed",
    "crossed",
)


class ColoursException(Exception):
    pass


def colour(s, foreground=None, background=None, style=None):
    sgr = []

    if foreground:
        if foreground in COLOURS:
            sgr.append(str(30 + COLOURS.index(foreground)))
        elif isinstance(foreground, int) and foreground in range(0, 256):
            sgr.append(f"38;5;{foreground}")
        else:
            raise ColoursException(f'Invalid colour "{foreground}"')

    if background:
        if background in COLOURS:
            sgr.append(str(40 + COLOURS.index(background)))
        elif isinstance(background, int) and background in range(0, 256):
            sgr.append(f"48;5;{background}")
        else:
            raise ColoursException(f'Invalid colour "{background}"')

    if style:
        for st in style.split("+"):
            if st in STYLES:
                sgr.append(str(1 + STYLES.index(st)))
            else:
                raise ColoursException(f'Invalid style "{st}"')

    if sgr:
        prefix = r"\x1b[" + ";".join(sgr) + "m"
        suffix = r"\x1b[0m"
        return f"{prefix}{s}{suffix}"
    else:
        return s


def strip_color(s):
    return re.sub(r"\x1b\[.+?m", "", s)


# Foreground shortcuts
black = partial(colour, foreground="black")
red = partial(colour, foreground="red")
green = partial(colour, foreground="green")
yellow = partial(colour, foreground="yellow")
blue = partial(colour, foreground="blue")
magenta = partial(colour, foreground="magenta")
cyan = partial(colour, foreground="cyan")
white = partial(colour, foreground="white")

# Style shortcuts
bold = partial(colour, style="bold")
faint = partial(colour, style="faint")
italic = partial(colour, style="italic")
underline = partial(colour, style="underline")
blink = partial(colour, style="blink")
blink2 = partial(colour, style="blink2")
negative = partial(colour, style="negative")
concealed = partial(colour, style="concealed")
crossed = partial(colour, style="crossed")
