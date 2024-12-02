# weather_data.py - Module for fetching weather data

class WeatherDataFetcher:
    """Class to fetch weather data."""
    
    def __init__(self):
        # Simulated weather data
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_data(self, city):
        """Fetches weather data for a given city."""
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

# weather_parser.py - Module for parsing weather data

class WeatherDataParser:
    """Class to parse and format weather data."""

    @staticmethod
    def parse(data):
        """Parses weather data into a readable format."""
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# weather_forecast.py - Main Weather Forecast Application

class WeatherForecastApp:
    """Main class for the Weather Forecast Application."""

    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = WeatherDataParser()

    def get_detailed_forecast(self, city):
        """Provides a detailed weather forecast for a city."""
        data = self.fetcher.fetch_data(city)
        return self.parser.parse(data)

    def display_weather(self, city):
        """Displays the basic weather forecast for a city."""
        data = self.fetcher.fetch_data(city)
        if not data:
            return f"Weather data not available for {city}"
        return self.parser.parse(data)

    def run(self):
        """Runs the interactive weather forecast application."""
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                print("Goodbye!")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

# main.py - Entry point

if __name__ == "__main__":
    app = WeatherForecastApp()
    app.run()
