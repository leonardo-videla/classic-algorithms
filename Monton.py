import math

class Monton (object):

    def __init__ (self, lista=None):
        if lista==None:
            lista=[]
        self._datos=[]
        for i in range(len(lista)):
            self.push(lista[i])

    def push (self, dato):
        self._datos.append(dato)
        p=len(self._datos)
        q=math.floor(p/2)
        while q >= 1 and self._datos[q-1][1] > self._datos[p-1][1]:
            s=self._datos[q-1]
            self._datos[q-1]=self._datos[p-1]
            self._datos[p-1]=s
            p=q
            q=math.floor(p/2)


    def extrae_minimo (self):
        if self.esta_vacia():
            return None
        if len(self._datos)==1:
            return self._datos.pop()

        ret=self._datos[0]
        element=self._datos.pop()
        self._datos[0]=element
        l=len(self._datos)
        m=m1=m2=10000000
        k=0
        p=1
        if 2*p <= l:
            m1=self._datos[2*p-1][1]
        if 2*p + 1 <= l:
            m2=self._datos[2*p][1]
        if m2 < m1:
            m=m2
            k=2*p+1
        if m1 <= m2:
            m=m1
            k=2*p
        while m < self._datos[p-1][1]:
            s=self._datos[k-1]
            self._datos[k-1]=self._datos[p-1]
            self._datos[p-1]=s
            m=m1=m2=10000000
            p=k
            k=0
            if 2*p <= l:
                m1=self._datos[2*p-1][1]
            if 2*p +1 <= l:
                m2=self._datos[2*p][1]
            if m2< m1:
                m=m2
                k=2*p+1
            if m1 <= m2:
                m=m1
                k=2*p
        return ret


    def esta_vacia(self):
        if len(self._datos)<=0:
            return True
        return False

    def __str__ (self):
        return str(self._datos)
