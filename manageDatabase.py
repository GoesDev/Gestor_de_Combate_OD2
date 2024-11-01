import sqlite3

# CRIANDO CONEXÃO COM O BANCO
con = sqlite3.connect("gestor_de_combate.db")

# CRIANDO CURSOR
cur = con.cursor()

# # cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("CREATE TABLE monster(name, armor_class, life_points)")
# cur.execute("CREATE TABLE character(name, armor_class, life_points)")


# ADICIONANDO PERSONAGENS NA TABELA character
def add_character(name, armor_class, life_points):
    dados = (name, armor_class, life_points)
    cur.execute("INSERT INTO character VALUES (? ,?, ?)", dados)
    con.commit()


# ADICIONANDO MONSTROS NA TABELA monster
def add_monster(name, armor_class, life_points):
    dados = (name, armor_class, life_points)
    cur.execute("INSERT INTO monster VALUES (? ,?, ?)", dados)
    con.commit()


# add_monster('Zombie', 12, 10)
# add_character('CiCi Fucarão', 11, 16)

# res = cur.execute('SELECT name FROM sqlite_master')
# print(res.fetchone())

def selectMonster(name):
    monster = cur.execute(f"SELECT * FROM monster WHERE name ='{name}'")
    return monster.fetchone()


monster = selectMonster('Zombie')
print(monster)

# FECHANDO CONEXÃO COM O BANCO
con.close()
