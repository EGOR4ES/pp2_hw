-- Таблица из Practice 7 (создаётся, только если её ещё нет)
CREATE TABLE IF NOT EXISTS contacts (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    phone VARCHAR(20)  NOT NULL
);

-- 1. Поиск по шаблону (часть имени или телефона)
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    WHERE c.name  ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%'
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;

-- 4. Постраничный вывод (LIMIT / OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    IF p_limit IS NULL OR p_limit <= 0 THEN
        RAISE EXCEPTION 'limit must be positive, got %', p_limit;
    END IF;
    IF p_offset IS NULL OR p_offset < 0 THEN
        RAISE EXCEPTION 'offset must be >= 0, got %', p_offset;
    END IF;

    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
