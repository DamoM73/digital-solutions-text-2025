SELECT grade, gender, COUNT(stnumb)
FROM student
GROUP BY grade, gender