import csv
import random
import datetime

NUM_RECORDS = 500


def random_timestamp(start, end):
    """Generate a random datetime between start and end."""
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

# ---------- Bike-share trips ----------
def generate_bike_share(num_records):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        trip_start = random_timestamp(start_date, end_date)
        trip_duration = random.randint(5, 60)  # minutes
        trip_end = trip_start + datetime.timedelta(minutes=trip_duration)

        record = {
            "trip_start": trip_start.strftime("%Y-%m-%d %H:%M:%S"),
            "trip_end": trip_end.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_min": trip_duration,
            "distance_km": round(random.uniform(0.5, 15.0), 2),
            "bike_id": f"BIKE-{random.randint(1000, 9999)}",
            "station_start": f"ST-{random.randint(1, 100)}",
            "station_end": f"ST-{random.randint(1, 100)}"
        }
        data.append(record)
    return data

# ---------- EV charging logs ----------
def generate_ev_charging(num_records):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        session_start = random_timestamp(start_date, end_date)
        duration = random.randint(15, 300)  # minutes
        session_end = session_start + datetime.timedelta(minutes=duration)

        record = {
            "session_start": session_start.strftime("%Y-%m-%d %H:%M:%S"),
            "session_end": session_end.strftime("%Y-%m-%d %H:%M:%S"),
            "station_id": f"EVS-{random.randint(1, 50)}",
            "vehicle_id": f"EV-{random.randint(1000, 9999)}",
            "energy_kWh": round(random.uniform(5, 80), 1),
            "duration_min": duration,
            "cost_usd": round(random.uniform(2, 30), 2)
        }
        data.append(record)
    return data

# ---------- Ride-hailing trips ----------
def generate_ride_hailing(num_records):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        trip_start = random_timestamp(start_date, end_date)
        trip_duration = random.randint(5, 90)  # minutes
        trip_end = trip_start + datetime.timedelta(minutes=trip_duration)

        record = {
            "trip_start": trip_start.strftime("%Y-%m-%d %H:%M:%S"),
            "trip_end": trip_end.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_min": trip_duration,
            "distance_km": round(random.uniform(1.0, 30.0), 2),
            "fare_usd": round(random.uniform(5, 60), 2),
            "driver_id": f"DRV-{random.randint(1000, 9999)}",
            "vehicle_id": f"CAR-{random.randint(1000, 9999)}"
        }
        data.append(record)
    return data


def save_to_csv(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    bike_data = generate_bike_share(NUM_RECORDS)
    save_to_csv(bike_data, "temp/bike_share_trips.csv")

    ev_data = generate_ev_charging(NUM_RECORDS)
    save_to_csv(ev_data, "temp/ev_charging_logs.csv")

    ride_data = generate_ride_hailing(NUM_RECORDS)
    save_to_csv(ride_data, "temp/ride_hailing_trips.csv")

    print("✅ Generated datasets:")
    print("- bike_share_trips.csv")
    print("- ev_charging_logs.csv")
    print("- ride_hailing_trips.csv")
