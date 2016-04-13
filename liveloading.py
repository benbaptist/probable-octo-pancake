import websocket
import threading
import time

class Liveloading:
	def __init__(self, socketize=None):
		self.socketize = socketize
		self.workers = []
		self.sluggiesToBeMadeIntoMen = []
	def subscribe(self, slug, callback):
		worker = self.getWorker()
		# self.sluggiesToBeMadeIntoMen.append([slug, callback])
	def getWorker(self):
		if len(self.workers) < 1:
			worker = Worker()
			self.workers.append(worker)
	def run(self):
		while True:
			time.sleep(0.1)

class Worker:
	def __init__(self, socketize=None):
		self.thread = threading.Thread(target=self.salad, args=())
		self.thread.daemon = True
		self.thread.start()

		self.sluggies = []
	def salad(self):
		""" It handles many salad. """
		while not self.abort:
			try:
				self.connect()
				self.handle()
			except:
				pass

			time.sleep(1)
	def connect(self):
		self.ws = websocket.WebSocket()
		self.ws.connect("wss://realtime.beam.pro/socket.io/?EIO=3&transport=websocket")
