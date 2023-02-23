from email import message
from msilib.schema import Icon
from socket import timeout
import time
from turtle import title
from plyer import notification
from tkinter import *

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!",
            message = "It will reduce stress and most important good for your skin." , 
            app_icon = "C:/Users/mansi/Downloads/Glass-Water.ico",
            timeout = 10
            )
        time.sleep(60*60)

