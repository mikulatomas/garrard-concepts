from enum import Enum

__all__ = ["Category", "Domain", "Language", "FeatureType"]


class Language(Enum):
    ENGLISH = "en"

    def __str__(self):
        return self.name.title()


class FeatureType(Enum):
    EXEMPLAR = "exemplar"

    def __str__(self):
        return self.name.title()


class StringMixin:
    @classmethod
    def from_str(cls, label):
        label = label.lower()
        label = label.rstrip("s")
        label = label.replace("_", " ")

        return cls(label)

    def to_filename(self):
        return self.value.replace(" ", "_")

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        return self.value.title().replace(" ", "")


class Category(StringMixin, Enum):
    ANIMAL = "animal"
    BIRD = "bird"
    FRUIT = "fruit"
    HOUSEHOLD_ITEM = "household item"
    TOOL = "tool"
    VEHICLE = "vehicle"


class Domain(StringMixin, Enum):
    LIVING = "living"
    NONLIVING = "nonliving"
    WORLD = "world"

    @property
    def members(self):
        if self == Domain.LIVING:
            return (Category.ANIMAL, Category.BIRD, Category.FRUIT)
        elif self == Domain.NONLIVING:
            return (Category.HOUSEHOLD_ITEM, Category.TOOL, Category.VEHICLE)
        else:
            return (
                Category.ANIMAL,
                Category.BIRD,
                Category.FRUIT,
                Category.HOUSEHOLD_ITEM,
                Category.TOOL,
                Category.VEHICLE,
            )
