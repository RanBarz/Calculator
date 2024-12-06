class TreeNode:
    def __init__(self, value = 0):
        self.__value = value
        self.__right = None
        self.__left = None

    def set_right(self, node):
        self.__right = node

    def get_right(self):
        return self.__right

    def set_left(self, node):
        self.__left = node

    def get_left(self):
        return self.__left

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
