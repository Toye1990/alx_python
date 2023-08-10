def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    if isinstance(obj, type):
        return issubclass(obj, a_class)
    return False