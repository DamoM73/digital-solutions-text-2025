SELECT technicians.name, experience.type
FROM technicians
JOIN experience ON technicians.id_numb = experience.id_numb
WHERE experience.qualification = "E"