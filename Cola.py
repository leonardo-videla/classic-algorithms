class Cola (object):

    def __init__ (self, lista=None):
        if lista==None:
            lista=[]
        self.__datos=lista

    def push (self, dato):
        self.__datos.append(dato)

    def pop (self):
        if self.esta_vacia():
            return
        r=self.__datos[0]
        if len(self.__datos)==1:
            self.__datos=[]
        else:
            self.__datos=self.__datos[1:]
        return r

    def esta_vacia(self):
        if len(self.__datos)==0:
            return True
        return False

    def __str__ (self):
        return str(self.__datos)
