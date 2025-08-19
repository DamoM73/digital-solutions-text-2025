-- Students table has no foreign keys

CREATE TABLE "Students" (
	"student_id" INTEGER,
	"name" TEXT NOT NULL,
	"form" TEXT NOT NULL,
	PRIMARY KEY("student_id" AUTOINCREMENT)
);