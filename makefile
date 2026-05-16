PYTHON := .venv/bin/python

setup:
	@if [ ! -d ".venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv .venv; \
	fi

install: setup
	$(PYTHON) -m pip install -r requirements.txt

run: setup
	$(PYTHON) -m python.render.simulation

freeze: setup
	$(PYTHON) -m pip freeze > requirements.txt

clean:
	find . -name "__pycache__" -exec rm -r {} +
	find . -name "*.pyc" -delete
