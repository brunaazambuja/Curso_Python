
#PARA FAZER PELO PYTHON: -----------------------------------------------------------

import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

connection = MySQLdb.connect(host, user, password, db, port)
c = connection.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where = None):
    
    global c

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

# --------------------------------------------------------------------------------------------

result = select("nome, cpf", "alunos", "id_aluno = 1")
print(result[0]["cpf"])

# --------------------------------------------------------------------------------------------

def insert(values, table, fields = None):

    global c, connection

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
        query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
    
    c.execute(query)
    connection.commit()

    return

# --------------------------------------------------------------------------------------------

values = ["DEFAULT, 'Joao Pedro', '2000-01-01', 'Av da Pedras, 123', 'Brasilia', 'DF', '12345678911'", 
    "DEFAULT, 'Maria Cavalcante', '2000-01-01', 'Av da Pedras, 123', 'Brasilia', 'DF', '12345678911'"]

insert(values, "alunos")
select("*", "alunos")

# --------------------------------------------------------------------------------------------

def update(sets, table, where = None):

    global c, connection

    query = "UPDATE " + table + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    connection.commit()

    return

# --------------------------------------------------------------------------------------------

update({"nome":"Joao Pedro", "cidade":"Curitiba", "alunos", "id_aluno = 8"})
select("*", "alunos", "id_aluno = 8")

# --------------------------------------------------------------------------------------------

def delete(table, where):

    global c, connection

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    connection.commit()


# --------------------------------------------------------------------------------------------

select("*", "alunos", "id_aluno = 9")
delete("alunos", "id_aluno = 9")

# --------------------------------------------------------------------------------------------
