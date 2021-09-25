.PHONY: test
test: install
	pytest $(ARGS)

.PHONY: install
install: build
	pip install dist/app-0.1.0-cp39-cp39-manylinux_2_31_x86_64.whl

.PHONY: build
build: clean
	poetry build --format wheel

.PHONY: clean
clean:
	rm -rf dist build cython_build
	find . -name "*.so" -type f -delete
	pip uninstall app -y
