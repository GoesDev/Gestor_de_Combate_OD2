import tkinter as tk
from tkinter import ttk
from manageDatabase import add_monster, deleteMonster, showMonsterBestiary

root = tk.Tk()
root.title('Gestor de Combate OD2')
root.option_add("*Font", "Helvetica 20")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 15, "bold"))

frm = ttk.Frame(root, padding=10)
frm.grid()


# FUNÇÃO QUE ENVIA DADOS DE MONSTROS PARA O MÓDULO manageDatabase
# E LÁ USA A FUNÇÃO add_monster PARA ADICIONÁ-LOS AO BANCO
def addMonster():
    new_monster = (
        monster_name.get(),
        monster_armor_class.get(),
        monster_life_points.get()
    )
    add_monster(new_monster)
    monster_name.delete(0, 'end')
    monster_armor_class.delete(0, 'end')
    monster_life_points.delete(0, 'end')
    print(f"{new_monster[0].title()} adicionado!")


# FUNÇÃO QUE DELETA UM MONSTRO DO BANCO USANDO SEU NOME COMO REFERÊNCIA
def dltMonster():
    del_monster = monster_name.get()
    deleteMonster(del_monster)
    monster_name.delete(0, 'end')
    print(f"{del_monster.title()} removido!")


# FUNÇÃO QUE CRIA UMA JANELA PARA ADICIONAR MONSTROS AO BANCO
def window_add_monster():
    clear_widgets()
    ttk.Label(frm, text="Nome do Monstro").grid(column=0, row=0)
    ttk.Label(frm, text="CA").grid(column=0, row=1)
    ttk.Label(frm, text="PV").grid(column=0, row=2)

    global monster_name, monster_armor_class, monster_life_points
    monster_name = ttk.Entry(frm)
    monster_name.grid(column=1, row=0)
    monster_armor_class = ttk.Entry(frm)
    monster_armor_class.grid(column=1, row=1)
    monster_life_points = ttk.Entry(frm)
    monster_life_points.grid(column=1, row=2)

    ttk.Button(frm, text="Adicionar Monstro",
               command=addMonster).grid(column=1, row=3)
    ttk.Button(frm, text="Remover Monstro",
               command=dltMonster).grid(column=2, row=3)
    ttk.Button(frm, text="Home",
               command=window_home).grid(column=1, row=100)


# FUNÇÃO QUE LIMPA TODOS OS WIDGETS DA TELA
def clear_widgets():
    for widget in frm.winfo_children():
        widget.destroy()


# FUNÇÃO QUE MOSTRA O BESTIÁRIO
def window_show_bestiary():
    clear_widgets()
    monsters = showMonsterBestiary()

    # Criando Cabeçalhos
    headers = ['Name', 'Armor Class', 'Life Points']
    for col, header in enumerate(headers):
        ttk.Label(frm, text=header).grid(column=col, row=0)

    # Inserindo Dados
    for row_idx, row in enumerate(monsters, start=1):
        for col_idx, value in enumerate(row):
            ttk.Label(frm, text=value).grid(column=col_idx, row=row_idx)

    ttk.Button(frm, text="Home",
               command=window_home).grid(column=1, row=100)


def window_home():
    clear_widgets()

    ttk.Button(frm, text="Add/Del Monster",
               command=window_add_monster).grid(column=0, row=100)
    ttk.Button(frm, text="Show Bestiary",
               command=window_show_bestiary).grid(column=1, row=100)
    ttk.Button(frm, text="Quit",
               command=root.destroy).grid(column=2, row=100)


window_home()
root.mainloop()
