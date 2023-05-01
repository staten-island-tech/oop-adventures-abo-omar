class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items or []

    def __str__(self):
        return self.name


class Item:
    def __init__(self, name, description, point_value):
        self.name = name
        self.description = description
        self.point_value = point_value

    def __str__(self):
        return self.name


class Character:
    def __init__(self, name, description, point_value):
        self.name = name
        self.description = description
        self.point_value = point_value

    def __str__(self):
        return self.name
