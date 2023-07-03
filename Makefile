VENV_DIR ?= $(abspath .venv-astro)

.PHONY: help
help:	
	@echo "clean - remove virtual environment"
	@echo "setup - create virtual environment"
	@echo "run - execute the main.py program"
	@echo "test - run all tests"

.PHONY: clean
clean:
	@echo "removing virtual environment..."
	@rm -rf __pycache__
	@rm -rf activate $(VENV_DIR)

.PHONY: setup
setup:
	@echo "creating virtual environment..."
	@python -m venv $(VENV_DIR) 
	@echo "updating PIP..."
	@$(VENV_DIR)/Scripts/python -m pip install --upgrade pip
	@echo "installing requirements..."
	@$(VENV_DIR)/Scripts/pip.exe install -r requirements-dev.txt
	@ln -sf $(VENV_DIR)/Scripts/activate ./activate
	@echo " "
	@echo "Run virtual environment with '. activate'..."

.PHONY: format
format:
	@echo "running black on all python code..."
	@. $(VENV_DIR)/Scripts/activate
	@black src/
	
.PHONY: run
run: $(VENV_DIR)
	@echo "running main astronomical algorithm program..."
	@. $(VENV_DIR)/Scripts/activate
	@$(VENV_DIR)/Scripts/python.exe main.py

.PHONY: test
test:
	pytest tests