class Configuration:
    """
    Updating a .json dict
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
