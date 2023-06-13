from PyQt5.QtGui import QPixmap

from utils.Effect import Effect

class EffectApplier:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("create EffectApplier Object")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        pass

    def render(self, effect: Effect, url: str) -> QPixmap:
        return effect.apply(url)


if __name__ == "__main__":
    pass