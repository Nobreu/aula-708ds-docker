CREATE TABLE IF NOT EXISTS usuariosflask
(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

INSERT INTO usuariosflask (nome) VALUES ('Alice'), ('Bob'), ('Egberto')