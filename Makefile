build:
	rm target/* && rye build --wheel --out target

clean:
	rye build --clean

publish:
	rm target/* && rye build --wheel --out target
	rye publish --token ${PYPI_TOKEN} --yes target/*

test:
	rye run pytest -s -v --cov

actions:
	act pull_request --container-architecture linux/amd64 --remote-name upstream
