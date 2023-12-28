# Import the required modules
import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather information from OpenWeatherMap API
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            result_str = f"Weather in {city}: {temperature}°C, {description}"
            # Update the result label in the GUI
            result_label.config(text=result_str)
        else:
            # Display an error message if the API request was not successful
            messagebox.showerror("Error", f"Error: {data['message']}")

    except Exception as e:
        # Display an error message for any exceptions that occur
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle button click event
def get_weather_button_clicked():
    city = city_entry.get()
    # Call the get_weather function with the provided city and API key
    get_weather(api_key, city)

# Replace with your OpenWeatherMap API key
api_key = "a1f10c6942e00c38745630c4d8afbbe5"

# GUI setup
app = tk.Tk()  # Create a Tkinter application window
app.title("Weather App")  # Set the window title

# Widgets (GUI components)
city_label = tk.Label(app, text="Enter City:")  # Label for city entry
city_entry = tk.Entry(app)  # Entry widget for entering the city name
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_button_clicked)  # Button to trigger weather retrieval
result_label = tk.Label(app, text="")  # Label to display weather information

# Widget placement using grid layout
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
city_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
app.mainloop()
