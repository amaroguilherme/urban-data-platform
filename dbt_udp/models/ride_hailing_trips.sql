SELECT
    driver_id
    , vehicle_id
    , trip_start
    , trip_end
    , duration_min
    , distance_km
    , fare_usd
FROM
    {{ ref('ride_hailing_trips_data') }}