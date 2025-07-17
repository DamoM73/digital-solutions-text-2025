SELECT teacher.tname, AVG(results.percent)
FROM teacher
JOIN subject ON teacher.tname = subject.tname
JOIN results ON subject.subjnumb = results.subjnumb
GROUP BY teacher.tname