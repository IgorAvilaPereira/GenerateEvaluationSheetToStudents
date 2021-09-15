# Gerar Planilha de Avaliação

## Instalação das Dependências

### Tkinter

```bash
# Python 2.7
sudo apt-get install python-tk
```
```bash
# Python 3
sudo apt-get install python3-tk
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
