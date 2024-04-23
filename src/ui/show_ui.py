import json

from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire.utils import decode
import tkinter as tk
import Contacts as appleContacts

from src.core.parse_raw_ward_data import parse_raw_ward_data


class UI:
    window = None
    member_list = None

    def __init__(self):
        self.window = tk.Tk()

    def fetch_ward_data(self):
        driver = webdriver.Chrome()
        driver.get("https://lcr.churchofjesuschrist.org/records/member-list?lang=eng")

        # The timeout here allows people have time to enter their username / password
        # and then load the member list. This will wait ten minutes.
        request = driver.wait_for_request("https://lcr.churchofjesuschrist.org/api/umlu/report/member-list",
                                          timeout=600)
        json_data = json.loads(
            decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))
        driver.close()

        self.member_list = parse_raw_ward_data(json_data)

    def draw_ui(self):
        window = tk.Tk()
        window.title("Latter-day Texting Tool")

        def handle_button_press(event):
            self.fetch_ward_data()
            window.destroy()

        button = tk.Button(text="Get Ward Data")
        button.bind("<Button-1>", handle_button_press)
        button.pack()

        # Start the event loop.
        window.mainloop()


    def add_member_to_contacts(self):
        pass

