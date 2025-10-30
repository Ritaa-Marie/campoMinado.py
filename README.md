# 🟢 Campo Minado

Trabalho desenvolvido por **Rita Mariê Amaral Siqueira**, aluna do curso de **Engenharia de Computação (CEFET - Campus V)**, para a disciplina de **Programação em Python**, orientada pelo professor **Guido Pantuza**.

---

## 1) Como iniciar e terminar a execução do programa

### Para iniciar o sistema:
1. Abra o arquivo em uma IDE (como **VSCode**) ou terminal;
2. Verifique se o **Python** está instalado (versão **3.13.3** ou superior) e se o terminal é compatível com ANSI colors (para as cores apareçam corretamente);
3. Execute o programa:
   - Na IDE: clique em **Run** ou no botão **"Play"**;
   - No terminal: navegue até o diretório do arquivo com o comando  
     ```bash
     cd caminho/do/arquivo python campo_minado.py
     ```
4. O sistema será exibido na tela principal com as instruções do jogo.

### Para sair do sistema:
1. Utilize a opção **"(8) - Sair"** no menu principal;
2. Ou feche a janela que contém o arquivo;
3. Ou pressione **Ctrl + C** no terminal.

---

## 2) Opções oferecidas pelo programa

### No início do programa:
- Escolher o **tamanho do campo**, digitando um valor entre **1 e 10**;
- Escolher o **número de minas escondidas**, com no mínimo **1** e no máximo o total de posições da matriz.

### Durante o jogo, o menu de movimentação oferece:
| Opção | Ação |
|:------:|:-----|
| (1) | Andar para cima |
| (2) | Andar para baixo |
| (3) | Andar para a direita |
| (4) | Andar para a esquerda |
| (5) | Marcar uma posição como mina (bandeira) |
| (6) | Abrir uma posição |
| (7) | Retirar uma bandeira |
| (8) | Sair do jogo |

### Resultados possíveis:
- **“Você ganhou o jogo! Parabéns.”** → se marcar todas as minas corretamente.  
- **“Você perdeu o jogo.”** → se abrir uma casa com mina.

---

##  3) Principais telas

O programa é executado no **terminal**, logo tem apenas a interface da linha de comando:

### Tela inicial:

> **Observação:** o jogador inicia na **posição verde**, e se move pelo campo com as opções do menu.

**Campo inicial:**
![Exibição do campo minado inicial](assets/screenshot.png)

**Campo final:**
![Exibição do campo minado final](assets/screenshot.png)

---

##  4) Conclusão

O jogo desenvolvido teve como finalidade **simular um campo minado simples**, mantendo suas principais regras e lógicas.

### Limitações:
1. Não há seleção de **níveis de dificuldade** (fácil, médio, difícil);
2. Não abre automaticamente as **casas vizinhas seguras**;
3. A movimentação é feita apenas pelo **teclado**, sem uso do mouse.

### Considerações finais:
Apesar das limitações, o jogo atende a todas as regras propostas no trabalho.  
Foi desenvolvido com o objetivo de ser **didático, acessível e funcional**, permitindo que qualquer pessoa possa jogar diretamente no terminal.

---

**Autora:** Rita Mariê Amaral Siqueira  
**Disciplina:** Programação em Python – CEFET-MG Campus V  
**Professor:** Guido Pantuza  

