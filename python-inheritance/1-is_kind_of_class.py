"""
module will be used later
"""
def is_kind_of_class(obj, a_class):
    """
    use function is_same_class() to confirm the instance of a class
    """
    if isinstance(obj, a_class):
        """
        use function isinstance function to confirm the instance of a class
        """
        return True
    if isinstance(obj, type):
        return issubclass(obj, a_class)
    return False