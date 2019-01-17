import io
import sys

g_buffer = sys.stdout = sys.__stdout__ = io.TextIOWrapper(
    sys.stdout.detach(), encoding=sys.stdout.encoding, line_buffering=True
)


def g_buf():
    return g_buffer


def write_to_stdout():
    """ TODO Use sys.stdout.reconfingure instead of detach """
    g_buffer = sys.stdout = sys.__stdout__ = io.TextIOWrapper(
        sys.stdout.detach(),
        encoding=sys.stdout.encoding,
        line_buffering=True,
        write_through=True,
    )
