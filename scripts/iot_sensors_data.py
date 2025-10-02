import csv
import random
import datetime

NUM_RECORDS = 500

OUTPUT_FILE = "dbt_udp/seeds/iot_sensors_data.csv"


def random_timestamp(start, end):
    """Generate a random datetime between start and end."""
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


def generate_data(num_records):
    start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        record = {
            "timestamp": random_timestamp(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S"),
            "energy_usage_kWh": round(random.uniform(0.1, 15.0), 2),  # kWh
            "co2_ppm": round(random.uniform(350, 1200), 1),          # ppm
            "pm25_ug_m3": round(random.uniform(5, 150), 1),          # µg/m³
            "no2_ppb": round(random.uniform(5, 200), 1),             # ppb
            "noise_dB": round(random.uniform(30, 100), 1),           # dB
            "parking_occupied": random.choice([0, 1])                # 0 = free, 1 = occupied
        }
        data.append(record)
    return data


def save_to_csv(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    data = generate_data(NUM_RECORDS)
    save_to_csv(data, OUTPUT_FILE)
    print(f"✅ Generated {NUM_RECORDS} records and saved to {OUTPUT_FILE}")
