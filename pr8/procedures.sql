-- 2. Upsert: вставить нового или обновить телефон существующего
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- 3. Массовая вставка с проверкой телефона.
-- Возвращает (через INOUT) список некорректных данных вида 'имя:телефон'.
-- Корректный телефон: необязательный '+', затем 10-15 цифр.
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names  VARCHAR[],
    p_phones VARCHAR[],
    INOUT p_invalid TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    n INT := COALESCE(array_length(p_names, 1), 0);
BEGIN
    p_invalid := ARRAY[]::TEXT[];

    IF n <> COALESCE(array_length(p_phones, 1), 0) THEN
        RAISE EXCEPTION 'names and phones arrays must have the same length';
    END IF;

    FOR i IN 1..n LOOP
        IF p_names[i] IS NULL OR btrim(p_names[i]) = ''
           OR p_phones[i] IS NULL OR p_phones[i] !~ '^\+?[0-9]{10,15}$' THEN
            p_invalid := p_invalid || (COALESCE(p_names[i], 'NULL') || ':' || COALESCE(p_phones[i], 'NULL'));
        ELSE
            CALL upsert_contact(p_names[i], p_phones[i]);
        END IF;
    END LOOP;
END;
$$;

-- 5. Удаление по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p_value OR phone = p_value;
    IF NOT FOUND THEN
        RAISE NOTICE 'No contact found for "%"', p_value;
    END IF;
END;
$$;
