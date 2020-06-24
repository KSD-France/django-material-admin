clean:
	rm -r package/build package/dist package/django_material_admin.egg-info

prepare:
	npm install
	virtualenv -p /usr/bin/python3.7 venv
	venv/bin/pip install -r requirements.txt

build:
	node_modules/gulp/bin/gulp.js
	venv/bin/python package/setup.py sdist bdist_wheel

scp:
	scp package/dist/* pip@pip.ksd.fr:repo/django-material-admin/
