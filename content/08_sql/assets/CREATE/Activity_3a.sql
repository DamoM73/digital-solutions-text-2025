-- Customer table has no foreign keys

CREATE TABLE "Customer" (
	"customer_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"email"	TEXT,
	"phone"	TEXT,
	PRIMARY KEY("customer_id" AUTOINCREMENT)
);