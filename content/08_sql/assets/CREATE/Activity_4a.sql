-- Customer table has no foreign keys

CREATE TABLE "Customer" (
	"customer_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	PRIMARY KEY("customer_id" AUTOINCREMENT)
);