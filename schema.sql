-- Tabela de Clima
CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather_description VARCHAR(255),
    datetime TIMESTAMP
);

-- Tabela de Trânsito
CREATE TABLE traffic (
    id SERIAL PRIMARY KEY,
    summary VARCHAR(255),
    distance VARCHAR(255),
    duration VARCHAR(255),
    start_address VARCHAR(255),
    end_address VARCHAR(255),
    start_location JSONB,
    end_location JSONB,
    steps JSONB
);
