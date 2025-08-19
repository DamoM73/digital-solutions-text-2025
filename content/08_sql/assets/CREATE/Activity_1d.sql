-- Tables for foreign keys exist

CREATE TABLE "Component Supplier" (
	"component_id" INTEGER,
	"supplier_id" INTEGER,
	PRIMARY KEY("component_id","supplier_id"),
	FOREIGN KEY("component_id") REFERENCES "Component"("component_id"),
	FOREIGN KEY("supplier_id") REFERENCES "Supplier"("supplier_id")
);