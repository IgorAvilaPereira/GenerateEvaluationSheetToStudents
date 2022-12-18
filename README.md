# Build Generate Evaluation Sheet To Students

## Dependences

### Tkinter

```bash
# Python 2.7
sudo apt-get install python-tk

# Python 3
sudo apt-get install python3-tk
```

## List of Students

 _students.csv_ 

## Terminal

```python
# qtde de requisitos == 2
python3.6 main.py 
# qtde de requisitos == 3
python3.6 main.py 3
```

## GUI mode

```python
python3.6 app.py 
```

## Make a Executable

```python
pyinstaller -D -F -n main -c "app.py"
```

```bash
cd /dist
```

```bash
./main
```
