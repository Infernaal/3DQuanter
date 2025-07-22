#!/usr/bin/env python
import os

if __name__ == "__main__":
    import octoprint
    os.environ["OCTOPRINT_CONFIG_DIR"] = os.path.expanduser("~/.3dquanter")
    octoprint.main()
