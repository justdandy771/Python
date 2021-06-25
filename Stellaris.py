# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:55:49 2020

@author: Ryan
"""


import random
import sys 

ethics = ['Spiritualist','Militarist','Xenophobe','Authoritarian','Gestalt Consciousness','Egalitarian',
          'Xenophile','Pacifist','Materialist','Machine Intelligence']


hive_mind_civic=['Ascetic','Divided Attention','Natural Neural Network','One Mind','Pooled Knowledge',
                 'Strength of Legions','Subspace Ephapse','Subsumed Will','Empath','Devouring Swarm',
                 'Terravore']

machine_intelligence_civics=['Machine Builder','Delegated Functions','Factory Overclocking','Introspective',
                             'Maintenance Protocols','OTA Updates','Rapid Replicator','Rockbreakers',
                             'Static Research Analysis','Unitary Cohesion','Warbots','Zero-Waste Protocols',
                             'Determined Exterminator','Driven Assimilator','Rogue Servitor']




roll1=random.choice(ethics)
ethics=['Spiritualist','Militarist','Xenophobe','Authoritarian','Egalitarian','Xenophile','Pacifist','Materialist']
if roll1 == 'Spiritualist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll1 == 'Militarist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll1 == 'Xenophobe':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')
if roll1 == 'Authoritarian':
    ethics.remove('Authoritarian')
    ethics.remove('Egalitarian')
if roll1 == 'Egalitarian':
    ethics.remove('Egalitarian')
    ethics.remove('Authoritarian')
if roll1 == 'Pacifist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll1 == 'Materialist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll1 == 'Xenophile':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')


roll2=random.choice(ethics)


if roll2 == 'Spiritualist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll2 == 'Militarist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll2 == 'Xenophobe':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')
if roll2 == 'Authoritarian':
    ethics.remove('Authoritarian')
    ethics.remove('Egalitarian')
if roll2 == 'Egalitarian':
    ethics.remove('Egalitarian')
    ethics.remove('Authoritarian')
if roll2 == 'Pacifist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll2 == 'Materialist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll2 == 'Xenophile':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')
    
    
roll3=random.choice(ethics)


if roll3 == 'Spiritualist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll3 == 'Militarist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll3 == 'Xenophobe':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')
if roll3 == 'Authoritarian':
    ethics.remove('Authoritarian')
    ethics.remove('Egalitarian')
if roll3 == 'Egalitarian':
    ethics.remove('Egalitarian')
    ethics.remove('Authoritarian')
if roll3 == 'Pacifist':
    ethics.remove('Militarist')
    ethics.remove('Pacifist')
if roll3 == 'Materialist':
    ethics.remove('Spiritualist')
    ethics.remove('Materialist')
if roll3 == 'Xenophile':
    ethics.remove('Xenophobe')
    ethics.remove('Xenophile')    
    
    
fanatic=random.randint(0,10)

if roll1 == 'Gestalt Consciousness':
   civic=random.choice(hive_mind_civic)
   print(civic+' - '+'Gestalt Consciousness') 
   sys.exit()
   
if roll1 == 'Machine Intelligence':
   civic=random.choice(machine_intelligence_civics)
   print(civic+' - '+'Machine Intelligence') 
   sys.exit()
   
if fanatic >= 2 and roll1 !='Gestalt Consciousness' and roll1 !='Machine Intelligence':
    print('Fanatic '+roll1+', '+roll2)
if fanatic < 2:
    print(roll1+', '+roll2+', '+roll3)





