# Gerar Planilha de Avaliação

## Instalação das Dependências

### Tkinter

```bash
# Python 2.7
sudo apt-get install python-tk

# Python 3
sudo apt-get install python3-tk
```

## Executar modo terminal

```python
# qtde de requisitos == 2
python3.6 main.py 
# qtde de requisitos == 3
python3.6 main.py 3
```

## Executar modo gráfico

```python
python3.6 app.py 
```

## Criar executável

```python
pyinstaller -D -F -n main -c "app.py"
```

```bash
cd /dist
```

```bash
./main
```
