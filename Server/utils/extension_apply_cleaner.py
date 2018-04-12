from datetime import datetime
import time

from app.models.v2.apply import ExtensionApplyBase


def run():
    while True:
        if datetime.now().time().hour == 0:
            ExtensionApplyBase.objects.delete()
            time.sleep(1800)
