-- Supplier table has no foreign keys

CREATE TABLE "Supplier" (
	"supplier_id" INTEGER,
	"name" TEXT NOT NULL,
	"email" TEXT NOT NULL,
	PRIMARY KEY("supplier_id" AUTOINCREMENT)
);