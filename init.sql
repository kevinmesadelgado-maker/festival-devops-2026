CREATE TABLE IF NOT EXISTS artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO artists (name) VALUES 
('The Kubernetes Symphony'),
('Continuous Integration DJ'),
('Microservices Echo'),
('The Docker Containers');