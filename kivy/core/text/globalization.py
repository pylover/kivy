#
# try:
#     from rtl import rtl as _rtl, reshaper
# except ImportError:
#     raise ImportError('The rtl package was not installed, You have to install it to use this feature.')
#
#
# def apply_fribidi(data):
#     return _rtl(data)

#
from fribidi import logical_to_visualize
def apply_fribidi(data):
    return logical_to_visualize(data)

#
# from pyfribidi import log2vis
# def apply_fribidi(data):
#     return log2vis(data)
