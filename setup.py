from setuptools import setup, Extension

setup(
    name="cibuildwheel_autopypi_example",
    ext_modules=[Extension('cibuildwheel_autopypi_example', sources=['cibuildwheel_autopypi_example.c'])],
    version="0.1.17",
)
