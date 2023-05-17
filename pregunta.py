"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    doc = 'clusters_report.txt'
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    encabezados = []
    indices = []
    listoencab = 0
    numlinea = 0
    with open(doc, mode='r') as text_file:
        texto = text_file.readlines()
        for linea in texto:
            linea = linea.replace("\n","")
            if linea.strip()!="":
                if listoencab == 0: 
                    if all(c == '-' for c in linea):
                        for i in range(0, len(encabezados)):
                            encabezados[i] = encabezados[i].replace(' ','_').lower()
                        listoencab = 1
                    else: 
                        if encabezados==[]:
                            contador = 0
                            error = 0
                            nuevalinea = linea.strip()
                            while error == 0: 
                                try:
                                    nuevalinea = nuevalinea.strip()
                                    encabezados.append(nuevalinea[:nuevalinea.index("  ")])
                                    indices.append(linea.index(encabezados[contador]))
                                    nuevalinea = nuevalinea[nuevalinea.index("  "):].strip()
                                    contador+=1
                                except:
                                    nuevalinea = nuevalinea.strip()
                                    encabezados.append(nuevalinea)
                                    indices.append(linea.index(encabezados[contador]))
                                    error = 1
                        else:
                            for i in range(0,len(encabezados)-1):
                                try: 
                                    if linea[indices[i]:indices[i+1]].strip()!='':
                                        encabezados[i]=encabezados[i]+" "+linea[indices[i]:indices[i+1]].strip()
                                except:""
                            try: 
                                encabezados[len(encabezados)-1] = encabezados[len(encabezados)-1]+" "+linea[indices[len(encabezados-1)]:].strip
                            except:""
                else: 
                    nuevalinea=linea.strip()
                    if nuevalinea[0].isdigit():
                        col1.append(nuevalinea[:nuevalinea.index("  ")].strip())
                        nuevalinea = nuevalinea[nuevalinea.index(col1[-1])+len(col1[-1]):].strip()
                        col2.append(nuevalinea[:nuevalinea.index("  ")].strip())
                        nuevalinea = nuevalinea[nuevalinea.index(col2[-1])+len(col2[-1]):].strip()
                        col3.append(nuevalinea[:nuevalinea.index("  ")].strip())
                        nuevalinea = nuevalinea[nuevalinea.index(col3[-1])+len(col3[-1]):].strip()
                        col4.append(nuevalinea)
                    else: 
                        nuevalinea=nuevalinea.strip()
                        col4[-1] = col4[-1]+" "+nuevalinea
            numlinea+=1

    for i in range(0,len(col4)):
        while '  ' in col4[i]:
            col4[i] = col4[i].replace('  ', ' ')
        if col4[i][-1]=='.':
            col4[i]=col4[i][:-1]
    col3 = [i.replace(" %", "").replace(",", ".") for i in col3]
    contenido = [col1, col2, col3, col4]
    for i in range(0, len(contenido)): 
        try: 
            contenido[i] = [float(dato) for dato in contenido[i]]
        except:""
    diccionario = {clave: valor for clave, valor in zip(encabezados, contenido)}
    data = pd.DataFrame(diccionario)
    return data

print(ingest_data().principales_palabras_clave.to_list()[9]
        == "micro grid, multi-agent systems, distributed energy resource, batteries energy storage system, dc micro grid, pitch-control, droop control, hybrid ac/dc microgrid, voltage regulation, superconducting magnetic energy storage, distributed-control"
    )


                    

