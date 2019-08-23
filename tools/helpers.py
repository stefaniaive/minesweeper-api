
class Helpers(object):
    @staticmethod
    def get_max(num1,num2):
        if num1>num2:
            return num1

        return num2

    @staticmethod
    def get_min(num1,num2):
        if num1<num2:
            return num1
        return num2


helpers = Helpers()