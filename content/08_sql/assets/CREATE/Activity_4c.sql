-- Tables of foreign keys exist

CREATE TABLE "Orders" (
	"customer_id"	INTEGER,
	"item_id"	INTEGER,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("customer_id","item_id"),
	FOREIGN KEY("customer_id") REFERENCES "Customer"("customer_id"),
	FOREIGN KEY("item_id") REFERENCES "Item"("item_id")
);