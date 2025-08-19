-- Tables of foreign keys exist

CREATE TABLE "Product Components" (
	"product_id" INTEGER,
	"component_id" INTEGER,
	"quantity" INTEGER NOT NULL,
	PRIMARY KEY("product_id","component_id"),
	FOREIGN KEY("component_id") REFERENCES "Component"("component_id"),
	FOREIGN KEY("product_id") REFERENCES "Product"("product_id"),
	FOREIGN KEY("quantity") REFERENCES ""
);