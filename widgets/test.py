from typing import Any

from libqtile import bar
from libqtile.widget import base


class RextBox(base._TextBox):
    """A flexible textbox that can be updated from bound keys, scripts, and qshell."""

    defaults = [
        ("font", "sans", "Text font"),
        ("fontsize", None, "Font pixel size. Calculated if None."),
        ("fontshadow", None, "font shadow color, default is None(no shadow)"),
        ("padding", None, "Padding left and right. Calculated if None."),
        ("foreground", "#ffffff", "Foreground colour."),
    ]  # type: list[tuple[str, Any, str]]

    def __init__(self, text=" ", width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, text=text, width=width, **config)

    def cmd_update(self, text):
        """Update the text in a TextBox widget"""
        self.update(text)

    def cmd_get(self):
        """Retrieve the text in a TextBox widget"""
        return self.text
