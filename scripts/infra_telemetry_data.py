import csv
import random
import datetime

NUM_RECORDS = 500


def random_timestamp(start, end):
    """Generate a random datetime between start and end."""
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

# ---------- Building energy efficiency ----------
def generate_building_energy(num_records):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        report_date = random_timestamp(start_date, end_date)

        record = {
            "report_date": report_date.strftime("%Y-%m-%d"),
            "building_id": f"BLDG-{random.randint(100, 999)}",
            "energy_consumption_kWh": round(random.uniform(1000, 20000), 1),  # total consumption
            "area_m2": random.randint(500, 5000),  # building size
            "efficiency_score": round(random.uniform(0.5, 1.0), 2),  # normalized 0-1
            "hvac_usage_percent": round(random.uniform(20, 70), 1),  # %
            "lighting_usage_percent": round(random.uniform(10, 40), 1),  # %
        }
        data.append(record)
    return data

# ---------- Water usage logs ----------
def generate_water_usage(num_records):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

    data = []
    for _ in range(num_records):
        log_time = random_timestamp(start_date, end_date)

        record = {
            "timestamp": log_time.strftime("%Y-%m-%d %H:%M:%S"),
            "building_id": f"BLDG-{random.randint(100, 999)}",
            "flow_rate_liters_min": round(random.uniform(10, 500), 1),
            "daily_total_liters": round(random.uniform(500, 10000), 1),
            "leak_detected": random.choice([0, 1])  # 0 = no leak, 1 = leak
        }
        data.append(record)
    return data


def save_to_csv(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    energy_data = generate_building_energy(NUM_RECORDS)
    save_to_csv(energy_data, "temp/building_energy_reports.csv")

    water_data = generate_water_usage(NUM_RECORDS)
    save_to_csv(water_data, "temp/water_usage_logs.csv")

    print("✅ Generated datasets:")
    print("- building_energy_reports.csv")
    print("- water_usage_logs.csv")
