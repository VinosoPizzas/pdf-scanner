import cv2 as cv
import pytesseract
import glob


class PdfScanner:
	def __init__(self, img):
		self.img = cv.imread(img)
		if self.img is None:
			sys.exit("Could not read the image.")
		
		self.scale_percent = 18
		self.width = int(self.img.shape[1] * self.scale_percent / 100)
		self.height = int(self.img.shape[0] * self.scale_percent / 100)
		self.dim = (self.width, self.height)

		self.resized = cv.resize(self.img, self.dim, interpolation = cv.INTER_AREA)

		# variáveis para as coordenadas dos retângulos (x,y)
		self.start_point_nome = (363,121)
		self.end_point_nome = (430,132)

		self.start_point_solucao = (18,245)
		self.end_point_solucao = (520,418)

		self.start_point_tempo = (87,465)
		self.end_point_tempo = (107,475)

		self.start_point_servico = (348,16)
		self.end_point_servico = (405,30)

		# cor (R,G,B)
		self.AZUL = (255,0,0)

		# expessura 
		self.thickness = 2

		# instanciação dos retângulos
		self.nome = cv.rectangle(self.resized, self.start_point_nome, self.end_point_nome, self.AZUL, self.thickness)
		self.solucao = cv.rectangle(self.resized, self.start_point_solucao, self.end_point_solucao, self.AZUL, self.thickness)
		self.tempo = cv.rectangle(self.resized,self.start_point_tempo, self.end_point_tempo, self.AZUL, self.thickness)
		self.servico = cv.rectangle(self.resized, self.start_point_servico, self.end_point_servico, self.AZUL, self.thickness)
		
		#leitura dos dados da imagem
		self.data = pytesseract.image_to_string(self.img, lang=None, config='--psm 6')
		self.file1 = open("myfile.txt", "a")
		self.file1.write(self.data)
		print(self.data)
		

	def render_window(self):		
		cv.imshow("Display window", self.resized)
		self.k = cv.waitKey(0)
		if self.k == ord("s"):
			cv.imwrite("img_kevin_mps.jpg", self.img)
