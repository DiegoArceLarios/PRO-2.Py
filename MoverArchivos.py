import os
import shutil

ReceptorPNG= 'D:/Receptores/ReceptorPNG'
ReceptorLNK= 'D:/Receptores/ReceptorLNK'
ReceptorWEBP= 'D:/Receptores/ReceptorWEBP'
Emisor= 'D:/Descargas generales'

Busqueda1 = os.listdir(Emisor)



for i in Busqueda1:
    n,path= os.path.splitext(i)

    if path == '.png':
        doc = Emisor+'/'+i
        shutil.move(doc,ReceptorPNG)
    if path == '.lnk':
        doc = Emisor+'/'+i
        shutil.move(doc,ReceptorLNK)
    if path == '.webp':
        doc = Emisor+'/'+i
        shutil.move(doc,ReceptorWEBP)
