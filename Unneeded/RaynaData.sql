-- Create a table for exercise data
CREATE TABLE ExerciseData (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Exercise VARCHAR(50),
    Reps INT,
    Performance DECIMAL(5, 2)
);

-- Insert data for Rayna
INSERT INTO ExerciseData (Name, Gender, Exercise, Reps, Performance)
VALUES ('Rayna', 'Female', 'Bicep Curls', 18, 90.00);

INSERT INTO ExerciseData (Name, Gender, Exercise, Reps, Performance)
VALUES ('Rayna', 'Female', 'Lateral Raises', 20, 87.00);