#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import json
from enum import Enum


class Status(Enum):
    failed = 1
    updating = 2
    success = 3


class IndexFetcher(object):
    def __init__(self, url):
        self.url = url
        self.refreshed_at = None
        self.data = {}
        self.index_names = None
        self.status = Status.failed

    def refresh(self):
        self.status = Status.updating
        r = requests.get(self.url)

        if r.ok:
            data = json.loads(r.text)
            self.refreshed_at = datetime.now()
            self.status = Status.success
        else:
            self.status = Status.failed

        return self.refreshed_at
