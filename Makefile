migrate:
	alembic upgrade head

runserver:
	uvicorn backend.server:app --reload --port 5000

style:
	flake8