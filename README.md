<h1 align="center">AgentKakuro</h1>




Diferentes tipos de algoritmos de puzzle que tem como objetivo resolver uma solução para o problema de busca. Este trabalho tem como objetivo de desenvolver uma solução de puzzles com o jogo Kakuro utilizando um agente para os algoritmos de satisfação de restrições (CSP – Constraint Satisfaction Problem). 

<br/>
<h2 align="center">Equipe</h2>
Brenda Paetzoldt Silva - brendapaetzoldt<br/>
Robson de Jesus - robsondejesus1996<br/>
<br/>

<h2 align="center">Sobre o jogo</h2>
O jogo tem algumas semelhanças com palavras cruzadas, mas ao invés de letrar o tabuleiro é preenchido com dígitos de 1 a 9. Os quadrados do tabuleiro precisam ser preenchidos com esses dígitos para somar números específicos que a linha superior ou lateral esquerda está solicitando. Basicamente a principal regra faz um travamento em utilizar o mesmo digito mais de uma vez para obter uma determinada soma, e cada quebra cabeça existe uma solução única. 


<h2 align="center">CSP</h2>
Em português, problemas de satisfação de restrições, são comumente usados para solucionar problemas que contenham restrições a serem satisfeitas para que sejam resolvidos. Uma solução é uma atribuição de valores às variáveis que satisfaz toda restrição
Exemplos mais comuns de uso de CSP são jogos como Kakuro, Damas, Xadrez, Futoshiki, Sudoku e muitos outros.


<h2 align="center">Algoritmos implementados</h2><br/>
 •  Minimum Remaining Values/Valores Mínimos Rrestantes (MRV)<br/>
    - Ideia: atribuir primeiro a variável mais restrita<br/>
    - Podar: as tarefas impossíveis com bastante antecedência<br/>
    - Heurística de grau: escolha primeiro grau mais alto<br/><br/>
     
 •  Backtracking<br/>
    - Escolhe valores para uma variável de cada vez<br/>
    - Verifica a consistência com as restrições.<br/>
    
<h2 align="center">Tabuleiros</h2>   

	Tabuleiro _5x5	
 
 ![easy](https://user-images.githubusercontent.com/18469694/175239744-46984e2f-7d82-4058-a1d4-8d4cb4e69056.png)

	Tabuleiro _12x10	
![hard](https://user-images.githubusercontent.com/18469694/175239772-09a3de68-d1b4-4cad-bb0c-ba756a7941b7.png)


<h2 align="center">Comparações e análises</h2>   


Com o objetivo de testar as algoritmos em diferentes tamanhos de tabuleiros, foram realizadas dez execuções de cada e o tempo em segundos que cada um levou até encontrar a solução pode ser verificada nas tabelas abaixo:
												
											
	Tabuleiro _5x5	
												
![image](https://user-images.githubusercontent.com/18469694/175237358-3a2cd432-63f3-4301-b336-f4308f4f9c43.png)
*Valores em segundos

				
![image](https://user-images.githubusercontent.com/18469694/175238252-2f4076be-8f64-446a-82b0-9ecd017a1e90.png)


												
	Tabuleiro _12x10	
												
![image](https://user-images.githubusercontent.com/18469694/175237547-290c0ede-233f-47e0-88c6-ad3d16e4b062.png)
*Valores em segundos
				
				
![image](https://user-images.githubusercontent.com/18469694/175240105-1339e618-43fe-44c6-8050-347e59f9dbe3.png)

<h2 align="center">Conclusão</h2>   
todo


<br/><br/>
<h2 align="center">Download</h2>   

git clone [https://github.com/nikosgalanis/KakuroSolver.git](https://github.com/brendapaetzoldt/AgentKakuro.git)

<br/><br/>

<h2 align="center">Executar</h2>   
Escreva:
</h2>

	kakuro.py
	

<br/><br/>
<h2 align="center">Referências bibliográficas</h2>   
<br/>
DA SILVA, Fabrıcio Machado; LENZ, Maikon Lucian; FREITAS, Pedro Henrique Chagas; SANTOS,
Sidney Cerqueira Bispo. Inteligˆencia Artificial. Grupo A, 2019. Dispon´ıvel em: https://app.
minhabiblioteca.com.br/#/books/9788595029392.
<br/>

WWW.SFU.CA. Notes on Chapter 6: Constraint Satisfaction Problems. Disponível em: http://www.sfu.ca/~tjd/310summer2019/chp6_csp.html. Acesso em: 16 jun. 2022.

<br/><br/>
