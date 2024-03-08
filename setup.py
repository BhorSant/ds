import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"
REPO_NAME = "ds"
AUTHOR_USER_NAME = "Santosh Bhor"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "santoshbhor2001@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # Add more classifiers as needed
    ],
    include_package_data=True,
    install_requires=[
        "numpy>=1.20.0",
        "scikit-learn>=0.24.0",
        # Add more dependencies as needed
    ],
    entry_points={
        "console_scripts": [
            "my_script = my_package.module:function",
            # Add more entry points as needed
        ]
    }
)
