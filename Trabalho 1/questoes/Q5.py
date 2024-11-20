# 5)
# Uma imagem pode ser pensada como um sinal com duas variáveis independentes
# que, ao invés de ser o tempo, são as dimensões (vertical e horizontal), ou seja, x[nV , nH].
# Utilizando a imagem (image.jpeg) disponibilizada no SIGAA, faça:

from PIL import Image
import matplotlib.pyplot as plt

imagem = Image.open("Trabalho 1\material\image.jpg")

# a) x[−nV , nH]
imagem_A = imagem.transpose(Image.FLIP_TOP_BOTTOM)

#b) x[nV, -nH]
imagem_B = imagem.transpose(Image.FLIP_LEFT_RIGHT)
plt.figure(figsize=(10, 5))

# c) x[nV - n0, nH]
n0 = 50  
imagem_C = Image.new("RGB", imagem.size)
imagem_C.paste(imagem, (0, n0))

# d) x[nV, nH - n1]
n1 = 50  
imagem_D = Image.new("RGB", imagem.size)
imagem_D.paste(imagem, (n1, 0))

# e) x[nV - n2, nH - n3]
n2, n3 = 50, 50 
imagem_E = Image.new("RGB", imagem.size)
imagem_E.paste(imagem, (n3, n2))  

# x[-nV, nH]
plt.subplot(2, 3, 1)
plt.title("x[-nV, nH])")
plt.imshow(imagem_A)
plt.axis("off")

# x[nV, -nH]
plt.subplot(2, 3, 2)
plt.title("x[nV, -nH])")
plt.imshow(imagem_B)
plt.axis("off")

# x[nV - n0, nH]
plt.subplot(2, 3, 3)
plt.title(f"x[nV - {n0}, nH]")
plt.imshow(imagem_C)
plt.axis("off")

# x[nV, nH - n1]
plt.subplot(2, 3, 4)
plt.title(f"x[nV, nH - {n1}]")
plt.imshow(imagem_D)
plt.axis("off")

# x[nV - n2, nH - n3]
plt.subplot(2, 3, 5)
plt.title(f"x[nV - {n2}, nH - {n3}]")
plt.imshow(imagem_E)
plt.axis("off")

plt.tight_layout()
plt.show()
