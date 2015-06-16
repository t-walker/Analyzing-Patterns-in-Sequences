from distutils.core import setup
import py2exe

packages = [
            'reportlab',
            'xhtml2pdf',
]

setup(
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            "includes":["sip"],
            "packages": packages
        }
    },
    console = [{'script': 'GUI.py'}]
)
