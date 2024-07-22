.PHONY: run monitor lint format

# Comando para rodar o servidor FastAPI
run:
	PYTHONPATH=src python3 src/main.py

# Comando para monitorar
monitor: 
	PYTHONPATH=src python3 src/monitor/main.py

# Comando para rodar o pylint
lint:
	PYTHONPATH=src pylint src/

# Comando para formatar o código com black e autopep8
format:
	black src/
	autopep8 --in-place --aggressive --aggressive src/*.py