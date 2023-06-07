


class EffectApplier:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("create object")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        pass

    def render(self) -> None:
        pass


if __name__ == "__main__":
    pass