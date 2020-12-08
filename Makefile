COLOR_OK=\\x1b[0;32m
COLOR_NONE=\x1b[0m
COLOR_ERROR=\x1b[31;01m
COLOR_WARNING=\x1b[33;01m
COLOR_OKTA=\x1B[34;01m

VERSION=$(shell grep -E -o '(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?' ./okta/__init__.py)

help:
	@echo "$(COLOR_OKTA)  ___  _  _______  _$(COLOR_NONE)"
	@echo "$(COLOR_OKTA) / _ \| |/ /_   _|/ \ $(COLOR_NONE)"
	@echo "$(COLOR_OKTA)| | | | ' /  | | / _ \ $(COLOR_NONE)"
	@echo "$(COLOR_OKTA)| |_| | . \  | |/ ___ \ $(COLOR_NONE)"
	@echo "$(COLOR_OKTA) \___/|_|\_\ |_/_/   \_\ $(COLOR_NONE)"
	@echo ""
	@echo "$(COLOR_OK)Okta SDK Python$(COLOR_NONE) version $(COLOR_WARNING)$(VERSION)$(COLOR_NONE)"
	@echo ""
	@echo "$(COLOR_WARNING)Usage:$(COLOR_NONE)"
	@echo "$(COLOR_OK)  make [command]$(COLOR_NONE)"
	@echo ""
	@echo "$(COLOR_WARNING)Available commands:$(COLOR_NONE)"
	@echo "$(COLOR_OK)  help$(COLOR_NONE)     Show this help message"

build\:dist:
	python3 setup.py sdist bdist_wheel

publish\:test:
	python3 -m twine upload --repository testpypi dist/*

publish\:prod:
	python3 -m twine upload dist/*