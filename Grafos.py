""" Clase Grafo
"""
import copy
import Merge_Sort
import Cola
import Pila

class Grafo(object): #Construccion de Grafos no dirigidos

    def __init__(self, graph_dict=None):
        """ Inicializa el objeto Grafo con un diccionario
            de adyacencia.
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ Devuelve los vertices del grafo. """
        return list(self.__graph_dict.keys())

    def aristas(self):
        """ Retorna las aristas del grafo. """
        return self.__genera_aristas()

    def esta_presente (self, vertex1, vertex2):
        """ Retorna "True" si la arista esta presente. """
        u=self.__graph_dict
        if vertex1 in u and vertex2 in u[vertex1]:
            return True
        return False

    def agrega_vertice(self, vertex):
        """ Si "vertex" no existe en
            self.__graph_dict, se agrega la clave "vertex"
            con una lista vacia al diccionario.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def agrega_arista(self, vertex1, vertex2):
        """ agrega una arista al grafo: lo asume no-dirigido
        """
        if vertex1 in self.__graph_dict and vertex2 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
            self.__graph_dict[vertex2].append(vertex1)
        elif vertex1 not in self.__graph_dict and vertex2 in self.__graph_dict:
            self.__graph_dict[vertex1]=[vertex2]
            self.__graph_dict[vertex2].append(vertex1)
        elif vertex1 in self.__graph_dict and vertex2 not in self.__graph_dict:
            self.__graph_dict[vertex2]=[vertex1]
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            self.__graph_dict[vertex2] = [vertex1]

    def __genera_aristas(self):
        """ Un metodo estatico que genera las aristas,
            listas para impresion.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges: #Asi evitamos repeticiones
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        """ Asi se imprime un grafo
        """
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\naristas: "
        for edge in self.__genera_aristas():
            res += str(edge) + " "
        return res

    def alcanzables (self, start_vertex):
        #Devuelve el conjunto de vertices alcanzables desde start_vertex. Usa BFS
        if start_vertex not in self.__graph_dict:
            return {}
        c=Cola.Cola([start_vertex])
        explorados={start_vertex}
        while not (c.esta_vacia()):
            u=c.pop()
            for v in self.__graph_dict[u]:
                if v not in explorados:
                    explorados.add(v)
                    c.push(v)
        return explorados

    def DFS (self, start_vertex):
        if start_vertex not in self.__graph_dict:
            return {}
        p=Pila.Pila([start_vertex])
        explorados={}
        while not (p.esta_vacia()):
            u=p.pop()
            if u not in explorados:
                explorados.add(u)
                for v in self._graph_dict[u]:
                    p.push(v)
        return explorados


    def caminos_desde (self, start_vertex):
        if start_vertex not in self.__graph_dict:
            return {}
        c=Cola.Cola([start_vertex])
        explorados={start_vertex : [0, []]}
        while not (c.esta_vacia()):
            u=c.pop()
            for v in self.__graph_dict[u]:
                if v not in explorados:
                    explorados[v]=copy.deepcopy(explorados[u])
                    explorados[v][0]=explorados[u][0]+1
                    (explorados[v][1]).append(u)
                    c.push(v)
        return explorados


    def bosque_generador (self):
        #Encuentra un conjunto de arboles generadores para el grafo. Si el grafo es conexo, devuelve un arbol
        arb=[]
        graph=self.vertices()
        for u in graph:
            arb.append({u})
        arboles=set(frozenset(c) for c in arb)
        ar=self.__genera_aristas()
        aristas_generadoras=[]
        for a in ar:
            lista_ar=list(a)
            v1=lista_ar[0]
            v2=lista_ar[1]
            s1={}
            s2={}
            for conjunto in arboles:
                if v1 in conjunto:
                    s1=conjunto
                if v2 in conjunto:
                    s2=conjunto
            if s1 != s2:
                arboles.discard(s1)
                arboles.discard(s2)
                arboles.add (frozenset(s1.union(s2)))
                aristas_generadoras.append({v1, v2})
        arb=list(set(s) for s in arboles)
        return arb, aristas_generadoras


    def grados(self):
        u=self.__graph_dict
        deg=[]
        for v in u:
            deg.append(len(u[v]))
        return Merge_Sort.Merge_Sort (deg)
