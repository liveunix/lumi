from setuptools import setup, find_packages

setup(
    name="lumi",
    description="",
    version="0.1.0",
    author="Danilo Spinella, Luca Di Vita, Domenico Corvasce",
    author_email="danyspin97@protonmail.com, d.v.luca99@gmail.com, dom.corvasce@yandex.com",
    url="https://www.liveunix.org",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["lumi-gui=lumi.gui:main", "lumi=lumi.cli.command_line:main"]
    },
)
