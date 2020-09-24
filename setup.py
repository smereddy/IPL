"""
Package setup
"""

import setuptools  # type: ignore

setuptools.setup(
    name="IPL",
    version=2020,
    author="Surya Mereddy",
    author_email="suryamereddy@gmail.com",
    description="Recommend Fantasy 11",
    long_description="N/A",
    url="https://medium.com/@surya.mereddy",
    license="MIT",
    platforms=["Linux", "Windows"],
    packages=["2020"],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
