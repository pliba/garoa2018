# Notas

## 2018-12-13

O teste `test_repl_multiple_expressions` está falhando: a segunda expressão não é processada.

Porém, o REPL consegue tratar múltiplas expressões quando usado interativamente, ou quando redireciono o arquivo `2expressions.txt` como neste exemplo:

```
$ ./repl.py < 2expressions.txt 
To exit, type .q
> 6
> 20
```

**Obs:** Este teste foi criado para verificar se o prompt primário volta a ser usado depois que uma expressão completa é avaliada.