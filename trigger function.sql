CREATE OR REPLACE FUNCTION update_user_name()
RETURNS TRIGGER AS $$
BEGIN
   
    IF OLD.name IS DISTINCT FROM NEW.name THEN
        INSERT INTO users_log(user_id, user_name, action)
        VALUES ( NEW.id, NEW.name, 'Name changed: from "' || OLD.name || '" to "' || NEW.name || '"');
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;



CREATE OR REPLACE TRIGGER log_user_update
AFTER UPDATE
ON users
FOR EACH ROW
EXECUTE FUNCTION update_user_name();

