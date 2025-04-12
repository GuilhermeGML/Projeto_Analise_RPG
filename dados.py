import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sistemas_expandido = [
    ["Dungeons & Dragons 1ª Edição", 1974, "TSR", "Fantasia", "D20", "Tática", "Alta", "Baixa", "Classes rígidas", "Grid e iniciativa", "Níveis"],
    ["Dungeons & Dragons 2ª Edição", 1989, "TSR", "Fantasia", "D20", "Tática", "Alta", "Baixa", "Classes rígidas", "Grid e iniciativa", "Níveis"],
    ["Dungeons & Dragons 3ª Edição", 2000, "Wizards of the Coast", "Fantasia", "D20", "Híbrida", "Alta", "Média", "Multiclasse flexível", "Grid e ataques por rodada", "Níveis e talentos"],
    ["Dungeons & Dragons 3.5", 2003, "Wizards of the Coast", "Fantasia", "D20", "Híbrida", "Alta", "Média", "Multiclasse flexível", "Grid e ataques por rodada", "Níveis e talentos"],
    ["Dungeons & Dragons 4ª Edição", 2008, "Wizards of the Coast", "Fantasia", "D20", "Tática", "Alta", "Baixa", "Poderes por função", "Estilo MMORPG", "Poderes por nível"],
    ["Dungeons & Dragons 5ª Edição", 2014, "Wizards of the Coast", "Fantasia", "D20", "Híbrida", "Média", "Média", "Classes com subclasses", "Simplificado com grid opcional", "Níveis com arquétipos"],
    ["Pathfinder 1ª Edição", 2009, "Paizo", "Fantasia", "D20", "Tática", "Alta", "Média", "Multiclasse com talentos", "Similar ao D&D 3.5", "Níveis e talentos"],
    ["Pathfinder 2ª Edição", 2019, "Paizo", "Fantasia", "D20", "Tática", "Alta", "Média", "Sistema de feats modular", "Ações por turno", "Níveis e feats"],
    ["Tormenta20", 2020, "Jambô", "Fantasia", "D20", "Híbrida", "Média", "Média", "Classes com caminhos", "Estilo D&D 5e", "Níveis"],
    ["Tormenta RPG (3D&T base)", 2005, "Jambô", "Fantasia", "D6", "Híbrida", "Média", "Média", "Tipos com perícias", "Simplificado", "Níveis"],
    ["Call of Cthulhu", 1981, "Chaosium", "Horror", "D100", "Narrativa", "Alta", "Alta", "Perícias percentuais", "Sanidade e investigação", "Uso de perícias"],
    ["GURPS", 1986, "Steve Jackson Games", "Genérico", "3d6", "Híbrida", "Alta", "Média", "Pontos em perícias e vantagens", "Determinístico", "Por experiência"],
    ["Savage Worlds", 2003, "Pinnacle", "Genérico", "Poliédricos", "Híbrida", "Média", "Média", "Atributos e vantagens", "Cartas e dados", "Avanço por pontos"],
    ["Shadowrun", 1989, "Catalyst Game Labs", "Cyberpunk/Fantasia", "D6", "Híbrida", "Alta", "Média", "Perícias e arquétipos", "Ações complexas", "Por karma"],
    ["Warhammer Fantasy Roleplay", 1986, "Games Workshop", "Fantasia", "D100", "Tática", "Alta", "Média", "Carreiras", "Crítico e sangrento", "Carreiras e XP"],
    ["Warhammer 40k: Dark Heresy", 2008, "Fantasy Flight", "Sci-fi sombrio", "D100", "Tática", "Alta", "Baixa", "Carreiras e habilidades", "Letal", "Experiência"],
    ["World of Darkness (Storyteller)", 1991, "White Wolf", "Moderno sombrio", "D10", "Narrativa", "Média", "Alta", "Atributos + habilidades", "Dados narrativos", "Avanços por XP"],
    ["Vampire: A Máscara", 1991, "White Wolf", "Terror pessoal", "D10", "Narrativa", "Média", "Alta", "Clãs e disciplinas", "Narrativo", "XP"],
    ["Werewolf: O Apocalipse", 1992, "White Wolf", "Terror espiritual", "D10", "Narrativa", "Média", "Alta", "Tribos e formas", "Narrativo e físico", "XP"],
    ["Mutants & Masterminds", 2002, "Green Ronin", "Super-heróis", "D20", "Tática", "Alta", "Média", "Pontos e poderes", "Combate heroico", "Por PL"],
    ["Fate Core", 2003, "Evil Hat", "Genérico", "Fate Dice", "Narrativa", "Baixa", "Muito alta", "Aspectos e perícias", "Livre e abstrato", "Avanço por marcos"],
    ["Fate Accelerated", 2013, "Evil Hat", "Genérico", "Fate Dice", "Narrativa", "Baixa", "Muito alta", "Abordagens", "Narrativo", "Marcos"],
    ["Dungeon World", 2012, "Sage Kobold", "Fantasia", "2d6", "Narrativa", "Baixa", "Alta", "Playbooks", "Moves narrativos", "Avanços por experiência"],
    ["Monsterhearts", 2012, "Buried Without Ceremony", "Drama adolescente", "2d6", "Narrativa", "Baixa", "Muito alta", "Playbooks", "Conflitos sociais", "Avanços pessoais"],
    ["Apocalypse World", 2010, "Lumpley Games", "Pós-apocalíptico", "2d6", "Narrativa", "Média", "Alta", "Playbooks", "Moves e consequências", "Avanços por experiência"],
    ["Blades in the Dark", 2017, "Evil Hat", "Fantasia urbana", "D6", "Narrativa", "Média", "Alta", "Ladrões e gangues", "Ações e stress", "Desenvolvimento de crew"],
    ["Ironsworn", 2018, "Shawn Tomkin", "Fantasia sombria", "D6", "Narrativa", "Média", "Alta", "Votos e perícias", "Moves e oráculos", "Jornada pessoal"],
    ["Masks: A New Generation", 2016, "Magpie Games", "Super-heróis", "2d6", "Narrativa", "Baixa", "Alta", "Playbooks adolescentes", "Conflito emocional", "Crescimento pessoal"],
    ["Thirsty Sword Lesbians", 2021, "Evil Hat", "Drama LGBTQ+", "2d6", "Narrativa", "Baixa", "Alta", "Arquetipos", "Emoções e relações", "Conquistas e vínculos"],
    ["The Veil", 2016, "Samjoko Publishing", "Cyberpunk", "2d6", "Narrativa", "Média", "Alta", "Emoções e mods", "Psicológico", "Desenvolvimento emocional"],
    ["Lasers & Feelings", 2013, "John Harper", "Sci-fi leve", "D6", "Narrativa", "Baixa", "Média", "Um número define tudo", "Simplificado", "Narrativo"],
    ["Ordem Paranormal", 2020, "Jambô", "Terror moderno", "D20", "Híbrida", "Média", "Alta", "Classes e trilhas", "Simplificado", "Níveis"],
    ["Lenda de Ghanor", 2017, "Cellbit", "Fantasia", "D20", "Híbrida", "Média", "Alta", "Inspirado em D&D 5e", "Narrativo", "Níveis"],
    ["3D&T Alpha", 2008, "Jambô", "Genérico", "D6", "Tática", "Baixa", "Média", "Pontos em atributos", "Simplificado", "Níveis"],
    ["Mighty Blade", 2010, "Independente", "Fantasia", "D6", "Tática", "Média", "Média", "Classes simples", "Iniciativa e ações", "Níveis"],
    ["Defensores de Tóquio 2ª edição (DT2)", 1996, "Trama", "Paródia", "D6", "Tática", "Média", "Média", "Atributos caricatos", "Engraçado", "XP"],
    ["A Bandeira do Elefante e da Arara", 2015, "Devir", "Fantasia histórica", "D20", "Narrativa", "Média", "Alta", "Origens e caminhos", "Ações e perícias", "Experiência"],
    ["UED: Você é a Resistência", 2015, "Universo Simulado", "Pós-apocalíptico", "D6", "Narrativa", "Média", "Alta", "Sobreviventes", "Tático e narrativo", "Narrativo"],
    ["Terra Devastada", 2008, "J.M. Trevisan", "Zumbis", "D6", "Narrativa", "Média", "Alta", "Livre", "Letalidade alta", "Survival"],
    ["Violentina", 2011, "Rodrigo Aragão", "Crime estilizado", "D6", "Narrativa", "Baixa", "Alta", "Estilo e exagero", "Improvisado", "Narrativo"],
    ["+2d6", 2014, "Independente", "Genérico", "2d6", "Narrativa", "Baixa", "Média", "Livre e simples", "Abstrato", "XP"],
    ["Honey Heist", 2017, "Grant Howitt", "Comédia", "D6", "Narrativa", "Baixa", "Alta", "Urso e criminoso", "Um atributo só", "Narrativo"],
    ["Cthulhu Dark", 2010, "Independente", "Horror", "D6", "Narrativa", "Baixa", "Alta", "Livre", "Sanidade e horror", "Narrativo"],
    ["Mörk Borg", 2020, "Stockholm Kartell", "Fantasia sombria", "D20", "Tática", "Média", "Baixa", "Aleatório e trágico", "Letal e punitivo", "Sobrevivência"],
    ["Troika!", 2019, "Melsonian Arts Council", "Fantasia surreal", "D6", "Narrativa", "Média", "Alta", "Backgrounds aleatórios", "Sistema de iniciativa caótica", "XP e caos"],
    ["Cairn", 2021, "Yochai Gal", "Fantasia OSR", "D20", "Tática", "Baixa", "Média", "Baseado em inventário", "Letal", "Exploração"],
    ["Into the Odd", 2014, "Chris McDowall", "Fantasia industrial", "D20", "Tática", "Baixa", "Média", "Atributos e relíquias", "Simplificado e letal", "Por exploração"],
    ["Knave", 2018, "Ben Milton", "Fantasia OSR", "D20", "Tática", "Baixa", "Média", "Sem classes", "Letal e direto", "Por saque e descoberta"],
    ["Electric Bastionland", 2020, "Chris McDowall", "Weirdpunk", "D20", "Tática", "Baixa", "Alta", "Falidos com dívida", "Letal e humorado", "Sobrevivência"],
    ["Index Card RPG", 2017, "Runehammer", "Fantasia/Genérico", "D20", "Tática", "Média", "Média", "Rápido e modular", "Minimalista", "Pontos de maestria"]
]

colunas = [
    "Sistema",
    "Ano de lançamento",
    "Editora",
    "Gênero principal",
    "Tipo de dado usado",
    "Tipo de mecânica (narrativa, tática, híbrida)",
    "Nível de complexidade (baixa/média/alta)",
    "Foco narrativo (baixa/média/alta)",
    "Estilo de criação de personagem",
    "Sistema de combate",
    "Sistema de progressão"
]

df_rpg = pd.DataFrame(sistemas_expandido, columns=colunas)

mecanica_tot = df_rpg['Tipo de mecânica (narrativa, tática, híbrida)'].value_counts()
print(mecanica_tot)

complexidade_porct = df_rpg['Nível de complexidade (baixa/média/alta)'].value_counts(normalize=True) * 100
print(complexidade_porct)

df_rpg['Década'] = (df_rpg['Ano de lançamento'] // 10) * 10
sistema_dec = df_rpg['Década'].value_counts().sort_index()
print(sistema_dec)

mec_fnarrat = pd.crosstab(df_rpg['Tipo de mecânica (narrativa, tática, híbrida)'], df_rpg['Foco narrativo (baixa/média/alta)'])
print(mec_fnarrat)

complex_fnarrat = pd.crosstab(df_rpg['Nível de complexidade (baixa/média/alta)'], df_rpg['Foco narrativo (baixa/média/alta)'])
print(complex_fnarrat)

genero_tot = df_rpg['Gênero principal'].value_counts()
print(genero_tot)

dados_tot = df_rpg['Tipo de dado usado'].value_counts()
print(dados_tot)

ano_complex = df_rpg.groupby('Nível de complexidade (baixa/média/alta)')['Ano de lançamento'].describe()
print(ano_complex)

estilo_perso = df_rpg['Estilo de criação de personagem'].value_counts().head(10)
print(estilo_perso)

top_editoras = df_rpg['Editora'].value_counts().head(8).index
df_top = df_rpg[df_rpg['Editora'].isin(top_editoras)]
mec_edit =pd.crosstab(df_top['Editora'], df_top['Tipo de mecânica (narrativa, tática, híbrida)'])
print(mec_edit)

plt.figure(figsize=(8, 5))
df_rpg['Tipo de mecânica (narrativa, tática, híbrida)'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição dos Tipos de Mecânica')
plt.xlabel('Tipo de Mecânica')
plt.ylabel('Quantidade de Sistemas')
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 6))
df_rpg['Nível de complexidade (baixa/média/alta)'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'gold', 'lightgreen'])
plt.title('Distribuição de Complexidade')
plt.ylabel('')
plt.tight_layout()
plt.show()


df_rpg['Década'] = (df_rpg['Ano de lançamento'] // 10) * 10
plt.figure(figsize=(10, 5))
df_rpg['Década'].value_counts().sort_index().plot(kind='bar', color='plum')
plt.title('Número de Sistemas por Década')
plt.xlabel('Década')
plt.ylabel('Quantidade de Sistemas')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(data=df_rpg, x='Tipo de mecânica (narrativa, tática, híbrida)', hue='Foco narrativo (baixa/média/alta)', palette='Set2')
plt.title('Mecânica vs Foco Narrativo')
plt.xlabel('Tipo de Mecânica')
plt.ylabel('Número de Sistemas')
plt.legend(title='Foco Narrativo')
plt.tight_layout()
plt.show()


cross_tab = pd.crosstab(df_rpg['Nível de complexidade (baixa/média/alta)'],
                        df_rpg['Foco narrativo (baixa/média/alta)'])
plt.figure(figsize=(8, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Complexidade vs Foco Narrativo')
plt.xlabel('Foco Narrativo')
plt.ylabel('Complexidade')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
df_rpg['Gênero principal'].value_counts().sort_values().plot(kind='barh', color='orchid')
plt.title('Distribuição dos Gêneros de RPG')
plt.xlabel('Quantidade de Sistemas')
plt.ylabel('Gênero Principal')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(data=df_rpg, x='Tipo de dado usado', order=df_rpg['Tipo de dado usado'].value_counts().index, palette='pastel')
plt.title('Tipos de Dados Usados nos Sistemas')
plt.xlabel('Tipo de Dado')
plt.ylabel('Número de Sistemas')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=df_rpg, x='Nível de complexidade (baixa/média/alta)', y='Ano de lançamento', palette='coolwarm')
plt.title('Distribuição de Anos por Complexidade')
plt.xlabel('Complexidade')
plt.ylabel('Ano de Lançamento')
plt.tight_layout()
plt.show()


top_estilos = df_rpg['Estilo de criação de personagem'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_estilos.plot(kind='bar', color='mediumseagreen')
plt.title('Top 10 Estilos de Criação de Personagem')
plt.xlabel('Estilo de Criação')
plt.ylabel('Quantidade de Sistemas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


top_editoras = df_rpg['Editora'].value_counts().head(8).index
df_top = df_rpg[df_rpg['Editora'].isin(top_editoras)]
crosstab_editora_mecanica = pd.crosstab(df_top['Editora'], df_top['Tipo de mecânica (narrativa, tática, híbrida)'])
crosstab_editora_mecanica.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20c')
plt.title('Tipo de Mecânica por Editora (Top 8)')
plt.xlabel('Editora')
plt.ylabel('Número de Sistemas')
plt.legend(title='Tipo de Mecânica')
plt.tight_layout()
plt.show()

