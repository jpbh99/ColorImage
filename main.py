import numpy as np
import cv2
import os

class colorimage:

    def __init__(self,path):    # Se define el constructor
        self.path_file = path   # Se almacena la direccion de la ruta
        self.image = cv2.imread(self.path_file) # Se almacena la imagen
        cv2.imshow('IMAGEN', self.image)    # Se muestra la imagen
        cv2.waitKey(0)  # Espera que se presione una tecla
        cv2.destroyAllWindows() # Cierra las ventanas


    def displayProperties(self):    # Se define el metodo
        height = int(self.image.shape[0])   # Obtiene el valor de la altura
        width = int(self.image.shape[1])    # Obtiene el valor del ancho
        print("La altura es: " + str(height))   # Se muestra el valor del largo
        print("El ancho es: " + str(width)) # Se muestra el valor del ancho


    def makeGray(self): # Se define el metodo
        self.image_BW = cv2.imread(self.path_file,0)    # Se almacena la imagen en escala de grises
        cv2.imshow('IMAGEN', self.image_BW) # Se muestra la imagen
        cv2.waitKey(0)  # Espera que se presione una tecla
        cv2.destroyAllWindows() # Cierra las ventanas

    def colorizeRGB(self,channel):  # Se define el metodo
        #B, G, R = cv2.split(self.image) # Se divide los componentes BGR de la imagen
        self.image_BW = cv2.imread(self.path_file,0)    # Se almacena la imagen en escala de grises
        zeros = np.zeros(self.image_BW .shape, np.uint8) # Se define una matriz de zeros

        #Bgr = cv2.merge((B, zeros, zeros))  # Se unen los componentes
        #bGr = cv2.merge((zeros, G, zeros))
        #bgR = cv2.merge((zeros, zeros, R))


        if (channel == "Azul"):
            Bgr = cv2.merge((self.image_BW, zeros, zeros))  # Se unen los componentes
            cv2.imshow('AZUL', Bgr) # Se muestra la imagen
        elif (channel == "Verde"):
            bGr = cv2.merge((zeros, self.image_BW, zeros))  # Se unen los componentes
            cv2.imshow('VERDE', bGr) # Se muestra la imagen
        elif(channel == "Rojo"):
            bgR = cv2.merge((zeros, zeros, self.image_BW))  # Se unen los componentes
            cv2.imshow('ROJO', bgR) # Se muestra la imagen
        else:
            print("Color no valido")

        cv2.waitKey(0)  # Espera que se presione una tecla
        cv2.destroyAllWindows() # Cierra las ventanas


    def makeHue(self):
        HSV = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # Se convierte a HSV

        H, S, V = cv2.split(HSV)    # Se dividen los componentes HSV

        S[:,:] = 254    # Se modifican los alores de la matriz
        V[:,:] = 254    # Se modifican los alores de la matriz
        HSV = cv2.merge((H, S, V)) # Se unen los componentes

        imagen = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)   # Se convierte a BGR
        cv2.imshow("IMAGEN", imagen)    # Se muestra la imagen

        cv2.waitKey(0)  # Espera que se presione una tecla
        cv2.destroyAllWindows() # Cierra las ventanas


if __name__ == '__main__':


    while (1):
        print("\n" + "A- Ingresar direccion de imagen")  # Se imprime en consola
        print("B- Visualizar ancho y alto de imagen")  # Se imprime en consola
        print("C- Visualizar imagenes en grises")  # Se imprime en consola
        print("D- Colorizar imagen")  # Se imprime en consola
        print("E- Visualizar colores resaltados")  # Se imprime en consola
        print("?- Salir" + "\n")  # Se imprime en consola
        Entrada = input("Escoja una opcion: ")  # Se pide un valor


        if (Entrada == 'A'):
            Entrada = input("Ingrese direccion de imagen: ")    # Se pide un valor
            Imagen = colorimage(Entrada)    # Se llama al metodo
        elif (Entrada == 'B'):
            Imagen.displayProperties()  # Se llama al metodo
        elif (Entrada == 'C'):
            Imagen.makeGray()   # Se llama al metodo
        elif (Entrada == 'D'):
            Entrada = input("Ingrese color (Rojo, Verde, Azul): ")  # Se pide un valor
            Imagen.colorizeRGB(Entrada) # Se llama al metodo
        elif (Entrada == 'E'):
            Imagen.makeHue()    # Se llama al metodo
        else:
            break   # Rompe while

#C:\Users\juanp\Desktop\lena.png