/**
  DROP TABLES IF THEY EXIT
 */
DROP TABLE SELECTED;
DROP TABLE EXECUTION_TIME;
DROP TABLE PERSON_DATA_A;
DROP TABLE PERSON_DATA_B;
DROP TABLE PERSON_DATA_C;
DROP TABLE PERSON_DATA_D;

/*
  Create TABLES
 */
CREATE TABLE SELECTED
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE EXECUTION_TIME
(
    parallel   boolean,
    table_char varchar(1),
    chunk_size int,
    chunk_start rowid,
    chunk_end  rowid,
    start_time timestamp,
    end_time   timestamp
);

CREATE TABLE PERSON_DATA_A
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE PERSON_DATA_B
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE PERSON_DATA_C
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE PERSON_DATA_D
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

COMMIT;
