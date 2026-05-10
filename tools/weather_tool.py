import requests
import flyte

from langchain_core.tools import tool


def _geocode_location(location: str):

    response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": location,
            "count": 1,
        },
    )

    data = response.json()

    if "results" not in data:
        return None

    return (
        data["results"][0]["latitude"],
        data["results"][0]["longitude"],
    )


@tool("get_weather_forecast")
@flyte.trace
def get_weather_forecast(
    location: str,
    date: str
) -> str:

    """
    Fetch weather forecast for a given location and date.
    """

    coordinates = _geocode_location(location)

    if coordinates is None:
        return f"Location not found: {location}"

    latitude, longitude = coordinates

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
            "start_date": date,
            "end_date": date,
            "timezone": "UTC",
        },
    )

    data = response.json()

    times = data["hourly"]["time"][:5]
    temps = data["hourly"]["temperature_2m"][:5]

    forecast = []

    for t, temp in zip(times, temps):

        forecast.append(
            f"{t}: {temp}°C"
        )

    return (
        f"Weather forecast for {location} "
        f"on {date}:\n" +
        "\n".join(forecast)
    )
