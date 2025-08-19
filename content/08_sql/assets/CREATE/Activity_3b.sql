-- Product table has no foreign keys

CREATE TABLE "Product" (
	"product_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"price"	REAL NOT NULL,
	"stock"	INTEGER NOT NULL,
	PRIMARY KEY("product_id" AUTOINCREMENT)
);