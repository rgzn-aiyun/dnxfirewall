#!/usr/bin/env python3

import os, sys

HOME_DIR = os.environ['HOME_DIR']
sys.path.insert(0, HOME_DIR)

from dnx_frontend.dfe_dnx_main import app as application

if __name__ == '__main__':
    application.run()
