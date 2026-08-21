.PHONY: test sync clean

test:
	python -m unittest discover tests

sync:
	python upload.py

clean:
	rm -rf __pycache__
