-- Table of foreign key exists

CREATE TABLE "Author" (
	"author_id"	INTEGER,
	"name" TEXT NOT NULL,
	"nationality" INTEGER NOT NULL,
	PRIMARY KEY("author_id" AUTOINCREMENT),
	FOREIGN KEY("nationality") REFERENCES "Nationality"("nationality_id")
);