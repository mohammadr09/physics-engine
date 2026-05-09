venv:
	python -m venv .venv
	$(if $(OS),$(if $(findstring Windows,$(OS)),cmd /c .venv\Scripts\activate.bat,. .venv/bin/activate),. .venv/bin/activate)
	
install:
	pip install -r requirements.txt