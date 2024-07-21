.PHONY: run lint format test

# Comando para rodar o servidor FastAPI
get_messages:
	PYTHONPATH=src python3 src/main.py

monitor: 
  PYTHONPATH=src python3 src/monitor/main.py

# Comando para rodar o pylint
lint:
	PYTHONPATH=src  pylint src/

# Comando para formatar o código com black e autopep8
format:
	black src/
	autopep8 --in-place --aggressive --aggressive src/*.py

# Comando para rodar os testes com pytest
test:
	pytest tests/