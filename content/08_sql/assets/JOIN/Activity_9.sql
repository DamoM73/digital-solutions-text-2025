SELECT subject.subjname AS "Subject", student.gender AS "Gender", COUNT(student.gender) AS "Enroled"
FROM subject
JOIN results ON subject.subjnumb = results.subjnumb
JOIN student ON results.stnumb = student.stnumb
GROUP BY subject.subjname, student.gender