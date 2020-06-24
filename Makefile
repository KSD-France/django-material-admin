clean:
	rm -r build dist django_material_admin.egg-info

prepare:
	npm install
	virtualenv -p /usr/bin/python3.7 venv
	venv/bin/pip install -r requirements.txt

build:
	node_modules/gulp/bin/gulp.js
	venv/bin/python -m pep517.build .

scp:
	scp dist/* pip@pip.ksd.fr:repo/django-material-admin/
