import threading
import time
#INSTANCIA DE SEMAFORO CON PARAMETRO 1
mutex = threading.Semaphore(1)


class TenedorFilosofo(threading.Thread):
    #CONSTRUCTOR E INICIARDOR DE LA CLASE TENEDORFILOSO
    def __init__(self, tenedores, filosofosNum):
        #ASIGNACIÓN DE REFERENCIAS CON LAS VARIABLES
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal = ((self.filosofosNum + 1) % 5)

    def hilosFilosofos(self):
        while True:
            #IMPRIME EL ID DE HILO Y QUIEN LO INICIA Y EL QUE SIGUE
            print("Filosofo iniciando", self.filosofosNum)
            print("ID: ", self.datoTemporal)
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "pasando tenedor del lado izquierdo")
            self.tenedores[self.filosofosNum].acquire()
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
            self.tenedores[self.datoTemporal].acquire()
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "libre derecho")
            self.tenedores[self.datoTemporal].release()
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "libre izquierdo")
            self.tenedores[self.filosofosNum].release()
            time.sleep(2)
            #LIBERACIÓN DEL HILO
            mutex.release()
            break;
    #EJECUTA EL METODO RUN DONDE LOS PROCESOS SE EJECUTAN
    def run(self):
        self.hilosFilosofos()


tenedorArray = [1, 1, 1, 1, 1]
#ASIGNACIÓN DE RANGOS ENTRE 0 Y 5
for i in range(0, 5):
    print("for uno: ", i)
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(0, 5):
    #BLOQUEO DE HILO
    mutex.acquire()
    print("for dos: ", i)
    total = TenedorFilosofo(tenedorArray, i)
    total.start()