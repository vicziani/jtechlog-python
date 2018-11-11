install: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	venv/bin/pip install -Ur requirements.txt
	venv/bin/pip install -e .
	touch venv/bin/activate

test: install
	venv/bin/pytest --cov=jtechlog --cov-report xml

pylint: install
	venv/bin/pylint --rcfile=.pylintrc jtechlog -r n > pylint-report.txt

sonar: install
	/opt/sonar-scanner-3.2.0.1227/bin/sonar-scanner