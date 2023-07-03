import setuptools

long_description = open("README.md", "r").read()

setuptools.setup(
    name="astronomical algorithms",
    version="0.0.1",
    description="algorithms to be used for astronomical calculations",
    author="Sean Tedesco",
    author_email="stedesco@live.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "test = astroalgo.test:main",
        ],
    },
)
