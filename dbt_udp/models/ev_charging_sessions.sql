SELECT
    vehicle_id
    , station_id
    , session_start
    , session_end
    , energy_kWh
    , duration_min
    , cost_usd
FROM
    {{ ref('ev_charging_logs') }}