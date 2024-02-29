CREATE TABLE IF NOT EXISTS PG_REACTIONS (
  EVENT_ID     VARCHAR(255) PRIMARY KEY,
  GENERATED_AT BIGINT,
  REACTION     VARCHAR(255),
  USER_EMAIL   VARCHAR(255),
  USER_IP      VARCHAR(255)
);


-- Create the zodiac table
CREATE TABLE zodiac (
    id          INT PRIMARY KEY,
    symbol      VARCHAR(255),
    element     VARCHAR(255),
    start_date  DATE,
    end_date    DATE,
    emoji       VARCHAR(255)
);

-- Insert rows into the zodiac table
INSERT INTO zodiac (id, symbol, element, start_date, end_date, emoji)
VALUES 
(1, 'Aries', 'Fire', '2024-03-21', '2024-04-19', '♈'),
(2, 'Taurus', 'Earth', '2024-04-20', '2024-05-20', '♉'),
(3, 'Gemini', 'Air', '2024-05-21', '2024-06-20', '♊'),
(4, 'Cancer', 'Water', '2024-06-21', '2024-07-22', '♋'),
(5, 'Leo', 'Fire', '2024-07-23', '2024-08-22', '♌'),
(6, 'Virgo', 'Earth', '2024-08-23', '2024-09-22', '♍'),
(7, 'Libra', 'Air', '2024-09-23', '2024-10-22', '♎'),
(8, 'Scorpio', 'Water', '2024-10-23', '2024-11-21', '♏'),
(9, 'Sagittarius', 'Fire', '2024-11-22', '2024-12-21', '♐'),
(10, 'Capricorn', 'Earth', '2024-12-22', '2025-01-19', '♑'),
(11, 'Aquarius', 'Air', '2025-01-20', '2025-02-18', '♒'),
(12, 'Pisces', 'Water', '2025-02-19', '2025-03-20', '♓');



CREATE TABLE logins
( brand_code          character varying(32)                not null ,
 application_code    character varying(32)                not null ,
 platform_code       character varying(64)                not null ,
 hardware_device_id  text                                 not null ,
 device_id           uuid                                 not null ,
 created_at          timestamp with time zone             not null ,
 expires_at          timestamp with time zone             not null ,
PRIMARY KEY (hardware_device_id, brand_code, application_code, platform_code)
);

insert into logins select md5(random()::text), md5(random()::text), md5(random()::text), md5(random()::text), gen_random_uuid(), now(), now()+trunc(random()*10)* '1 day'::interval
FROM generate_series(1,100) id;