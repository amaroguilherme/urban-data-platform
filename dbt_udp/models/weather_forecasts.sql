SELECT
    forecast_date
    , condition
    , temp_high_C
    , temp_low_C
    , precipitation_mm
    , humidity_percent
    , wind_speed_kmh
FROM
    {{ ref('weather_forecasts_data') }}