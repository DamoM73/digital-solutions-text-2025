-- Table for foreign key exists

CREATE TABLE "Order" (
	"order_id"	INTEGER,
	"customer"	INTEGER NOT NULL,
	PRIMARY KEY("order_id" AUTOINCREMENT),
	FOREIGN KEY("customer") REFERENCES "Customer"("customer_id")
);