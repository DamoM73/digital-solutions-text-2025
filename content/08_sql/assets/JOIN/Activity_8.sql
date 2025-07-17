SELECT student.stname AS "Student", subject.subjname AS "Subject", results.percent AS "Result"
FROM student
JOIN results ON student.stnumb = results.stnumb
JOIN subject ON results.subjnumb = subject.subjnumb
