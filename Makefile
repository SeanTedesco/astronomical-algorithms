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
	@python3 -m venv $(VENV_DIR) 
	@echo "updating PIP..."
	@$(VENV_DIR)/bin/python -m pip install --upgrade pip
	@echo "installing requirements..."
	@$(VENV_DIR)/bin/pip install -r requirements-dev.txt
	@ln -sf $(VENV_DIR)/bin/activate ./activate
	@echo " "
	@echo "Run virtual environment with '. activate'..."

.PHONY: format
format:
	@echo "running black on all python code..."
	@. $(VENV_DIR)/bin/activate
	@black src/
	
.PHONY: run
run: $(VENV_DIR)
	@echo "running main astronomical algorithm program..."
	@. $(VENV_DIR)/bin/activate
	@$(VENV_DIR)/bin/python main.py

.PHONY: test
test:
	pytest tests