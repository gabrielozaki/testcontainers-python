-- create table
CREATE TABLE example_table (
	id serial NOT NULL,
	column1 VARCHAR(20) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE example_table2 (
    id serial NOT NULL,
    id_example_table1 INT NOT NULL,
    column2 VARCHAR(20) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_example_table1 FOREIGN KEY (id_example_table1) REFERENCES example_table (id)
);