import ipdb

class Person ():
    def __init__(self,name) -> None:
        self._name = name

    def get_name(self):
        return self._name
    
    
    name = property (get_name)
    


if __name__ == "__main__":
    print ("Am run directly")

    ipdb.set_trace()
