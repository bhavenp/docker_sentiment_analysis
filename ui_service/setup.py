from pathlib import Path
from setuptools import setup, find_packages

ROOT_DIR = Path(__file__).resolve().parent

with open(ROOT_DIR / "README.md", "r") as f:
    long_description = f.read().strip()

setup(
    name="sentiment_analysis_ui_service",
    version=0.1,
    description="Display the UI using a Flask application. UI will interact with the ML model.",
    long_description=long_description,
    author="Bhaven Patel",
    python_requires= ">=3.6.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
)