CREATE TABLE users (
    id      SERIAL  PRIMARY KEY,
    name    TEXT    NOT NULL,
    score   INT     NOT NULL,
);

INSERT INTO users (name, score) VALUES ('Wen Hao', 10);
INSERT INTO users (name, score) VALUES ('Shi Chen', 11);
INSERT INTO users (name, score) VALUES ('Angler', 9);

SELECT * FROM users;
