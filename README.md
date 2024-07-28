# Weather App

The "Weather App" repository contains a Python-based application that provides weather forecasting for various locations. It uses the OpenWeatherMap API to fetch real-time weather data, including temperature, pressure, humidity, wind speed, and more. The application is built with Tkinter for the GUI and integrates various features to enhance user experience.

## Features

- **Weather Forecasting**: Get real-time weather data for any location.
- **User Interface**: A user-friendly interface built with Tkinter.
- **City Suggestions**: Auto-suggestions for city names as you type.
- **Detailed Weather Information**: Displays temperature, pressure, humidity, wind speed, and cloud cover.
- **Error Handling**: Graceful handling of errors and API issues.

## Requirements

- ipywidgets
- requests
- tkinter
- Pillow (PIL)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Weather-App.git
    cd Weather-App
    ```

2. Install dependencies:

    ```bash
    pip install ipywidgets requests Pillow
    ```

## Usage

1. Set your OpenWeatherMap API key in the environment variable `OPENWEATHERMAP_API_KEY`. If you don't have one, the app uses a default key.

2. Run the script:

    ```bash
    python weather_app.py
    ```

3. Interact with the GUI to get weather information by entering a location and pressing "Generate Now".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact shivamdave172003@gmail.com.
