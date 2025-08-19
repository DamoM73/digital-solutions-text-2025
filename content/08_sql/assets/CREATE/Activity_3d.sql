-- Tables of foreign keys exist

CREATE TABLE "Order Products" (
	"order_id"	INTEGER,
	"product_id"	INTEGER,
	"quantity"	INTEGER NOT NULL,
	"price"	REAL NOT NULL,
	PRIMARY KEY("order_id","product_id"),
	FOREIGN KEY("order_id") REFERENCES "Order"("order_id"),
	FOREIGN KEY("product_id") REFERENCES "Product"("product_id")
);