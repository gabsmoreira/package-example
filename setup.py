from setuptools import setup
setup(
    name='dev_aberto_gabs',
    version='0.1',
    packages=['dev_aberto'],
    scripts=['scripts/hello.py'],
    author='Gabriel Moreira',
    author_email='gabriel.moreira98@hotmail.com',
    install_requires=['requests>=2.22.0']
)
