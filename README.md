# Black screen - MOHAA Spearhead and breakthrough

Script python de solução improvisada para o erro de tela preta ocasionado pela execução das expansões do jogo medal of honor alied assualt. Esse método usualmente funciona desde que o jogo base seja executado normalmente, contundo, experience o erro mencionado ao executar uma de suas expansões.

# Descrição da solução:
O script em questão reproduz o passo a passo de forma automatizada da solução apresentada pelo canal [theshadow27](https://www.youtube.com/watch?v=UEFbprRUsBI) e consiste num truque simples de renomeação dos atalhos de expansões para o nome do atalho relativo ao jogo base presentes na pasta de instalação do jogo. A alteração entre jogo base e expansões se dá mediante restauração dos atalhos originais.

O script, por sua vez, através das bibliotecas OS e SHUTIL altera apenas os atalhos presentes na pasta do jogo e adiciona um novo diretório de backup a mesma contendo os respectivos atalhos originais. Nenhum outro arquivo ou diretórios externos é impactado por sua execução.


> [!IMPORTANT]
> script desenvolvido baseado-se na versão do [medal of honor - Alied Assault War chest](https://www.gog.com/en/game/medal_of_honor_allied_assault_war_chest) disponível na GOG


# Como executar o script:

1° passo: execute o script black_screen_fix.py usando sua IDE habitual ou o interpretador python nativo

2° passo: selecione uma das opções exibidas pelo menu:

![menu de seleção](/Menu_image.png)

3° execute o arquivo 'mohaa.exe' ou 'MOHAA.exe' presente na pasta do jogo. O jogo executado será correspondente a opção selecionada no menu anterior

