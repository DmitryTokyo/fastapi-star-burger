migrate:
	alembic upgrade head

runserver:
	uvicorn backend.server:app --reload --port 8000

style:
	flake8

front:
	./frontend/node_modules/.bin/parcel watch frontend/src/index.js --dist-dir frontend/bundles --public-url="./"