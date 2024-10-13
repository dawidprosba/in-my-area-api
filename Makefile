.PHONY: help install-requirements

# Define colors
COLOR_RESET=\033[0m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m

# Show available commands
help:
	@echo "$(COLOR_GREEN)Available commands:$(COLOR_RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(COLOR_YELLOW)%-20s$(COLOR_RESET) %s\n", $$1, $$2}'

prepare: ## - Prepare the environment
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run: ## - Run the application
	uvicorn app.main:app --reload