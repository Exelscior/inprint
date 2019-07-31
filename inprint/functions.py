import sys


def iprint(
    imput: str,
    autoclose: bool = True,
    autoprint: str = True,
    clean=False,
    file=sys.stdout,
):
    """
    Utility function that provides interactive prints with unicode activated curses manipulation

    Uses a concatenation formatting syntax, for example:

      >>> from inprint import iprint
      >>> iprint('[b]This text will print in blue.[/]')
      >>> iprint('[*][r]This text will print in bold and red.[/]')
      >>> iprint('[*][r]Bold red text: [/][y]Non-bold yellow text, [b]blue text, [*]bold blue text.[/]')

    :param imput: str: Input stream to format and print
    :param autoclose: bool: Defaults to `True`: Automatically append the curses termination byte
    :param autoprint: bool: Defaults to `True`: Automatically pass the formatted string to `print()`
    :param clean: bool: Defaults to `False`: If set to True, all color tags will be removed to clean the string.
    :param file: Defaults to `sys.stdout`: IO stream to print to. See `file` parameter for `print()`
    :return: str: The formatted string result
    """
    colours = {
        "black": ("d", "\x1b[30m"),
        "red": ("r", "\x1b[31m"),
        "green": ("g", "\x1b[32m"),
        "yellow": ("y", "\x1b[33m"),
        "blue": ("b", "\x1b[34m"),
        "magenta": ("m", "\x1b[35m"),
        "cyan": ("c", "\x1b[36m"),
        "white": ("w", "\x1b[37m"),
    }
    bold_colours = {
        "black": ("D", "\x1b[1m\x1b[30m"),
        "red": ("R", "\x1b[1m\x1b[31m"),
        "green": ("G", "\x1b[1m\x1b[32m"),
        "yellow": ("Y", "\x1b[1m\x1b[33m"),
        "blue": ("B", "\x1b[1m\x1b[34m"),
        "magenta": ("M", "\x1b[1m\x1b[35m"),
        "cyan": ("C", "\x1b[1m\x1b[36m"),
        "white": ("W", "\x1b[1m\x1b[37m"),
    }
    styles = {
        "bold": ("*", "\x1b[1m"),
        "faint": ("~", "\x1b[2m"),
        "italic": ("i", "\x1b[3m"),
        "underline": ("_", "\x1b[4m"),
        "blink": ("bl", "\x1b[5m"),
        "blink2": ("bl2", "\x1b[6m"),
        "negative": ("neg", "\x1b[7m"),
        "concealed": ("?", "\x1b[8m"),
        "crossed": ("-", "\x1b[9m"),
        "reset": ("/", "\x1b[0m"),
    }
    for name, colour in bold_colours.items():
        imput = imput.replace(f"[{colour[0]}]", colour[1] if not clean else "")
    for name, colour in colours.items():
        imput = imput.replace(f"[{colour[0]}]", colour[1] if not clean else "")
    for name, style in styles.items():
        imput = imput.replace(f"[{style[0]}]", style[1] if not clean else "")
    if autoclose and not clean:
        imput += styles["reset"][1]
    if autoprint:
        print(imput, file=file)
    return imput
