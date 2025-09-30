import csv
import random
import datetime

NUM_RECORDS = 500
OUTPUT_FILE = "temp/weather_forecasts.csv"


def random_date(start, end):
    """Generate a random date between start and end."""
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))

def generate_weather_forecasts(num_records):
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rain", "Thunderstorm", "Snow", "Fog"]

    data = []
    for _ in range(num_records):
        forecast_date = random_date(start_date, end_date)

        high_temp = round(random.uniform(-10, 40), 1)   # °C
        low_temp = high_temp - random.uniform(2, 15)    # °C
        precipitation_mm = round(random.uniform(0, 50), 1) if random.random() < 0.6 else 0.0
        humidity = random.randint(20, 100)              # %
        wind_speed = round(random.uniform(0, 60), 1)    # km/h
        condition = random.choice(conditions)

        record = {
            "forecast_date": forecast_date.strftime("%Y-%m-%d"),
            "condition": condition,
            "temp_high_C": high_temp,
            "temp_low_C": round(low_temp, 1),
            "precipitation_mm": precipitation_mm,
            "humidity_percent": humidity,
            "wind_speed_kmh": wind_speed
        }
        data.append(record)
    return data

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    weather_data = generate_weather_forecasts(NUM_RECORDS)
    save_to_csv(weather_data, OUTPUT_FILE)
    print(f"✅ Generated {NUM_RECORDS} weather forecast records and saved to {OUTPUT_FILE}")
