"""lambdata - a collection of Data Science helper functions
"""

import setuptools

REQUIRED = [
	"numpy"
	"pandas"
]

with open("README.md", "r") as fh:
	LONG_DESCRIPTION = fh.read()

setuptools.setup(
	name="lambdata"
	version="0.0.1"
	author="lambdata_blakelobato"
	descripton="A collection of DS helper functions",
	long_description=LONG_DESCRIPTION,
	long_description_content_type="text/markdown",
	url="https://github.com/blakelobato/lambdata_bpl",
	packages=setuptools.find_packages(),
	python=requires=">=3.5",
	install_requires=REQUIRED,
	classifiers=[
		"Programming Language :: Pyton :: 3",
		"License :: OSI Approved :: MIT License",
		"Operation System :: OS Independent",
	],
)

