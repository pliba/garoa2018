# garoa2018

Exemplos para a Oficina de Linguagens de Programação iniciada no Garoa Hacker Clube em nov/2018

Destaques no wiki deste repositório:

* [Preparação](https://github.com/pliba/garoa2018/wiki/Prepara%C3%A7%C3%A3o) do ambiente de desenvolvimento com Python 3

* [SubPascal](https://github.com/pliba/garoa2018/wiki/Linguagem-SubPascal): a linguagem do capítulo 1 de PLIBA (Programming Languages: an Interpreter-Based Approach)


## Uso de Dialogue

O projeto [Dialogue](https://github.com/pliba/dialogue.git) é uma dependência para rodar os testes dos REPL, mas ele não pode ser instalado via `pip`, tem que ser *vendored* (incluído). Siga estes passos:

```
$ git remote add -f dialogue https://github.com/pliba/dialogue.git

$ git subtree add --prefix onde_quero_colocar/dialogue dialogue master --squash
```
