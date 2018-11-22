# garoa2018

Exemplos para a Oficina de Linguagens de Programação iniciada no Garoa Hacker Clube em nov/2018

## Preparação do ambiente de trabalho

### GNU/Linux Ubuntu 18.04

Instruções para verificar e preparar o ambiente para trabalhar com TDD usando Pytest em um Python moderno.

#### 1. Identificar o interpretador de Python 3

Qual interpretador Python 3 é o padrão no meu sistema?

O comando do `which` responde (*"which"* é "qual", em inglês):

```
$ which python3 
/home/luciano/anaconda3/bin/python3
```

Qual a versão exata deste interpretador padrão?

```
$ python3 --version
Python 3.7.0
```

> **Importante:** Se não tem uma versão recente de Python (3.6 ou 3.7), baixe e instale a versão mais recente de Python (versão 3.7.1 em novembro de 2018).


#### 2. Criar ambiente virtual

Com um Python recente, podemos criar o ambiente virtual usando o módulo `venv` da biblioteca padrão. No meu caso, vou chamar o ambiente virtual de `.venv37` para lembrar que foi criado com `venv` a partir de um Python 3.7:

```
$ python3 -m venv .venv37
```

#### 3. Ativar o ambiente virtual

Uma vez criado o ambiente virtual, é necessário ativá-lo usando o comando `.` (ou `source`, mesma coisa) para executar os comandos do arquivo `bin/activate` que foi criado no ambiente. Note que isso muda o prompt do shell, colocando o nome do ambiente entre parêntesis. Nesse exemplo, `(.venv37)`:

```
$ . .venv37/bin/activate
(.venv37) $
```

Quando o ambiente é ativado, o interpretador Python padrão passa a ser aquele instalado no ambiente. O mesmo ocorre com o comando `pip`. O comando `which` comprova isso:

```
(.venv37) $ which python3
/home/luciano/prj/pliba/garoa2018/.venv37/bin/python3
(.venv37) $ which pip
/home/luciano/prj/pliba/garoa2018/.venv37/bin/pip
```

A partir de agora, toda vez que você usar `pip`, vai instalar pacotes apenas no ambiente virtual, e não no Python do sistema. E quando chamar `python3` (ou mesmo `python`), o interpretador do ambiente virtual será executado.


#### 4. Atualizar o pip

O comando `pip` que vem na biblioteca padrão do Python normalmente não é a versão mais atual. Vale a pena atualizá-lo assim:

```
$ . .venv37/bin/activate
(.venv37) $ pip install --upgrade pip
Collecting pip
... blá, blá, blá ...
Successfully installed pip-18.1
```


#### 5. Instalar pytest

Agora podemos instalar bibliotecas. A primeira que precisamos é `pytest`:

```
(.venv37) $ pip install pytest
Collecting pytest
... blá, blá, blá ...
Successfully installed atomicwrites-1.2.1 attrs-18.2.0 more-itertools-4.3.0 pluggy-0.8.0 py-1.7.0 pytest-4.0.0 six-1.11.0
``` 

Pronto, agora já dá para fazer TDD usando `pytest`, a melhor ferramenta de testes do mundo Python.

Se quiser ver uma lista do que foi instalado, para satisfazer os requisitos de `pytest`, use `pip freeze`:

```
(.venv37) $ pip freeze
atomicwrites==1.2.1
attrs==18.2.0
more-itertools==4.3.0
pluggy==0.8.0
py==1.7.0
pytest==4.0.0
six==1.11.0
```

#### 6. (opcional) Desativar o ambiente virtual

Ao final de uma sessão de trabalho, você pode desativar o ambiente virtual usando o comando `deactivate`. Ao executar esse comando, a parte do prompt identificando o ambiente entre parêntesis desaparece:

```
(.venv37) $ deactivate
$
```

Em vez de desativar o ambiente, você pode simplesmente fechar o shell, porque o ambiente não fica ativo entre sessões. Para reativar o ambiente no futuro, use o comando `.` (ou `source`), conforme o **passo 3.**
