/**
  DROP TABLES IF THEY EXIT
 */
DROP TABLE SELECTED;
DROP TABLE EXECUTION_TIME;
DROP TABLE DATA_A;
DROP TABLE DATA_B;
DROP TABLE DATA_C;
DROP TABLE DATA_D;
DROP TABLE DATA_E;
DROP TABLE DATA_F;
DROP TABLE DATA_G;
DROP TABLE DATA_H;

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
    script      varchar(20),
    table_char  varchar(1),
    chunk_size  int,
    chunk_start rowid,
    chunk_end   rowid,
    start_time  timestamp,
    end_time    timestamp
);

CREATE TABLE DATA_A
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_B
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_C
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_D
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_E
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_F
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_G
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

CREATE TABLE DATA_H
(
    name       varchar(50),
    first_name varchar(50),
    postcode   varchar(5),
    city       varchar(50),
    country    varchar(50),
    occupation varchar(100)
);

COMMIT;
