# Api
# from api.models import Artist
import os
from datetime import datetime


def printHello():
    with open(
            os.environ['HOME']+f"/cron_test/test{datetime.now().minute}.txt", "w+") as file:
        file.write("This is a test file created with a crontab\n")
        file.close()
