#!/usr/bin/env python3
import math
import time
from typing import Optional

import requests


NAME = "jtprogru"
EMAIL = 'mail@example.com'
URL = 'https://google.com'

COUNTER = 5


def get_page(url: str) -> Optional[requests.Response]:
    try:
        res = requests.get(url)
        return res
    except:
        return None

def run() -> None:
    result = f"Name: {NAME}\nEmail: {EMAIL}\nOpened url: {URL}"
    print(result)
    for _ in range(COUNTER):
        time.sleep(0.5)
        page = get_page(URL)
        print(page.status_code)

if __name__ == '__main__':
    run()
