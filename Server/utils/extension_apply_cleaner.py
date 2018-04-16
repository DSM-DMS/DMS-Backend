from datetime import datetime
import time

from app.models.v2.apply import ExtensionApply11Model, ExtensionApply12Model


def run():
    while True:
        if 0 < datetime.now().time().hour < 12:
            ExtensionApply11Model.objects.delete()
            ExtensionApply12Model.objects.delete()
            time.sleep(3600)
