# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:59:20 2021

@author: ryan_
"""

import time
import pygame
import random
import keyboard


pygame.mixer.init()


def chest_back():
    countdown=[r"C:\Users\ryan_\Music\workout\countdown.mp3"]
    breaktime=[r"C:\Users\ryan_\Music\workout\break.mp3"]
    exercise=[r"C:\Users\ryan_\Music\workout\pushup.mp3",r"C:\Users\ryan_\Music\workout\declined_bench_press.mp3"]
    count=[r"C:\Users\ryan_\Music\workout\count.mp3"]
    for i in range(0,8):
        pygame.mixer.music.load(random.choice(exercise))
        pygame.mixer.music.play()
        if keyboard.is_pressed('a'):
            pygame.mixer.music.load(countdown)
            pygame.mixer.music.play()
            time.sleep(4)
            pygame.mixer.music.load(random.choice(count))
            pygame.mixer.music.play()
            if keyboard.is_pressed('a'):
                pygame.mixer.music.load(random.choice(breaktime))
                pygame.mixer.music.play()
                time.sleep(20)

while True:
    if keyboard.is_pressed('q'):
        chest_back()
        
      


    
    
    

    
    
    
    
    
    
    