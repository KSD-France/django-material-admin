import codecs
import os

from setuptools import setup, find_packages


###################################################################

NAME = "django-material-admin"
PACKAGES = find_packages(exclude=("app", "app.*", "tests", "tests.*"))
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Framework :: Django :: 2.2",
    "Framework :: Django :: 3.0",
]
INSTALL_REQUIRES = []

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


if __name__ == "__main__":
    setup(
        name=NAME,
        description="Material Design For Django Administration",
        license="MIT License",
        url="https://github.com/KSD-France/django-material-admin",
        version="1.1.0-ksd",
        author="Anton Maistrenko",
        author_email="it2015maistrenko@gmail.com",
        maintainer="KSD",
        maintainer_email="contact@ksd.fr",
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        options={"bdist_wheel": {"universal": "1"}},
        include_package_data=True,
    )
