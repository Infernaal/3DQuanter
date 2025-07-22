#!/usr/bin/env python 
import os

# ❗ Перемещаем установку переменной вверх
os.environ["OCTOPRINT_CONFIG_DIR"] = os.path.expanduser("~/.3dquanter")

if __name__ == "__main__":
    import octoprint
    octoprint.main()
