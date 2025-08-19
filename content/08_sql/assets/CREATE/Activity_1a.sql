-- Product table has no foreign keys

CREATE TABLE "Product" (
	"product_id" INTEGER,
	"name" TEXT NOT NULL,
	"quantity" INTEGER NOT NULL,
	PRIMARY KEY("product_id" AUTOINCREMENT)
);