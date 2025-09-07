# RainNotifier
Python Rain Alert System using OpenWeatherMap API, sending automated daily rain notifications via PythonAnywhere

🌧️ Rain Alert System
📌 Overview

The Rain Alert System is a Python-based project that sends daily weather alerts to notify users if it will rain in their location. It leverages the OpenWeatherMap API to fetch real-time weather data and is fully automated to run daily on PythonAnywhere.

This project is useful for anyone who wants to stay prepared for rainy days without checking weather apps manually.

🚀 Features

Fetches live weather data using OpenWeatherMap API

Checks daily forecast and alerts if rain is expected

Fully automated via PythonAnywhere scheduled tasks

Lightweight and easy to set up

🛠️ Tech Stack

Python 3

OpenWeatherMap API (for weather data)

Requests library (API calls)

PythonAnywhere (for automation & hosting)

⚙️ How It Works

The script connects to OpenWeatherMap API using your API key.

It fetches weather forecast data (temperature, conditions, rain probability, etc.).

If rain is expected, it triggers an alert (via console, email, or notification depending on setup).

The script is scheduled to run automatically every day using PythonAnywhere’s task scheduler.
