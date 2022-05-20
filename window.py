import cv2 as cv
import pytesseract

img = cv.imread(cv.samples.findFile("img_kevin_mps.jpg"))
if img is None:
    sys.exit("Could not read the image.")

# variáveis para o redimensionamento da image
scale_percent = 18 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

# variáveis para as coordenadas dos retângulos (x,y)
start_point_nome = (363,121)
end_point_nome = (430,132)

start_point_solucao = (18,245)
end_point_solucao = (520,418)

start_point_tempo = (87,465)
end_point_tempo = (107,475)

start_point_servico = (352,16)
end_point_servico = (405,30)

# cor (R,G,B)
AZUL = (255,0,0)

# expessura 
thickness = 2

# instanciação dos retângulos
nome = cv.rectangle(resized, start_point_nome, end_point_nome, AZUL, thickness)
solucao = cv.rectangle(resized, start_point_solucao, end_point_solucao, AZUL, thickness)
tempo = cv.rectangle(resized, start_point_tempo, end_point_tempo, AZUL, thickness)
servico = cv.rectangle(resized, start_point_servico, end_point_servico, AZUL, thickness)

retangulos = [nome,solucao,tempo,servico]

# renderizar imagem
cv.imshow("Display window", resized)

print(resized.shape)

# if de execução da janela
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("img_kevin_mps.jpg", img)

text = str(pytesseract.image_to_string(resized, config='--psm 6'))
print(text)