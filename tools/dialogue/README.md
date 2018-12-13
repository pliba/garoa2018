# REPLs e a classe Dialogue

Os programas deste diretório mostram como construir e testar um REPL (Read-Eval-Print-Loop, o laço central de um interpretador interativo).

O que há de mais complicado aqui é a classe `Dialogue`. Ela serve para simular interações com usuários, oferecendo um método `fake_input` que serve como _mock_ da função embutida `input` do Python 3.

O arquivo `dialogue_test.py` inclui dois REPLs simples para testar e demonstrar a classe `Dialogue`.

Um exemplo mais interessante de REPL está no módulo `adder.py`. É uma "máquina de somar" que só faz isso mesmo: somar números — o uso mais comum das tradicionais somadoras de mesa com fita de papel. O `adder_test.py` é mais um exemplo de uso do `Dialogue`.

> Meu pai, Jairo Ramalho, gostava de dizer que uma somadora de mesa com fita de papel é melhor que qualquer calculadora mais moderna e portátil que só mostra um número de cada vez na tela, porque a somadora permite conferir os números digitados facilmente. Meu pai iria gostar do `adder.py`.