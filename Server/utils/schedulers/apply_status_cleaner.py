from datetime import datetime
from multiprocessing import Process
from time import sleep

from app.models.account import StudentModel


def clean_extension_apply(sleep_seconds):
    while True:
        now = datetime.now()
        if 0 < now.hour < 2:
            for student in StudentModel.objects:
                student.update(extension_apply_11=None, extension_apply_12=None)

        sleep(sleep_seconds)


def run():
    process__extension_apply_cleaner = Process(target=clean_extension_apply, args=(3600,))
    process__extension_apply_cleaner.start()
