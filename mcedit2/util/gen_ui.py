import logging
import os
from PySide6.scripts.pyside_tool import pyside6_uic

log = logging.getLogger(__name__)

def compile_ui():
    from mcedit2.util import resources
    if not resources.isSrcCheckout():
        return

    src = resources.getSrcFolder()
    uiDir = os.path.join(src, "mcedit2", "ui")

    log.info("Compiling .ui files...")
    compile_ui_dir(uiDir, recurse=True)
    log.info("Done.")

def compile_ui_dir(directory, recurse=False):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ui'):
                ui_file = os.path.join(root, file)
                py_file = os.path.splitext(ui_file)[0] + ".py"
                log.info(f"Compiling {ui_file} to {py_file}")
                pyside6_uic.compileUi(ui_file, py_file)

        if not recurse:
            break

if __name__ == '__main__':
    compile_ui()
