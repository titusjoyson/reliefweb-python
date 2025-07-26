build:
	python -m build

check:
	python -m twine check dist/*

publish:
	python -m twine upload dist/*

.PHONY: build check publish
