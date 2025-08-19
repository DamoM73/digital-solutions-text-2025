CREATE TABLE "Book" (
	"book_id" INTEGER,
	"title" TEXT NOT NULL,
	"author" INTEGER NOT NULL,
	"genre" INTEGER NOT NULL,
	"year" INTEGER NOT NULL,
	PRIMARY KEY("book_id" AUTOINCREMENT),
	FOREIGN KEY("author") REFERENCES "Author"("author_id"),
	FOREIGN KEY("genre") REFERENCES "Genre"("genre_id")
);