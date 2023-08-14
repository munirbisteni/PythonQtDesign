-- 1o PASSO:

create schema biblioteca


CREATE TABLE biblioteca.Genero
(
	idGenero INT IDENTITY,
	descricao VARCHAR(20) NOT NULL,
	PRIMARY KEY (idGenero)
)


-- 2o PASSO:
CREATE TABLE biblioteca.Livro
(
	NumeroLivro INT IDENTITY,
	Titulo VARCHAR (50) NOT NULL,
	Prateleira VARCHAR (15) NOT NULL,
	ISBN VARCHAR (25) NOT NULL,
	Autor Varchar(50) NOT NULL,
	idGenero INT NOT NULL,
	FOREIGN KEY (idGenero)
		REFERENCES biblioteca.Genero(idGenero),
	PRIMARY KEY (NumeroLivro)
)

-- 3o PASSO:
CREATE TABLE biblioteca.Locatario
(
	registro INT IDENTITY,
	nome VARCHAR(30) NOT NULL,
	PRIMARY KEY (registro)
)

-- 4o PASSO:

CREATE TABLE biblioteca.Bibliotecario
(
	numeroBibliotecario INT IDENTITY,
	nome VARCHAR(30) NOT NULL,
	PRIMARY KEY (numeroBibliotecario)
)

--5o PASSO:

CREATE TABLE biblioteca.Emprestimo
(
	numeroEmprestimo INT IDENTITY,
	devolucaoStatus varchar(5),
	numeroLivro INT NOT NULL,
	numeroBibliotecario INT NOT NULL,
	registroLocatario INT NOT NULL,
	FOREIGN KEY (numeroLivro)
		REFERENCES biblioteca.Livro (NumeroLivro),
	FOREIGN KEY (numeroBibliotecario)
		REFERENCES biblioteca.Bibliotecario( NumeroBibliotecario),
	FOREIGN KEY (registroLocatario)
		REFERENCES biblioteca.Locatario(registro),
	PRIMARY KEY (numeroEmprestimo),
)
select * from biblioteca.Bibliotecario

DELETE FROM biblioteca.Bibliotecario WHERE numeroBibliotecario = 3