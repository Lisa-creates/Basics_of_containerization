import sqlite3

connection = sqlite3.connect('data/db.sqlite')
cursor = connection.cursor()

create_table_command = '''
CREATE TABLE IF NOT EXISTS Courses (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    teacher VARCHAR(100)
);
'''
create_data_command = '''
INSERT INTO Courses VALUES 
(1, "Probability Theory", "Kolmogorov A.N."), 
(2, "Mathematical Analysis", "Leonhard Euler");
'''

try:
    cursor.execute(create_table_command)
    cursor.execute(create_data_command)
except sqlite3.IntegrityError:
    print("Insertion skipped")
finally:
    connection.commit()
    connection.close()

