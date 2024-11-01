# Gestor_de_Combate_OD2
Um simples gerenciador de combate para Old Dragon 2e, um sistema de RPG de mesa nacional.

# Componentes Principais:
- Entradas do Usuário: Dados dos personagens e monstros, como nome, HP (pontos de vida), força, etc.
- Registros de Personagens: Manter uma base de dados dos personagens e monstros.
- Sistema de Iniciativa: Decide a ordem de ataque dos personagens e dos monstros, passa o turno para o próximo.
- Sistema de Ataque: Cálculos para acertos, danos e defesas.
- Registro de Combate: Manter um histórico das ações de cada turno.
- Conclusão do Combate: Determina o final da batalha quando um lado vence, calcular XP.

# Passos:
- Definição dos Personagens: Crie classes ou estruturas de dados para armazenar as informações dos personagens e monstros.
- Iniciativa: Uma função para decidir a ordem das ações. Pode ser aleatório ou baseado em um atributo como destreza.
- Ataques e Defesas: Funções que lidam com o cálculo dos acertos, danos causados e defesas.
- Exibição e Atualização: Mostrar o estado atual da batalha (HP dos personagens, quem está atacando, etc.) e atualizar após cada ação.
- Log de Combate: Registrar cada ação para que o jogador possa ver o que aconteceu.

# Tecnologias Usadas:
- Python para codificação.
- SQLite para persistência de dados.
- Tkinter para interface gráfica.