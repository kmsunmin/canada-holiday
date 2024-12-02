test:
	pytest -ra

test-cov:
	coverage run -m pytest -ra

cov-report:
	coverage report
