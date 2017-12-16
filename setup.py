from setuptools import setup, find_packages

version = __import__("django_better_migrations").__version__


def read(path):
    """Return the content of a file."""
    with open(path, "r") as f:
        return f.read()


setup(
    name="django-better-migrations",
    version=version,
    description="Improves Django migration system.",
    long_description=(read("README.md")),
    url="http://github.com/botify-labs/django-better-migrations",
    license="MIT",
    author="Jean-Baptiste Barth",
    author_email="jeanbaptiste.barth@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    scripts=[],
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Database",
    ],
)
