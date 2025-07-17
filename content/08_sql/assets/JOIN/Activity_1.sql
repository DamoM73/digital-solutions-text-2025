SELECT repair.job_numb, technicians.name
FROM repair
JOIN technicians ON repair.id_numb = technicians.id_numb