#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import time


class Displayer(object):
    def __init__(self):
        self.data = {}
        self.thread = Thread(target=self._display)
        self.thread.start()

    def set_data(self, value):
        self.data = value

    def _display(self):
        while True:
            print(self.data)
            time.sleep(1)
