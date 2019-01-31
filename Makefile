.PHONY: help ci venv install test test-fast test-commit lint-style lint-types sort-imports

help: ## This help dialog
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "Target" "Help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
        IFS=$$':' ; \
        help_split=($$help_line) ; \
        help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
        help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
        printf '\033[36m'; \
        printf "%-30s %s" $$help_command ; \
        printf '\033[0m'; \
        printf "%s\n" $$help_info; \
    done

ci: install test lint-style lint-types ## Run the CI pipeline locally

venv: ## Create a Python virtual environment, if does not exist yet
	test -d venv || python3.7 -m venv venv

install: venv ## Install the application with its dependencies for local development
	venv/bin/python -m pip install -U pip && \
	venv/bin/python -m pip install -e src && \
	venv/bin/python -m pip install -r src/tests/requirements.txt

test: ## Run tests
	./ci/run-tests.sh --coverage

test-fast: ## Run tests without coverage
	./ci/run-tests.sh

test-commit: # Whenever a source file changes, run tests and commit if they succeed
	./ci/test-commit.sh

lint-style: ## Lint code style
	./ci/lint-style.sh

lint-types: ## Lint types
	./ci/lint-types.sh

sort-imports: ## Fix the order of Python imports
	cd src && ../venv/bin/python -m isort -rc .
