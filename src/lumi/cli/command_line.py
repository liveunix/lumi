from .parser import parse_args
from .dispatcher import dispatch

def call_cli():
    dispatch(parse_args())
