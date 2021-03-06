import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="tangsheng",
  version="0.0.1",
  author="tangsheng",
  author_email="imtangsheng@outlook.com",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/imtangsheng/pypi_tangsheng",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  python_requires='>=3.9',
)