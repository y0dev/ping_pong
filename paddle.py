import pygame

class Paddle():
	def __init__(self,ai_settings,screen, pos, score):
		self.screen = screen
		self.screen_height = ai_settings.screen_height
		self.width  = ai_settings.paddle_width
		self.height = ai_settings.paddle_height
		self.color  = ai_settings.paddle_color

		self.pos    = pos
		self.vel    = 0
		self.score  = score

	def draw_paddle(self):
		pygame.draw.line(self.screen, self.color, (self.pos[0], self.pos[1] - self.height/2), (self.pos[0], self.pos[1] + self.height/2), self.width)

	def update(self):
		if self.pos[1]+self.vel > int(self.height/2) and self.pos[1]+self.vel < int(self.screen_height-self.height/2):
			self.pos[1]=self.pos[1]+self.vel

	def play_sound(self):
		try:
			pygame.mixer.music.load('sounds/hit.wav')
			pygame.mixer.music.play()
		except :
			pass