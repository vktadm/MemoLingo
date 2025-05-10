from dataclasses import dataclass


@dataclass
class GeneratorSettings:
    mako_root: str = "./templates/"
    app_root: str = "../app/"


settings = GeneratorSettings()
