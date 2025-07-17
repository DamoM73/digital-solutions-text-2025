SELECT repair.id_numb, technicians.name, repair.type, repair.owner, repair.ready
FROM repair
JOIN technicians ON repair.id_numb = technicians.id_numb
ORDER BY repair.ready DESC