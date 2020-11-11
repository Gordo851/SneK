# -*- coding: utf-8 -*-

import pygame
import modelMaster as model
import time
import random
import csv
import numpy as np
(width, height) = (500, 500)
background_colour = (255,255,255)


dataModel = model.board()
agent = model.Agent()
head = 1225
tail = 1225
direction = "DOWN"
snake = model.snake(head, tail, direction)
#


"""
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('snek')
pygame.display.flip()
#"""

dataStates = []

for x in range(0,5):
	
	snake = model.snake(head, tail, direction)
	point = 1230
	frameCounter = 0
	running = True
	counter = 0
	score = 0
	while running:
		counter = counter + 1
		if counter > 100000:
			running = False
			continue
		oldState = agent.getState(dataModel, snake, point)
		oldReward = agent.getReward(oldState, eaten=False)
		
		
		"""
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_ESCAPE]:
				running = False
				pygame.quit()
			
			if pressed[pygame.K_UP]:
				snake.setDirection("UP")
			if pressed[pygame.K_DOWN]:
				snake.setDirection("DOWN")
			if pressed[pygame.K_RIGHT]:
				snake.setDirection("RIGHT")
			if pressed[pygame.K_LEFT]:
				snake.setDirection("LEFT")
		#"""
		snake.direction = agent.get_random_move(snake)
			
		eaten = model.snake.updateSnake(snake, point)
		
		for n in range(0, len(snake.body)):
			squares = snake.body[n]
			dataModel.squares[squares].colourState = "BLACK"
		dataModel.squares[snake.tail].colourState = "WHITE"
		
		
		
		if eaten == True:
			score = score + 1
			point = np.random.randint(100,2400)
			#if dataModel.squares[point].colourState == "BLACK":
			#	point = np.random.randint(100,2400)
				
		
		
		
		
		
		if point > 2400:
			point == 1220
		if point < 50:
			point = 100
		dataModel.squares[point].colourState = "BLACK"
		"""
		for square in dataModel.squares:
			if square.getColourState() == "WHITE":
				pygame.draw.rect(screen, (255, 255, 255),  (square.getX(),  
						 square.getY(),   square.getSize(),   square.getSize()))
			if square.getColourState() == "BLACK":
				pygame.draw.rect(screen, (0, 0, 0),  (square.getX(),  
						 square.getY(),   square.getSize(),   square.getSize()))
		#"""
		#colide = snake.checkColision()
		#if colide:
		#	print("GAME OVER")
		#	running = False
			#pygame.quit()
		#time.sleep(1)
		
		state = agent.getState(dataModel, snake, point)
		reward = agent.getReward(state, eaten)
		rewardFinal = reward-oldReward
		#print("Old:",oldReward, "New:",reward, "Final", rewardFinal)
		#if colide:
		#	reward = -1000
		FinalState = []
		FinalState.append(oldState[0])
		FinalState.append(oldState[1])
		FinalState.append(state[2])
		FinalState.append(state[3])
		FinalState.append(reward)
		
		
		dataStates.append(FinalState)
		#print(oldState)
		#time.sleep(0.1)
	print(score)
	
	
agent.train_model(dataStates)



dataModel = model.board()
head = 1225
tail = 1225
direction = "DOWN"
snake = model.snake(head, tail, direction)
dataStates = []
screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption('snek')
#screen.fill(background_colour)


pygame.display.flip()


point = 1230
running = True
while running:
	pygame.display.update()	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_ESCAPE]:
			running = False
			pygame.quit()
	
	agent.getDirections(snake, dataModel, point)
	
	
	eaten = model.snake.updateSnake(snake, point)
	
	for n in range(0, len(snake.body)):
		squares = snake.body[n]
		dataModel.squares[squares].colourState = "BLACK"
	
	dataModel.squares[snake.tail].colourState = "WHITE"
	
	
	if eaten == True:
		point = np.random.randint(100,2400)
	if point > 2400:
		point == 1220
	if point < 50:
		point = 100
	dataModel.squares[point].colourState = "BLACK"
	
		
	for square in dataModel.squares:
		if square.getColourState() == "WHITE":
			pygame.draw.rect(screen, (255, 255, 255),  (square.getX(),  
					 square.getY(),   square.getSize(),   square.getSize()))
		if square.getColourState() == "BLACK":
			pygame.draw.rect(screen, (0, 0, 0),  (square.getX(),  
					 square.getY(),   square.getSize(),   square.getSize()))
	colide = snake.checkColision()
	"""
	if colide:
		print("GAME OVER")
		running = False
		pygame.quit()
		continue
	"""
	# if the current dot has been eaten then produce a new one
	#time.sleep(1)
	
	
	







