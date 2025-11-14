-- Function for INSERT
CREATE OR REPLACE FUNCTION registerUser()
RETURNS TRIGGER AS $$
BEGIN 
    INSERT INTO users_log(user_id, user_name, action)
    VALUES (NEW.id, NEW.name, 'New user registered');
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

-- Trigger for INSERT
CREATE OR REPLACE TRIGGER log_user_insert
AFTER INSERT
ON users
FOR EACH ROW
EXECUTE FUNCTION registerUser();

-- Function for DELETE (fixed to use OLD instead of NEW)
CREATE OR REPLACE FUNCTION delete_it()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO users_log(user_id, user_name, action)
    VALUES (OLD.id, OLD.name, 'User deleted');
    RETURN OLD;
END;
$$
LANGUAGE plpgsql;

-- Trigger for DELETE (renamed to avoid conflict)
CREATE OR REPLACE TRIGGER log_user_delete
AFTER DELETE
ON users
FOR EACH ROW
EXECUTE FUNCTION delete_it();
