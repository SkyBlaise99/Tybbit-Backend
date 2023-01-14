CREATE TABLE usersRed (
    id      SERIAL  PRIMARY KEY,
    name    TEXT    NOT NULL,
    score   INT     NOT NULL
);

INSERT INTO usersRed (name, score) VALUES ('Wen Hao', 10);

SELECT * FROM usersRed ORDER BY score;

CREATE TABLE usersBlue (
    id      SERIAL  PRIMARY KEY,
    name    TEXT    NOT NULL,
    score   INT     NOT NULL
);

INSERT INTO usersBlue (name, score) VALUES ('Shi Chen', 11);
INSERT INTO usersBlue (name, score) VALUES ('Angler', 9);

SELECT * FROM usersBlue ORDER BY score;
