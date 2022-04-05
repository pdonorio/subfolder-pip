from setuptools import setup, find_packages

requirements = ["glom", "parse_it"]
# app_location = 'cli.__main__:app'

setup(
    name="subfolder",
    version="0.0.1",
    author="Paradigm Co.",
    author_email="paolo.donoriodemeo@paradigm.co",
    install_requires=requirements,
    packages=find_packages(),
    # packages=['subfolder'],
    # entry_points={
    #     'console_scripts': [f'myapp={app_location}', f'ma={app_location}']
    # },
)
