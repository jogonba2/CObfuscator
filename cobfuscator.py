#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from random import randint

non_start_text           = "(?!(?:\/\/|\"|\'|\/\*\*))"
identifier               = "[a-zA-Z][\w|_]*"
declarator               = "\*?"+identifier
storage_class_specifiers = "auto|register|static|extern|typedef"
type_qualifiers          = "const|volatile"
type_specifiers          = "void|char|short|int|long|float|double|signed|unsigned|struct|union" # Anyadir soporte enum (identifier) #
declaration_specifiers   = "(?:"+storage_class_specifiers+")?\s*(?:"+type_qualifiers+")?\s*(?:"+type_specifiers+")\s+"
function_definition      = non_start_text+declaration_specifiers + "("+declarator +")\s*\("
start_preprocessor       = "(?#)"
preprocessor_defines     = "define|ifdef|ifndef|undef"
preprocessor             = non_start_text+start_preprocessor+"\s*(?:"+preprocessor_defines+")\s*"+"("+declarator+")\s*\(?"
variable_definition      = "Build it..."

def getSource(fileName):
	""" Obtiene el código fuente del fichero.
	Devuelve el código fuente con las declaraciones cambiadas.
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	with open(fileName,"r") as fd: yield fd.read()
	fd.close()

def saveSource(source,fileName):
	""" Almacena en disco el código fuente modificado.
	No devuelve ningún valor
	Parámetros:
	source   -- código fuente
	fileName -- nombre del fichero donde almacenar el código fuente
	Excepciones:
	...
	"""
	with open(fileName,"w") as fd: fd.write(source)
	fd.close()
	
def replaceFunctions(source,functions):
	""" Reemplazar funciones haciéndolas ilegibles.
	Devuelve el codigo fuente con las funciones cambiadas
	Parámetros:
	source    -- código fuente
	functions -- conjunto de funciones del código fuente
	Excepciones:
	...
	Sentencia:
	storage_class_identifier type_qualifier type_specifier
	"""
	for function in functions: source = source.replace(function,functions[function])
	return source

def searchFunctions(source,lengthValidIdentifiers):
	""" Buscar las funciones y almacenarlas en una tabla hash.
	Devuelve una tabla hash con todas las funciones del código como clave y su token aleatorio como valor
	Parámetros:
	source                 -- código fuente
	lengthValidIdentifiers -- longitud de los identificadores aleatorios
	Excepciones:
	1) La expresion regular no encuentra ocurrencias, match.group(0) = None (AttributeError)
	2) Se sobrepasa el indice del grupo (IndexError)
	...
	"""
	try:
		functions = {}  # Nombre función : aleatorio #
		#print non_start_text+function_definition
		for match in re.finditer(function_definition,source):
			funcToken = match.group(1)
			if funcToken!="main":
				if funcToken not in functions: functions[funcToken] = generateValidIdentifier(lengthValidIdentifiers)
	except AttributeError as ae:
		print "AttributeError"
	except IndexError as ie:
		print "Index error"
	finally:
		return functions
	
	
def replaceDeclarations(source,declarations):
	""" Reemplazar variables|funciones definidas con llamadas al preprocesador.
	Devuelve el código fuente con las declaraciones cambiadas
	Parámetros:
	source       -- código fuente
	declarations -- conjunto de declaraciones a reemplazar
	Excepciones:
	...
	"""
	for declaration in declarations: source = source.replace(declaration,declarations[declaration])
	return source

def searchDeclarations(source,lengthValidIdentifiers):
	""" Buscar las declaraciones
	Devuelve una tabla hash con todas las declaraciones del código como clave y su token aleatorio como valor.
	Parámetros:
	source                 -- código fuente
	lengthValidIdentifiers -- longitud de los identificadores aleatorios
	Excepciones:
	1) La expresion regular no encuentra ocurrencias, match.group(0) = None (AttributeError)
	2) Se sobrepasa el indice del grupo (IndexError)
	...
	"""
	try:
		declarations = {}  # Nombre declaracion : aleatorio #
		print preprocessor
		for match in re.finditer(preprocessor,source):
			decToken = match.group(1)
			print decToken
			if decToken not in declarations: declarations[decToken] = generateValidIdentifier(lengthValidIdentifiers)
	except AttributeError as ae:
		print "AttributeError"
	except IndexError as ie:
		print "Index error"
	finally:
		return declarations
	
def replaceVariables(source):
	""" Cambia el nombre de todas las variables haciéndolas ilegibles.
	Devuelve el código fuente con las variables cambiadas
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass

def searchVariables(source):
	""" Buscar las variables y almacenarlas en una tabla hash.
	Devuelve una tabla hash con todas las variablesdel código como clave y su token aleatorio como valor
	Parámetros:
	source                 -- código fuente
	lengthValidIdentifiers -- longitud de los identificadores aleatorios
	Excepciones:
	1) La expresion regular no encuentra ocurrencias, match.group(0) = None (AttributeError)
	2) Se sobrepasa el indice del grupo (IndexError)
	...
	"""
	pass
	
def addJunk(source):
	""" Añade código basura con instrucciones que alteren el contenido binario sin alterar el resultado final.
	Devuelve el código fuente con basura añadida
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass

def replaceNumberCodification(source):
	""" Cambia los valores numéricos con codificaciones alternativas (binario,hexadecimal,octar,funciones (+,-,...) ,...).
	Devuelve el código fuente con la codificación de todos los números cambiada
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass

def permuteSource(source):
	""" Permuta grupos de instrucciones sin dependencias de flujo ni antidependencias.
	Devuelve el código fuente con grupos de instrucciones con el orden cambiado aleatoriamente
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass

def addJumps(source):
	""" Cambia el flujo de ejecución añadiendo saltos sin alterar el resultado final.
	Devuelve el código fuente con saltos añadidos aleatoriamente
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass

def transposeSource(source):
	""" Transponer el código manteniendo el flujo de ejecución.
	Devuelve el código fuente transpuesto aleatoriamente
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
def replaceInstructions(source):
	""" Reemplaza instrucciones por otras equivalentes.
	Devuelve el código fuente con las instrucciones reemplazadas aleatoriamente
	Parámetros:
	source -- código fuente
	Excepciones:
	...
	"""
	pass
	
def generateValidIdentifier(length): 
	""" Generar un identificador valido para las sustituciones.
	Devuelve un identificador aleatorio x / |x| = length, iniciado por un caracter alfabético seguido de length-1 caracteres alfanuméricos
	Parámetros:
	length -- longitud del identificador
	Excepciones:
	...
	"""
	return "".join([chr(randint(65,90)) if randint(0,2) >= 1 else chr(randint(97,122))] + [chr(randint(65,90)) if randint(0,2)==2 else chr(randint(97,122)) if randint(0,2)==1 else chr(randint(48,57)) for x in xrange(length)])
	
if __name__ == "__main__":
	source = getSource("bmphide.c").next()
	#print replaceFunctions(source,searchFunctions(source,10))
	#print searchDeclarations(source,10)
	#print replaceDeclarations(source,searchDeclarations(source,10))
	#print help(generateValidIdentifier)
