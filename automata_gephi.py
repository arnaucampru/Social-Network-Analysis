#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:49:01 2019

@author: dnhernando
"""

import pyautogui 
import time
import sys
import os
import subprocess
USER = "dnhernando"
pyautogui.PAUSE = 0.4
class Automata:
    def get_actual_pos(self):
        return pyautogui.position()
    def get_zero_pos(self):
        pyautogui.moveTO(0,0)
    def wait(self):
        time.sleep(0.3)
    def start_movement(self):
        raise ValueError("No esta implementada la funció")
    def set_slash(self):
        pyautogui.keyDown('shift')
        pyautogui.keyDown('7')
        pyautogui.keyUp('7')
        pyautogui.keyUp('shift')
        
    def write(self,string,salto_de_linea=False):
        if not salto_de_linea:  return pyautogui.typewrite(string)
        string+="\n"
        return  pyautogui.typewrite(string)
    def tap_intro(self):
        pyautogui.press("\n")
    
    def open_terminal(self):
     pyautogui.keyDown('ctrl')
     pyautogui.keyDown('alt')
     pyautogui.keyDown('t')

     pyautogui.keyUp('ctrl')
     pyautogui.keyUp('alt')
     pyautogui.keyUp('t')
    
    
print(os.system("ls"))
def get_mouse_pos_on_time(n):
    time.sleep(n)
    return autopy.mouse.location()

def ir_principio():
    pyautogui.moveTO(0,0)

     
     
def start_movemnt(ruta_a_executable_de_gephi,comanda_per_executar_gephi):
    open_terminal()

    time.sleep(0.4)
    
    time.sleep(0.3)
    
    
    time.sleep(0.3)
    pyautogui.typewrite("cd Escritorio\n")
    time.sleep(0.3)
    pyautogui.typewrite("cd gephi-0.9.2\n")
    time.sleep(0.3)
    pyautogui.typewrite("cd bin\n")
    time.sleep(0.3)
    pyautogui.typewrite(".")
    time.sleep(0.3)
    
    time.sleep(0.3)
    pyautogui.typewrite("gephi -J-Dnetbeans.logger.console=false -J-ea --branding gephi --jdkhome /usr/lib/jvm/java-8-openjdk-amd64\n")

class PY_Gephi_automota(Automata):
    
    def __init__(self):
        self.open_terminal()

        self.write("cd Escritorio",True)
        self.write("cd gephi-0.9.2",True)
        self.write("cd bin",True)
        self.write(".")
        self.set_slash()
        self.write("gephi -J-Dnetbeans.logger.console=false -J-ea --branding gephi --jdkhome ")
        self.set_slash()
        self.write("usr")
        self.set_slash()
        self.write("lib")        
        self.set_slash()
        self.write("jvm")
        self.set_slash()
        self.write("java-8-openjdk-amd64",True)
        
        '''Aprovechamos capacidad de Iniit para poner el main aqui'''
        time.sleep(5)
        self.open_project('a',[[587,399]])
        self.gent_stadistics(["Grado Medio","Grado Medio con pesos","Diàmetro de la red","Dendsidad del grafo","HITS","Page Rank","Componentes Conexos"])
        self.export_image("Grafo.png")
    def open_project(self,ruta,clicks,n=0):
            if os.path.isdir('/home/'+USER+'/Grafos'):
                print('La carpeta existe.')
            else:
                self.open_terminal()
                self.write("mkdir Grafos",True)
                time.sleep(2)
                pyautogui.click(878,123)
            
            
            pyautogui.click(clicks[0][0],clicks[0][1])
            pyautogui.moveRel(-10,-125)
            pyautogui.click()
            pyautogui.moveRel(0,75)
            pyautogui.click()
            pyautogui.moveRel(0,135)
        
            pyautogui.click()
            self.write("LesMiserables.gexf")
            pyautogui.moveRel(500,58)
            pyautogui.click()
            pyautogui.moveRel(-140,108)
            pyautogui.click()
            
    def gent_stadistics(self,list_of_stadistics,start_posx=1310.0,start_posy=308.0,sumax=0,sumay=40.0):
        dic = {"Grado Medio":[0,False],"Grado Medio con pesos":[1,False],"Diàmetro de la red":[2,True],"Dendsidad del grafo":[3,True],"HITS":[4,True],"Page Rank":[5,True],"Componentes Conexos":[6,True]}
        pyautogui.moveRel(100,0)
        self.get_actual_pos()
    
        pyautogui.moveRel(100,0)
        pyautogui.moveTo(start_posx,start_posy)
        for x in dic:
            if x in list_of_stadistics:
                pyautogui.moveTo(start_posx,start_posy+dic[x][0]*sumay)
                pyautogui.click()
                if dic[x][1]:
                    pyautogui.press("enter")
                time.sleep(0.2)
                self.close_emergent_statistics((1045.0,120.0))
        self.export_data_to_file("Grafo_info.csv")
        
    def close_emergent_statistics(self,place):
        pyautogui.moveTo(place[0],place[1])
        pyautogui.click()
    
    def export_data_to_file(self,filename):
        pyautogui.moveTo(303.0, 97.0)
        pyautogui.click()
        pyautogui.moveTo(954.0, 178.0)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite(filename)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.moveTo(130.0, 90.0)
        time.sleep(0.1)
        pyautogui.click()
    def export_image(self,file_name):
        pyautogui.moveTo(108.0, 57.0)
        pyautogui.click()
        pyautogui.moveTo(108.0, 57.0)
        time.sleep(0.3)
        pyautogui.moveTo(455.0, 398.0)
        pyautogui.click()
if __name__=='__main__':
    PY_Gephi_automota()
    
        
        
    