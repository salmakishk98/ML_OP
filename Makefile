install:
	pip install -r requirements.txt

lint:
	pylint main.py

test:
	python -m pytest -vv test.py

deploy:
	uvicorn main_app:app