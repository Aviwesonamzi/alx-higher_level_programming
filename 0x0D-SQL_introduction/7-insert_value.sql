-- Insert a new row into first_table with id = 89 and name = Best School
INSERT INTO first_table (id, name)
SELECT 89, 'Best School'
WHERE NOT EXISTS (
    SELECT 1 FROM first_table WHERE id = 89 AND name = 'Best School'
);
