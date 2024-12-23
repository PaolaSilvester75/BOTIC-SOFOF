class Libro:
    def __init__(self, autor, titulo, ann_de_publicacion=None):
        self.autor = autor
        self.titulo = titulo
        self.ann_de_publicacion = ann_de_publicacion

libro_1 = Libro(autor="Dan Brown", titulo="Inferno")
libro_2 = Libro(autor="Dan Brown", titulo="El Código Da Vinci", ann_de_publicacion=2003)

print(libro_1.__dict__)
print(libro_2.__dict__)
