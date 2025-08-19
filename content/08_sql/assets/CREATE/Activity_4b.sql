-- Item table has no foreign keys

CREATE TABLE "Item" (
	"item_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"price"	REAL NOT NULL,
	PRIMARY KEY("item_id" AUTOINCREMENT)
);