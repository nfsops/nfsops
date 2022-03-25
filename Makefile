PACKAGE_NAME := nfsops
PACKAGE_PATH := ${PACKAGE_NAME}
DOCS_PATH := docs
SOURCE_PATHS := setup.py ${PACKAGE_PATH} ${DOCS_PATH} tests

create-environment:
	conda env create -f environment.yaml

install:
	pip install .

install-development:
	pip install -e .[development]

sort-import:
	isort ${SOURCE_PATHS}

format:
	autopep8 --recursive --in-place ${SOURCE_PATHS}

check-typing:
	mypy ${SOURCE_PATHS}

lint:
	pylint ${SOURCE_PATHS}

fix: sort-import format check-typing lint

test:
	pytest

report-coverage:
	pytest --cov ${PACKAGE_PATH}

build-docs:
	sphinx-build -b html ${DOCS_PATH}/nfsops ${DOCS_PATH}/build

clean-source:
	git clean -Xdf

clean-install:
	pip uninstall -y ${PACKAGE_NAME}

clean-environment:
	conda remove -y -n ${PACKAGE_NAME} --all

clean: clean-source clean-install clean-environment
