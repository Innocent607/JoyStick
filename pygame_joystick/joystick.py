import pygame, sys, random
import socket
from socket import socket

class managers():

	def __init__(self, size, caption):
		"""
		Handles pygame display controls
		
		"""
		self.size = size
		self.caption = caption
		
	def _background(self, screen):
		#background = pygame.Surface(screen.get_size())
		background = pygame.Surface(screen.get_size())
		return background.convert()
		
	def _screen(self):
		return pygame.display.set_mode(self.size)
		
	def _caption(self):
		pygame.display.set_caption(self.caption)
		
	
class Joy():
	def __init__(self, color=(255, 0, 12)):
		self.managers = managers(size=(640, 480), caption="Joystick Testing / XBOX360 Controller")
		self.color = color
		
		
	def main(self):
	
		#screen, background = connect()
		joysticks = []
		display = self.managers._screen()
		self.managers._caption()
		background = self.managers._background(display)
		background.fill(self.color)
		
		clock = pygame.time.Clock()
		keepPlaying = 1
		#for all the connected joysticks
		for i in range (0, pygame.joystick.get_count()):
		    #create a joystick object in our list
		    joysticks.append(pygame.joystick.Joystick(i))
		    #initialize them all (-1 ---> loop forever)
		    joysticks[-1].init()
		    #print  a statement what the name of the controller is
		    print ('detected', joysticks[-1].get_name())
	
		while keepPlaying:
		    clock.tick(60)
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            print ('recieved event, exiting')
		            keepPlaying=0
		            
		        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
		            print ('escape key pressed... exiting')
		            keepPlaying=0
		            
		        elif event.type == pygame.KEYDOWN:
		            print ('key down pressed', event.key)
		            
		        elif event.type == pygame.KEYUP:
		            print ('key up pressed', event.key)                
		            
		        elif event.type == pygame.MOUSEBUTTONDOWN:
		            print ('Mouse button', event.button, 'down at',pygame.mouse.get_pos())
		            
		        elif event.type == pygame.MOUSEBUTTONUP:
		            print ('Mouse button', event.button, 'up at',pygame.mouse.get_pos())
		            
		            if event.button == 0: 
		                background.fill((255, 0, 0))
		            elif event.button == 1: 
		                background.fill((0, 0, 255))
		        elif event.type == pygame.JOYBUTTONUP: 
		            print ('Joystick', joysticks[event.joy].get_name(),'button', event.button,'up')
		            if event.button == 0:
		                background.fill((255, 255, 255))
		            elif event.button == 1:
		                background.fill((255, 255, 255))
		        elif event.type == pygame.JOYHATMOTION:
		            print('Joystick', joysticks[event.joy].get_name(),'hat', event.hat,'moved')
		            
		screen.blit(background, (0, 0))
		pygame.display.flip()
		            

pygame.init()
joy = Joy()
joy.main()  

