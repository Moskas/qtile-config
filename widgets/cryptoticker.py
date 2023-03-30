# from typing import Any
#
# from libqtile import bar
# from libqtile.widget import base
#
# from pycoingecko import CoinGeckoAPI
#
# cg = CoinGeckoAPI()
#
#
# class CryptoTicker(base._TextBox):
#    """Crypto coin ticker"""
#
#    defaults: [
#        ("interval", "1min", "Default delay between queries"),
#        ("coin", None, "Coin to parse from coingecko"),
#    ]
#
#
# def __init__(
#    self,
#    text=cg.get_price(ids=coin, vs_currencies="usd"),
#    width=bar.CALCULATED,
#    **config
# ):
#    base._TextBox.__init__(self, text=text, width=width, **config)
#
#
# def cmd_update(self, text):
#    """Get text"""
#    self.update
#
#
# def cmd_get(self):
#    return self.text
