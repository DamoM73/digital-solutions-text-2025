-- Tables of foreign keys exist

CREATE TABLE "Loan" (
	"book_id"	INTEGER,
	"student_id"	INTEGER,
	"borrow_date"	TEXT NOT NULL,
	"return_date"	TEXT,
	PRIMARY KEY("book_id","student_id"),
	FOREIGN KEY("book_id") REFERENCES "Book"("book_id"),
	FOREIGN KEY("student_id") REFERENCES "Students"("student_id")
);