import sqlite3

# CRIANDO CONEXÃO COM O BANCO
con = sqlite3.connect("gestor_de_combate.db")

# CRIANDO CURSOR
cur = con.cursor()


# CRIANDO CONEXÃO COM O BANCO
def openDatabase():
    # CRIANDO CONEXÃO COM O BANCO
    conn = sqlite3.connect("gestor_de_combate.db")
    return conn


# ADICIONANDO character NA TABELA character
def add_character(new_character):
    con = openDatabase()
    cur = con.cursor()
    sql_insert_character = """
        INSERT INTO character
        VALUES (?,
        ?,
        ?)
    """
    cur.execute(sql_insert_character, new_character)
    con.commit()
    con.close()


# ADICIONANDO monster NA TABELA monster
def add_monster(new_monster):
    con = openDatabase()
    cur = con.cursor()
    sql_insert_monster = """
        INSERT INTO monster (name,
        armor_class,
        life_points)
        VALUES (?,
        ?,
        ?)
    """
    cur.execute(sql_insert_monster, new_monster)
    con.commit()
    # FECHANDO CONEXÃO COM O BANCO
    con.close()


# BUSCANDO character NA TABELA character
def selectCharacter(character_name):
    sql_select_character = """
        SELECT *
        FROM character
        WHERE name = ?
    """
    character = cur.execute(sql_select_character, (character_name,))
    return character.fetchone()


# BUSCANDO monster NA TABELA monster
def selectMonster(monster_name):
    sql_select_monster = """
        SELECT *
        FROM monster
        WHERE name = ?
    """
    character = cur.execute(sql_select_monster, (monster_name,))
    return character.fetchone()


# ATUALIZANDO monster NA TABELA monster
def updateMonster(att_monster):
    sql_update = """
        UPDATE monster
        SET name = ?,
            life_points = ?
        WHERE armor_class = ?
    """
    cur.execute(sql_update, att_monster)
    con.commit()


# ATUALIZANDO character NA TABELA character
def updateCharacter(att_character):
    sql_update = """
        UPDATE character
        SET armor_class = ?,
            life_points = ?
        WHERE name = ?
    """
    cur.execute(sql_update, att_character)
    con.commit()


# MOSTRANDO TODOS OS monster DA TABELA monster
# ORDENADOS POR NOME
def showMonsterBestiary():
    con = openDatabase()
    cur = con.cursor()
    sql_select_all_monsters = """
        SELECT *
        FROM monster
        ORDER BY name
    """
    cur.execute(sql_select_all_monsters)
    all_monsters = cur.fetchall()
    con.close()
    return all_monsters


# MONSTRANDO TODOS OS character DA TABELA character
# ORDENADOS POR NOME
def showCharacterList():
    con = openDatabase()
    cur = con.cursor()
    sql_select_all_characters = """
        SELECT *
        FROM character
        ORDER BY name
    """
    cur.execute(sql_select_all_characters)
    all_characters = cur.fetchall()
    return all_characters


# DELETANDO monster DA TABELA monster USANDO name COMO REFERÊNCIA name
def deleteMonster(del_monster):
    sql_delete_monster = """
        DELETE FROM monster
        WHERE name = ?
    """
    cur.execute(sql_delete_monster, (del_monster,))
    con.commit()


# DELETANDO monster DA TABELA monster USANDO name COMO REFERÊNCIA name
def deleteCharacter(del_character):
    sql_delete_character = """
        DELETE FROM character
        WHERE name = ?
    """
    cur.execute(sql_delete_character, (del_character,))
    con.commit()
