from abc import ABC, abstractmethod


class Effect(ABC):

    @abstractmethod
    def apply(self):
        pass



class PencilEffect(Effect):

    def apply(self):
        pass


class CartoonEffect(Effect):

    def apply(self):
        pass

