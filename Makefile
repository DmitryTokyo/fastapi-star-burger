migrate:
	alembic upgrade head

runserver:
	uvicorn backend.server:app --reload --port 8000

styles:
	flake8

front:
	./frontend/node_modules/.bin/parcel watch frontend/src/index.js --dist-dir frontend/bundles --public-url='./'

types:
	mypy backend/ --config-file setup.cfg

check:
	make styles types

ipython:
	ipython -i ipython_startup.py

test:
	pytest -v --cov=backend/foodcart --cov-fail-under=55 --cov-report term backend/foodcart