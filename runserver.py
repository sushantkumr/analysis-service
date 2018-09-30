#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
import logging

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s'
    )
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
