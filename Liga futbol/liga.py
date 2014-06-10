#-------------------------------------------------------------------------------

class Equipo():
    def __init__ (self):
        self.__Nombre = ""
        self.__jugadores = []    # LISTA DE Jugadores
        self.__partidos = []     # LISTA DE Partidos jugados

    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nombre):
        if len(Nombre) > 20:
            print ("ERROR")
            return
        self.__Nombre = Nombre

    def getPartidosG(self):
        GanadosCasa = [x for x in self.__partidos if x.getEquipoLocal().getNombre() == self.__Nombre and x.getGolesLocal() > x.getGolesVisitante()]
        GanadosFuera = [x for x in self.__partidos if x.getEquipoVisitante().getNombre() == self.__Nombre and x.getGolesVisitante() > x.getGolesLocal()]
        return len(GanadosCasa) + len(GanadosFuera)

    def getPartidosE(self):
        Empatados = [x for x in self.__partidos if x.getGolesLocal() == x.getGolesVisitante()]
        return len(Empatados)

    def getPartidosP(self):
        PerdidosCasa = [x for x in self.__partidos if x.getEquipoLocal().getNombre() == self.__Nombre and x.getGolesLocal() < x.getGolesVisitante()]
        PerdidosFuera = [x for x in self.__partidos if x.getEquipoVisitante().getNombre() == self.__Nombre and x.getGolesVisitante() < x.getGolesLocal()]
        return len(PerdidosCasa) + len(PerdidosFuera)

    def getGolesF(self):
        TotalGoles = 0
        for x in self.__partidos:
            if x.getEquipoLocal().getNombre() == self.__Nombre:
                TotalGoles += x.getGolesLocal()
            else:
                TotalGoles += x.getGolesVisitante()
        return TotalGoles

    def getGolesC(self):
        TotalGoles = 0
        for x in self.__partidos:
            if x.getEquipoLocal().getNombre() == self.__Nombre:
                TotalGoles += x.getGolesVisitante()
            else:
                TotalGoles += x.getGolesLocal()
        return TotalGoles

    def getPuntos(self):
        TotalPuntos = 0
        for x in self.__partidos:
            if x.getEquipoLocal().getNombre() == self.__Nombre:
                if x.getGolesLocal() > x.getGolesVisitante():
                    TotalPuntos += 3
                elif x.getGolesLocal() == x.getGolesVisitante():
                    TotalPuntos += 1
            else:
                if x.getGolesVisitante() > x.getGolesLocal():
                    TotalPuntos += 3
                elif x.getGolesVisitante() == x.getGolesLocal():
                    TotalPuntos += 1
        return TotalPuntos

    def addJugador (self,jug):
        self.__jugadores.append(jug)

    def addPartido (self,par):
        self.__partidos.append(par)

    def getJugadores(self):
        return self.__jugadores

    def getPartidos(self):
        return self.__partidos

    def Guardar (self,F):
        F.write ("EQ\t");
        F.write (self.getNombre() + "\t")
        F.write ("\n")

    def Recuperar (self,linea):
        trozos = linea.split("\t")
        self.setNombre (trozos[1])

    def Imprimir (self):
        print ("Nombre equipo",self.getNombre())
        print ("Partidos Ganados",self.getPartidosG())
        print ("Partidos Empatados",self.getPartidosE())
        print ("Partidos Perdidos",self.getPartidosP())
        print ("Goles favor",self.getGolesF())
        print ("Goles Contra",self.getGolesC())
        print ("Puntos logrados",self.getPuntos())




class Jugador():
    def __init__ (self):
        self.__Nombre = ""
        self.__equipo = None

    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nombre):
        self.__Nombre = Nombre

    def setEquipo (self,Equip):
        self.__equipo = Equip

    def getEquipo (self):
        return self.__equipo

    def Guardar (self,F):
        F.write ("JU\t");
        F.write (self.__Nombre + "\t")
        F.write (self.__equipo.getNombre() + "\t")
        F.write ("\n")

    def Recuperar (self,linea):
        trozos = linea.split("\t")
        self.__Nombre = trozos[1]
        self.__Apellido = trozos[2]
        self.__Edad = trozos[3]


class Partido():

    def __init__(self):
        self.__eqlocal = None
        self.GolesL=0
        self.__eqvisitante = None
        self.GolesV=0

    def getEquipoLocal(self):
        return self.__eqlocal

    def setEquipoLocal(self,eqlocal):
        self.__eqlocal = eqlocal

    def getGolesLocal(self):
        return int(self.__GolesL)


    def setGolesLocal(self,GolesL):
        self.__GolesL = GolesL

    def getEquipoVisitante(self):
        return self.__eqvisitante

    def setEquipoVisitante(self,eqvisitante):
        self.__eqvisitante = eqvisitante

    def getGolesVisitante(self):
        return int(self.__GolesV)

    def setGolesVisitante(self,GolesV):
        self.__GolesV = GolesV


    def Guardar (self,F):
        F.write ("PA\t");
        F.write (self.__eqlocal.getNombre() + "\t")
        F.write (str(self.__GolesL) + "\t")
        F.write (self.__eqvisitante.getNombre() + "\t")
        F.write (str(self.__GolesV) + "\t")
        F.write ("\n")

class GestionPartidos():
    def __init__(self):
        self.__equipos = []
        self.__jugadores = []
        self.__partidos = []


    def getMejorEquip (self):
        mejor = None
        mejorEquip = -1.0
        for x in self.__equipos:
            if float(x.getGolesF()) > mejorEquip:
                mejorEquip = float(x.getGolesF())
                mejor = x
        return mejor


    def getPeorEquip (self):
        peor = None
        peorNota = 999
        for x in self.__equipos:
            if float(x.getGolesF()) < peorEquip:
                peorEquip = float(x.getGolesF())
                peor = x
        return peor

    def cargarFichero (self):
        self.__equipos = []
        self.__jugadores= []
        self.__partidos= []


        try:
            F = open ("liga.txt","r")
            for x in F:
                datos = x.replace("\n","").split("\t")
                tipo = datos[0]
                if tipo == "EQ":
                    J = Equipo()
                    J.setNombre(datos[1])
                    self.__equipos.append(J)
                if tipo == "JU":
                    J=Jugador()
                    J.setNombre(datos[1])
                    equip = [xx for xx in self.__equipos if xx.getNombre() == datos[2]]
                    J.setEquipo(equip[0])
                    equip[0].addJugador(J)
                    self.__jugadores.append(J)
                if tipo == "PA":
                    J=Partido()
                    equip = [xx for xx in self.__equipos if xx.getNombre() == datos[1]]
                    J.setEquipoLocal(equip[0])
                    J.setGolesLocal(datos[2])

                    equipV = [xx for xx in self.__equipos if xx.getNombre() == datos[3]]
                    J.setEquipoVisitante(equipV[0])
                    J.setGolesVisitante(datos[4])

                    equip[0].addPartido(J)
                    equipV[0].addPartido(J)

                    self.__partidos.append(J)


            F.close()
        except:
            print ("No encuentro el fichero")

    def guardarFichero(self):
        F = open("liga.txt","w")
        for x in self.__equipos:
            F.write("EQ" + "\t" + x.getNombre() + "\n")

        for x in self.__jugadores:
            F.write ("JU" + "\t" + x.getNombre() + "\t" + x.getEquipo().getNombre() + "\n")

        for x in self.__partidos:
            F.write ("PA" + "\t" + x.getEquipoLocal().getNombre() + "\t" + str(x.getGolesLocal()) + "\t" + x.getEquipoVisitante().getNombre() + "\t" + str(x.getGolesVisitante()) + "\n")

        F.close()


    def VisualizarEquipos (self):
        print ("Lista de equipos")
        print ("================")
        Num = 1
        for x in self.__equipos:
         print (Num,x.getNombre())
         Num += 1

    def VisualizarEquipo (self):
        nombre = input("Nombre del equipo")
        equip = [x for x in self.__equipos if x.getNombre() == nombre]
        if len(equip) == 0:
            print ("No existe este equipo")
        else:
            e = equip[0]
            print ("Nombre: ",e.getNombre())
            print ("Jugadores:")
            for j in e.getJugadores():
                print (j.getNombre())

            print ("Partidos jugados:")
            for j in e.getPartidos():
                print (j.getEquipoLocal().getNombre(),j.getGolesLocal(),j.getEquipoVisitante().getNombre(),j.getGolesVisitante())

            print ("Partidos Ganados: ",e.getPartidosG())
            print ("Partidos Empatados: ",e.getPartidosE())
            print ("Partidos Perdidos: ",e.getPartidosP())
            print ("Goles Favor: ",e.getGolesF())
            print ("Goles Contra: ",e.getGolesC())
            print ("Puntos: ",e.getPuntos())


    def agregarEquipo(self):
        m = Equipo()
        s = input ("Nombre: ")
        m.setNombre(s)
        self.__equipos.append(m)

    def borrarEquipo (self):
        num = int(input("Numero de equipo:"))
        if num >=1 and num <= len(self.__equipos):
            # eliminar los jugadores de ese equipo.
            jBorrar = [j for j in self.__jugadores if j.getEquipo().getNombre() == self.__equipos[num-1].getNombre()]
            for j in jBorrar:
                self.__jugadores.remove(j)

            # eliminar los partidos de ese equipo.
            jBorrar = [j for j in self.__partidos if j.getEquipoLocal().getNombre() == self.__equipos[num-1].getNombre() or j.getEquipoVisitante().getNombre() == self.__equipos[num-1].getNombre() ]
            for j in jBorrar:
                self.__partidos.remove(j)

            #  borrar el equipo de la lista
            del self.__equipos[num-1]

        else:
            print ("Numero de equipo incorrecto")

    def modificarEquipo (self):
        m = Equipo()
        num = int(input("Numero de equipo:"))
        if num < 1 or num > len(self.__equipos):
            print ("No hay tantos equipos")
            return
        vAux = input("Nombre: ")
        if vAux!="":
            m.setNombre(vAux)


    def VisualizarJugadores (self):
        print ("Lista de Jugadores")
        print ("================")
        Num = 1
        for x in self.__jugadores:
         print (Num,x.getNombre(),x.getEquipo().getNombre())
         Num += 1


    def agregarJugador(self):
        m = Jugador()
        s = input ("Nombre: ")
        m.setNombre(s)
        nomEquipo = input("Nombre equipo: ")
        equip = [x for x in self.__equipos if x.getNombre() == nomEquipo]
        if len(equip) == 0:
            print ("No existe el equipo")
            return
        equip[0].addJugador (m)
        m.setEquipo(equip[0])
        self.__jugadores.append(m)

    def borrarJugador (self):
        num = int(input("Numero de jugador:"))
        if num >=1 and num <= len(self.__jugadores):
            del self.__jugadores[num-1]
        else:
            print ("Numero de jugador incorrecto")

    def modificarJugador (self):
        m = Jugador()
        num = int(input("Numero de jugador:"))
        if num < 1 or num > len(self.__jugadores):
            print ("No hay tantos jugadores")
            return
        vAux = input("Nombre: ")
        if vAux!="":
            m.setNombre(vAux)

    def visualizarJugador (self):
        m = Jugador()
        num = int(input("Numero de jugador:"))
        if num < 1 or num > len(self.__jugadores):
            print ("No hay tantos jugadores")
            return
        m = self.__jugadores[num-1]
        print ("Nombre: ",m.getNombre())
        print ("Equipo: ",m.getEquipo().getNombre())


    def VisualizarPartidos (self):
        print ("Lista de Partidos")
        print ("================")
        Num = 1
        for x in self.__partidos:
         print (Num,x.getEquipoLocal(),str(x.getGolesLocal()),x.getEquipoVisitante(),str(x.getGolesVisitante()))
         Num += 1


    def agregarPartido(self):
        m = Partido()
        s = input ("equipo local: ")
        elocal = [x for x in self.__equipos if x.getNombre() == s]
        if len(elocal) == 0:
            print ("No existe el equipo")
            return
        m.setEquipoLocal(elocal[0])
        p = input ("Goles local: ")
        m.setGolesLocal(p)

        s = input ("equipo visitante: ")
        evisit = [x for x in self.__equipos if x.getNombre() == s]
        if len(evisit) == 0:
            print ("No existe el equipo")
            return
        m.setEquipoVisitante(evisit[0])
        p = input ("Goles visitante: ")
        m.setGolesVisitante(p)

        self.__partidos.append(m)

        elocal[0].addPartido (m)
        evisit[0].addPartido (m)

    def borrarpartido (self):
        num = int(input("Numero de partido:"))
        if num >=1 and num <= len(self.__partidos):
            del self.__partidos[num-1]
        else:
            print ("Numero de partido incorrecto")

    def modificarPartido (self):
        m = Partido()
        num = int(input("Numero de partido:"))
        if num < 1 or num > len(self.__partidos):
            print ("No hay tantos partidos")
            return
        vAux = input("equipo local: ")
        if vAux!="":
            m.seteqlocal(vAux)
        vAux2 = str(input("Goles local "))
        if vAux2!=0:
            m.setGolesL(vAux2)

        vAux3 = input("equipo visitante: ")
        if vAux3!="":
            m.seteqvisitante(vAux3)
        vAux4 = str(input("Goles visitante "))
        if vAux4!=0:
            m.setGolesv(vAux4)

    def visualizarPartido (self):
        m = Partido()
        num = int(input("Numero de partido:"))
        if num < 1 or num > len(self.__partidos):
            print ("No hay tantos partidos")
            return
        m = self.__partidos[num-1]
        print ("equipo local: ",m.geteqlocal())
        print ("Goles local: ",m.getGolesL())
        print ("equipo visitante: ",m.geteqvisitante())
        print ("Goles visitante: ",m.getGolesV())

    def equipoMasGoles(self):
        equipMax= None
        golesMax = -1
        for x in self.__equipos:
            mejorEquip = x.getGolesF()
            if mejorEquip != None:
                if float(mejorEquip.getGolesF()) > golesMax:
                    equipMax = mejorEquip
                    golesMax = float(mejorEquip.getGolesF())
        if equipMax == None:
            print ("No hay ningun gol")
        else:
            print (equipMax.getNombre(),equipMax.getGolesF())


    def equipoMenosGoles(self):
        equipMin= None
        GolesMin = 999
        for x in self.__equipos:
            PeorEquip = x.getGolesF()
            if PeorEquip != None:
                if float(PeorEquip.getGolesF()) < GolesMin:
                    equipMin = PeorEquip
            golesMin = float(PeorEquip.getGolesF())
        if equipMin == None:
            print ("No hay ningun gol")
        else:
            print (equipMin.getNombre(),equipMin.getGolesF())

    def ClasificacionEquipos (self):
        print ("Lista de equipos")
        print ("================")
        Num = 1
        Ordenados = sorted(self.__equipos,key=GestionPartidos.ObtenerPuntos)
        for x in self.__equipos:
         print (Num,x.getNombre(),x.getPuntos())
         Num += 1

    @staticmethod
    def ObtenerPuntos (x):
        return x.getPuntos()

def Menu():
    print ("Menu:")
    print ("1 - Visualizar equipos")
    print ("2 - Anadir equipo")
    print ("3 - Modificar equipo")
    print ("4 - Eliminar equipo")
    print ("5 - Visualizar equipo")
    print ("6 - Visualizar jugadores")
    print ("7 - Anadir jugadores")
    print ("8 - Modificar jugadores")
    print ("9 - Eliminar jugadores")
    print ("10 - Visualizar partidos")
    print ("11 - Anadir partido")
    print ("12 - Modificar partido")
    print ("13 - Eliminar partido")
    print ("14-Equipo mas goles")
    print ("15-Equipo menos goles")
    print ("16-Clasificacion equipos")
    print ("0 - Salir")
    op = -1
    while op < 0 or op > 16:
        op = int(input("Introducir opcion: "))
    return op



def main():
    gestion = GestionPartidos()
    gestion.cargarFichero()
    opcion = -1
    while opcion != 0:
        opcion = Menu()
        if opcion == 1:
            gestion.VisualizarEquipos()
        elif opcion == 2:
            gestion.agregarEquipo()
        elif opcion == 3:
            gestion.modificarEquipo()
        elif opcion == 4:
            gestion.borrarEquipo()
        elif opcion == 5:
            gestion.VisualizarEquipo()
        elif opcion == 6:
            gestion.visualizarJugador()
        elif opcion == 7:
            gestion.agregarJugador()
        elif opcion == 8:
            gestion.modificarJugador()
        elif opcion == 9:
            gestion.borrarJugador()
        elif opcion == 10:
            gestion.visualizarPartido()
        elif opcion == 11:
            gestion.agregarPartido()
        elif opcion == 12:
            gestion.modificarPartido()
        elif opcion == 13:
            gestion.borrarpartido()
        elif opcion == 14:
            gestion.equipoMasGoles()
        elif opcion == 15:
            gestion.equipoMenosGoles()
        elif opcion == 16:
            gestion.ClasificacionEquipos()





    gestion.guardarFichero()


if __name__ == '__main__':
    main()








