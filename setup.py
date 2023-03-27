import sys
from cx_Freeze import setup, Executable

base=None
exe=Executable(script='main.py',base=base)

setup(name='pfd_787',version='1.2',description='787',executables=[exe])