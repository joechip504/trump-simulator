from base import SimulatorBase

class Trump(SimulatorBase):

	def give_speech(self):
		return self.generate_text(minimum = 50)

if __name__ == '__main__':
	trump = Trump(fodder_directory = 'fodder/')
	print('\n{}\n'.format(trump.give_speech()))