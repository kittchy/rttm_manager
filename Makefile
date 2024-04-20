build:
	rye build --wheel --out target

test:
	pytest -s --cov -v tests/*
