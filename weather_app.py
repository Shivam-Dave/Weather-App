#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ipywidgets')
get_ipython().system('pip install requests')


# In[2]:


import ipywidgets as widgets
from IPython.display import display, HTML
import requests
from ipywidgets import HBox, VBox
import os


# In[3]:


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import os

# Define API key and URLs
api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
if not api_key:
    api_key = "de90b6d110d9af62479879569657bd8f"  

api_url = "http://api.openweathermap.org/data/2.5/weather"
cities_api_url = "http://api.openweathermap.org/data/2.5/find"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecasting App")

        # Set initial window size and center the window
        window_width, window_height = 900, 600
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(True, True)

        # Load background image and convert it to PhotoImage
        background_path = r'C:\Users\acer\OneDrive\Desktop\weather app.png'  
        pil_image = Image.open(background_path)
        self.background_image = ImageTk.PhotoImage(pil_image.resize((window_width, window_height), Image.ANTIALIAS))

        # Create background label
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Bind window resize event to resize background function
        self.root.bind('<Configure>', self.resize_background)

        # Create heading
        self.heading_label = tk.Label(root, text="Weather Forecasting App", font=("Arial", 24, "bold"), fg="black")
        self.heading_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create location frame
        self.location_frame = tk.Frame(root, bg='white')
        self.location_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Create location label and combobox
        self.location_label = tk.Label(self.location_frame, text="Location:", font=("Arial", 14, "bold"), bg='white')
        self.location_label.grid(row=0, column=0, padx=5)
        self.city_combobox = ttk.Combobox(self.location_frame, font=("Arial", 14), width=30)
        self.city_combobox.grid(row=0, column=1, padx=5)
        self.city_combobox.bind("<KeyRelease>", self.on_key_release)

        # Bind the "Enter" key to the `get_weather` function
        self.root.bind('<Return>', self.get_weather)

        # Create "Generate Now" button below the location frame
        self.get_weather_button = ttk.Button(
            root,
            text="Generate Now",
            command=self.get_weather,
            style='TButton',
            width=15  # Decrease button width
        )
        # Place the button higher and center it
        self.get_weather_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Create frame to hold weather information labels
        # Decrease the width of the weather frame by adjusting the `relwidth` property
        # Keep the height same and centered
        self.weather_frame = tk.Frame(root, bg='white')
        self.weather_frame.place(relx=0.5, rely=0.5, anchor=tk.N, relwidth=0.35, relheight=0.45)

        # Create a list of labels for weather data
        self.weather_labels = {
            'location': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'temperature': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'pressure': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'humidity': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'description': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'wind_speed': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w'),
            'cloud_cover': tk.Label(self.weather_frame, font=("Arial", 14), bg='white', anchor='w')
        }

        # Place labels in the frame
        for i, (key, label) in enumerate(self.weather_labels.items()):
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)

        # Apply styles to components
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14, 'bold'), background='white', foreground='black')

    # Function to resize background image
    def resize_background(self, event=None):
        new_width = self.root.winfo_width()
        new_height = self.root.winfo_height()
        pil_image = Image.open(r'C:\Users\acer\OneDrive\Desktop\weather app.png')  # Replace with your image path
        resized_image = pil_image.resize((new_width, new_height), Image.ANTIALIAS)
        new_background_image = ImageTk.PhotoImage(resized_image)

        # Update the background label with the new image
        self.background_label.config(image=new_background_image)

        # Keep a reference to the new image to prevent garbage collection
        self.background_label.image = new_background_image

    # Function to fetch and display weather data
    def get_weather(self, event=None):
        location = self.city_combobox.get()
        if location:
            params = {
                "q": location,
                "appid": api_key,
                "units": "metric"  # Using metric units (Celsius) for temperature
            }
            response = requests.get(api_url, params=params)
            data = response.json()

            # Check for errors in the API response
            if response.status_code != 200 or 'message' in data:
                messagebox.showerror("Weather App", f"Error: {data.get('message', 'Unknown error')} (Status code: {response.status_code})")
                return

            # Extract relevant information and update labels
            try:
                self.weather_labels['location'].config(text=f"Weather in {location.title()}")
                self.weather_labels['temperature'].config(text=f"Temperature: {data['main']['temp']}°C")
                self.weather_labels['pressure'].config(text=f"Pressure: {data['main']['pressure']} hPa")
                self.weather_labels['humidity'].config(text=f"Humidity: {data['main']['humidity']}%")
                self.weather_labels['description'].config(text=f"Description: {data['weather'][0]['description'].title()}")
                self.weather_labels['wind_speed'].config(text=f"Wind Speed: {data['wind']['speed']} m/s")
                self.weather_labels['cloud_cover'].config(text=f"Cloud Cover: {data['clouds']['all']}%")
            except KeyError as e:
                messagebox.showerror("Weather App", f"Error: Missing key in response: {e}")

    # Function to handle key release event for city suggestions
    def on_key_release(self, event=None):
        query = self.city_combobox.get().strip()
        if not query:
            self.city_combobox.set('')
            self.city_combobox['values'] = []
            return

        # Implement a delay to avoid lag in the input box
        self.root.after(200, self.fetch_city_suggestions, query)

    # Function to fetch city suggestions based on the user's input
    def fetch_city_suggestions(self, query):
        if query == self.city_combobox.get().strip():
            params = {
                "q": query,
                "appid": api_key,
                "type": "like",
                "sort": "population",
                "cnt": 10  # Limit the number of suggestions to 10
            }
            response = requests.get(cities_api_url, params=params)
            data = response.json()

            # Filter city names and add them to the combobox
            if 'list' in data:
                suggestions = [f"{city['name']}, {city['sys']['country']}" for city in data['list']]
                self.city_combobox['values'] = suggestions

# Create the Tkinter window and initialize the app
root = tk.Tk()
app = WeatherApp(root)

# Start the Tkinter main loop
root.mainloop()


# In[ ]:




