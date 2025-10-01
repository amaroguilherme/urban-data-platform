SELECT
    bike_id
    , trip_start
    , trip_end
    , duration_min
    , distance_km
    , station_start
    , station_end
FROM
    {{ ref('bike_share_trips_data') }}