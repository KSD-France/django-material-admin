init:
	find . -type d \( -iname 'node_modules' -o -iname 'venv' \) -prune -exec rm -rf {} \;
	npm install
	virtualenv -p /usr/bin/python3.7 venv
	venv/bin/pip install -r requirements.txt

clean:
	find . -maxdepth 0 -type d \( -iname 'build' -o -iname 'dist' -o -iname 'django_material_admin.egg-info' \) -prune -exec rm -rf {} \;

update: clean
	npm install
	venv/bin/pip install -r requirements.txt

build: update
	node_modules/gulp/bin/gulp.js
	venv/bin/python -m pep517.build .

scp: build
	scp dist/* pip@pip.ksd.fr:repo/django-material-admin/

.PHONY : init clean update scp
