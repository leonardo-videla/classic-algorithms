class Pila (object):

    def __init__ (self, lista=None):
        if lista==None:
            lista=[]
        self._puntero=len(lista)-1
        self.__datos=lista

    def push (self, dato):
        self.__datos.append(dato)
        puntero+=1

    def pop (self):
        if self.esta_vacia():
            return
        return  self._datos[puntero]
        puntero-=1

    def esta_vacia(self):
        if punteor<0:
            return True
        return False

    def __str__ (self):
        return str(self.__datos)
