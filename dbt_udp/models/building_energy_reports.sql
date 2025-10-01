SELECT
    building_id
    , energy_consumption_kWh
    , area_m2
    , efficiency_score
    , hvac_usage_percent
    , lighting_usage_percent
    , report_date
FROM
    {{ ref('building_energy_data') }}