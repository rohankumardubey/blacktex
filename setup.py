import os

from setuptools import find_packages, setup

base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "blacktex", "__about__.py"), "rb") as f:
    exec(f.read(), about)


setup(
    name="blacktex",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/blacktex",
    project_urls={
        "Code": "https://github.com/nschloe/blacktex",
        "Issue tracker": "https://github.com/nschloe/blacktex/issues",
    },
    author=about["__author__"],
    author_email=about["__author_email__"],
    install_requires=[],
    python_requires=">=3.6",
    description="Cleans up your LaTeX files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["blacktex = blacktex.cli:main"]},
)
