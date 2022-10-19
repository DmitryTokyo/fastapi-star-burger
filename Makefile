migrate:
	alembic upgrade head

runserver:
	uvicorn backend.server:app --reload

style:
	flake8