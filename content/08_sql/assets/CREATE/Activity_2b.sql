-- Genre table has no foreign keys

CREATE TABLE "Genre" (
	"genre_id" INTEGER,
	"name" TEXT NOT NULL,
	PRIMARY KEY("genre_id" AUTOINCREMENT)
);