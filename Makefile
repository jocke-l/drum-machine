.PHONY: test
test:
	@coverage run -m unittest --verbose

.PHONY: coverage-report
coverage-report:
	@coverage report -m --fail-under=100
