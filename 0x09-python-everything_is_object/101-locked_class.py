#!/usr/bin/python3
"""MOdule for a new class"""


class LockedClass:
    """Class to allow only one instance attribute"""

    def __setattr__(self, name, value):
        """Instance to disallow new attribute creatiion"""

        if not hasattr(self, name) and name != "first_name":
            raise AttributeError(f"Cannot add new attribute '{name}'")
        super().__setattr__(name, value)
