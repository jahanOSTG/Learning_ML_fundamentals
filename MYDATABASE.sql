-- Drop and recreate schema

DROP SCHEMA IF EXISTS janie;
CREATE SCHEMA janie;
USE janie;

-- Table for grandfather
CREATE TABLE grandfather (
    id INT PRIMARY KEY NOT NULL,
    grandparent_id INT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

-- Table for grandfather's siblings
CREATE TABLE grandfather_siblings (
    id INT PRIMARY KEY NOT NULL,
    grandparent_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100),
    FOREIGN KEY (grandparent_id) REFERENCES grandfather(id)
);

-- Table for father (required for foreign key in father_gifts)
CREATE TABLE father (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

-- Table for father's gift history
CREATE TABLE father_gifts (
    id INT PRIMARY KEY NOT NULL,
    father_id INT NOT NULL,
    from_relative_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    estimated_value DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (father_id) REFERENCES father(id)
);

INSERT INTO grandfather VALUES
(1, 01, 'Abdul Karim', 85),
(2, 02, 'Mohammad Rahim', 83);


INSERT INTO grandfather_siblings VALUES
(1, 1, 'Fatema Begum', '1945-03-12', 79, 'fatema@example.com'),
(2, 1, 'Ali Hossain', '1948-11-25', 76, 'ali.hossain@example.com'),
(3, 2, 'Salma Khatun', '1950-06-10', 74, 'salma@example.com');


INSERT INTO father (id, name, age)
VALUES
(1, 'Md. Habib', 55),
(2, 'Md. Karim', 53);

INSERT INTO father_gifts (id, father_id, from_relative_name, birth_date, estimated_value)
VALUES
(1, 1, 'Fatema Begum', '2023-02-14', 1500.00),
(2, 1, 'Ali Hossain', '2022-08-01', 2000.50),
(3, 2, 'Salma Khatun', '2024-05-20', 1800.00);




