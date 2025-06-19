CREATE DATABASE student_registration;

USE student_registration;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    gender VARCHAR(10),
    emergency_contact VARCHAR(15),
    payment_mode VARCHAR(50),
    remember_me BOOLEAN DEFAULT 0
);

