-- Component table has no foreign keys

CREATE TABLE "Component" (
	"component_id" INTEGER,
	"name" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	PRIMARY KEY("component_id" AUTOINCREMENT)
);