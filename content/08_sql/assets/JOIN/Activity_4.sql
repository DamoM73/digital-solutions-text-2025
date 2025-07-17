SELECT repair.job_numb, repair.owner, repair.type, repair.time, repair.time * devices.rate AS "Cost"
FROM repair
JOIN devices ON repair.type = devices.type
WHERE repair.ready = "Yes"