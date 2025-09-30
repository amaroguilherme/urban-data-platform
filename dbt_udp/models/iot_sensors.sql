{{ 
    config(materialized='table') 
}}

SELECT
    energy_usage_kWh
    , co2_ppm AS air_quality_co2
    , pm25_ug_m3 AS air_quality_pm25
    , no2_ppb AS air_quality_no2
    , noise_dB
    , IF(parking_occupied=1, TRUE, FALSE) AS is_parking_occupied
    , timestamp AS created_at
FROM
    {{ ref('iot_sensors_data') }}
