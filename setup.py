import sys
from cx_Freeze import setup, Executable

base=None

exe=Executable(script='main.py',base=base)

setup(name='pfd',version='1.0',description='converter',executables=[exe])