# Build Generate Evaluation Sheet To Students

## Demo

![](demo.gif)

## Input: List of Students

 _students.csv_ : add your students here

 ## Ouput: Planilha_Avaliacao.ods

 __planilha_avaliacao.ods__ : list of students and your requirements tests

## Dependences

### Tkinter

```bash
# Python 2.7
sudo apt-get install python-tk

# Python 3
sudo apt-get install python3-tk
```

### ezodf

```bash
pip install ezodf
```

## Terminal

```python
# number of questions to students == 2 (default)
python3.6 main.py 
# number of questions to students == 3
python3.6 main.py 3
```

## GUI mode

```python
python3.6 app.py 
```

## Make a Executable

### Install Pyinstaller

```python
-- pip2
pip install pyinstaller
-- pip3
pip3 install pyinstaller
```

### Build 

```python
pyinstaller -D -F -n main -c "app.py"
```

```bash
cd /dist
```

```bash
./main
```
