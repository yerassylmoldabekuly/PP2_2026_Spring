CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);


CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook (username, phone)
        VALUES (p_username, p_phone);
    END IF;

EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Phone already exists: %', p_phone;
    WHEN OTHERS THEN
        RAISE NOTICE 'Error: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_many_users(
    IN p_usernames VARCHAR[],
    IN p_phones VARCHAR[]
)
AS $$
DECLARE
    i INT;
    invalid_data TEXT := '';
BEGIN
    IF array_length(p_usernames, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have the same length';
    END IF;

    FOR i IN 1 .. array_length(p_usernames, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_usernames[i]) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE username = p_usernames[i];
            ELSE
                BEGIN
                    INSERT INTO phonebook (username, phone)
                    VALUES (p_usernames[i], p_phones[i]);
                EXCEPTION
                    WHEN unique_violation THEN
                        invalid_data := invalid_data || '(' || p_usernames[i] || ', ' || p_phones[i] || ') phone already exists; ';
                END;
            END IF;
        ELSE
            invalid_data := invalid_data || '(' || p_usernames[i] || ', ' || p_phones[i] || ') invalid phone; ';
        END IF;
    END LOOP;

    IF invalid_data <> '' THEN
        RAISE NOTICE 'Incorrect data: %', invalid_data;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value OR phone = p_value;

    IF NOT FOUND THEN
        RAISE NOTICE 'No user found with username or phone: %', p_value;
    END IF;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;