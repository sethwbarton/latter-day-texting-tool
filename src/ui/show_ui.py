import json

from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire.utils import decode
import tkinter as tk
import os

from src.core.parse_raw_ward_data import parse_raw_ward_data, WardMember


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
        print("Successfully scraped ward data from the site.")
        return json_data

    def draw_ui(self):
        self.window.title("Latter-day Texting Tool")

        def handle_button_press(event):
            self.member_list = parse_raw_ward_data(self.fetch_ward_data())
            self.save_member_list_to_csvs()

        button = tk.Button(text="Get Ward Data")
        button.bind("<Button-1>", handle_button_press)
        button.pack()

        # Start the event loop.
        self.window.mainloop()

    def save_member_list_to_csvs(self):
        csv_header = "Last Name,First Name,Mobile Phone,Note\n"

        # Elders Quorum CSV
        elders_quorum_items = ""
        relief_society_items = ""
        for member in self.member_list:
            if member.note == 'Elders Quorum':
                elders_quorum_items += member.to_csv_row()
            if member.note == 'Relief Society':
                relief_society_items += member.to_csv_row()

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        print("Writing Elder's Quorum CSV...")

        with open(os.path.join(desktop_path, "elders_quorum.csv"), "w") as file:
            file.write(csv_header + elders_quorum_items)

        print("Writing Relief Society CSV...")
        with open(os.path.join(desktop_path, "relief_society.csv"), "w") as file:
            file.write(csv_header + relief_society_items)

        print("File successfully written")

