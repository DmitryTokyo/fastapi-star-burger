migrate:
	alembic upgrade head

runserver:
	uvicorn backend.server:app --reload