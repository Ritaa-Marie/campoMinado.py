# Campo Minado
Trabalho desenvolvido por Rita Mariê Amaral Siqueira, aluna do curso de Engenharia de Computação (CEFET - Campus V) para a disciplina de Programação em Python orientada pelo professor Guido Pantuza.

# 1) Como iniciar e terminar a execução do programa
Para iniciar o sistema:
  1 - Abra o arquivo em uma IDE (VSCode) ou terminal;
  2 - Verifique se a extensão do python e interpretador estão instalados (versão 13.3);
  3 - Aberte run para executar o arquivo, ou navegue até o diretório que contém o arquivo, usando o comando cd (se estiver usando Windows), e utilize esse comando "python campo_minado.py";
  4 - O sistema será exibido na tela principal com as instruções para o jogo.

  Para sair do sistema:
    1 - Utilize a opção do menu "8" para encerrar a execução;
    2 - Feche a janela que contém o arquivo;
    3 - Pressione Ctrl + C no terminal;

# 2) Opções oferecidas pelo programa
  No início do programa é possível:
    1- Escolher o tamanho do campo, digitando um único valor entre 1 e 10;
    2 -Escolher o número de minas escondidas, com no mínimo 1 e no máximo o total de posições da matriz;
  Logo em seguida, é exibido o menu de opções para de fato jogar:
    (1) - Cima >> para andar para cima;
    (2) - Baixo >> para andar para baixo;
    (3) - Direita >> para andar para direita;
    (4) - Esquerda >> para andar para esquerda;
    (5) - Marcar uma posição como mina (bandeira) >> para marcar uma posição como mina;
    (6) - Abrir uma posição >> para abrir uma posição;
    (7) - Retirar bandeira >> para retirar uma bandeira;
    (8) - Sair >> para sair do sistema;
  Após as opções escolhidas, se não utilizar a opção "8", o jogador verá duas respostas:
    1 - "Você ganhou o jogo! Parabéns.", caso ele marque todas as minas corretamente;
    2 - "Você perdeu o jogo.", caso abra uma posição com mina.

# 3) Principais telas
O programa é exibido via terminal, logo temos apenas a interface da linha de comando:
{
------ CAMPO MINADO ------

Instruções para o jogo:
 - Escolha um tamanho para o lado seu campo minado quadrado (máximo: 10)
 - Escolha o número de minas escondidas (mínimo: 1)
 - Você inicia o jogo na posição da cor verde.
 - O limite de bandeiras ('M') é o número de minas.
 - Você perde o jogo se abrir uma casa com mina (?).
 - Você vence o jogo se marcar todas as casas com minas corretamente.

 Digite o tamanho para o lado do campo minado: RESPOSTA DO USUÁRIO
 Digite o número de minas escondidas: RESPOSTA DO USUÁRIO

== Campo minado ==
|*| |*|
|*| |*|
Número de bandeiras disponíveis ('M'): 2

   Movimentação
 (1) - Cima
 (2) - Baixo
 (3) - Direita
 (4) - Esquerda
 (5) - Marcar uma posição como mina (bandeira)
 (6) - Abrir uma posição
 (7) - Retirar bandeira
 (8) - Sair
--------------------
Digite a sua opção: RESPOSTA DO USUÁRIO

== Campo minado ==
|?| |2|
|2| |?|
Você perdeu o jogo.
}

OBSERVAÇÃO: o jogador começa na posição marcada com a cor verde, e a partir dela passa a se movimentar no campo:
![Exibição do campo minado inicial](assets/screenshot.png)

Ao finalizar o jogo, ele é impresso com as respostas:
![Exibição do campo minado final](assets/screenshot.png)

# 4) Conclusão
O jogo desenvolvido teve como finalidade simular um campo minado simples, mas com algumas de suas características principais.
Limitações:
  1 - Não permite a escolha de níveis (fácil, médio, alto);
  2 - Não abre todas as casas vizinhas mostrando os números, caso uma casa segura seja aberta;
  3 - Fica mais complexo se movimentar no campo sem ser pelo uso do mouse;
Considerações finais:
  Apesar de possuir algumas limitações, o jogo contém todas as regras impostas na descrição do trabalho, e tem o objetivo de ser simples e acessível para que qualquer pessoa consiga jogar.

C:\Users\ritam\OneDrive\Documentos\Faculdade\2º semestre\pythonOp>
