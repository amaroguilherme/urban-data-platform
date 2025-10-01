SELECT
    building_id
    , flow_rate_liters_min
    , daily_total_liters
    , leak_detected
    , timestamp AS created_at
FROM
    {{ ref('water_usage_logs') }}