.PHONY: run simulator lint format

# Define PYTHONPATH como uma variável
PYTHONPATH=src

# Comando para monitorar
run: 
	@PYTHONPATH=$(PYTHONPATH) python3 $(PYTHONPATH)/monitor/main.py

# Comando para simular
simulator:
	@PYTHONPATH=$(PYTHONPATH) python3 $(PYTHONPATH)/simulator.py

# Comando para rodar o pylint
lint:
	@PYTHONPATH=$(PYTHONPATH) pylint $(PYTHONPATH)/

# Comando para formatar o código com black e autopep8
format:
	@black $(PYTHONPATH)/
	@autopep8 --in-place --aggressive --aggressive $(PYTHONPATH)/*.py