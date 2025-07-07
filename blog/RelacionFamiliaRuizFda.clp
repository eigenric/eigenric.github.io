

;;;; HECHOS GENERALES DEL SISTEMA ;;;;;
;;;;(seran v?lidos para todas las ejecuciones del sistema ;;;;

; Listado de personas de la familia en cuestion introducidas con la propiedad unaria de hombre o mujer

(deffacts personas
   (hombre Juan) ; "Juan es un hombre"
   (hombre ManuelRuiz)
   (hombre ManuelVidal)
   (hombre Manolo)
   (hombre Yeray)
   (hombre Daniel)
   (hombre ManoloRuiz)
   (hombre ManoloVidal)
   (hombre Dani)
   (hombre Ricardo)
   (hombre Pedro)
   (hombre Andre)
   (hombre Manuel)
   (hombre Paco)
   (mujer Esther)         ; Esther es una mujer
   (mujer Maite)
   (mujer Lourdes)
   (mujer Lidia)
   (mujer Noelia)
   (mujer Raquel)
   (mujer Lidia)
   (mujer Teresa) 
   (mujer Marina)
   (mujer Ada)
   (mujer Rosa)
)

;;;;; Plantilla t?pica de Relaciones binarias, ajustada a relaciones de parentesco restringiendo los valores de tipo de relacion a estas. Se usa para registrar "El <sujeto> es <tipo de relacion> de <objeto>", por ejemplo "Juan es TIO de Julia" 

(deftemplate Relacion 
  (slot tipo (type SYMBOL) (allowed-symbols HIJO PADRE ABUELO NIETO HERMANO ESPOSO PRIMO TIO SOBRINO  CUNIADO YERNO SUEGRO))
  (slot sujeto)
  (slot objeto))

;;;;; Datos de la relacion HIJO y ESPOSO en mi familia que es suficiente para el problema, pues el resto se deduce de estas

(deffacts relaciones
   (Relacion (tipo HIJO) (sujeto Ricardo) (objeto ManuelRuiz)) ; "Luis es HIJO de Antonio
   (Relacion (tipo HIJO) (sujeto ManoloRuiz) (objeto ManuelRuiz))
   (Relacion (tipo HIJO) (sujeto Marina) (objeto ManuelRuiz))
   (Relacion (tipo HIJO) (sujeto Daniel) (objeto ManuelVidal))
   (Relacion (tipo HIJO) (sujeto ManoloVidal) (objeto ManuelVidal))
   (Relacion (tipo HIJO) (sujeto Raquel) (objeto ManuelVidal))
   (Relacion (tipo HIJO) (sujeto Noelia) (objeto Esther))
   (Relacion (tipo HIJO) (sujeto Ada) (objeto Juan))
   (Relacion (tipo HIJO) (sujeto Yeray) (objeto Juan))
   (Relacion (tipo HIJO) (sujeto Dani) (objeto ManoloRuiz))
   (Relacion (tipo HIJO) (sujeto Andre) (objeto Pedro))
   (Relacion (tipo HIJO) (sujeto Lidia) (objeto Teresa))
   (Relacion (tipo HIJO) (sujeto Esther) (objeto Teresa))
   (Relacion (tipo HIJO) (sujeto Maite) (objeto Teresa))
   (Relacion (tipo HIJO) (sujeto Lourdes) (objeto Teresa))
   (Relacion (tipo HIJO) (sujeto Juan) (objeto Manuel))
   (Relacion (tipo HIJO) (sujeto ManuelRuiz) (objeto Manuel))
   (Relacion (tipo ESPOSO) (sujeto Juan) (objeto Lourdes)) 
   (Relacion (tipo ESPOSO) (sujeto ManuelRuiz) (objeto Maite)) 
   (Relacion (tipo ESPOSO) (sujeto ManuelVidal) (objeto Lidia))
   (Relacion (tipo ESPOSO) (sujeto ManoloRuiz) (objeto Rosa))
   (Relacion (tipo ESPOSO) (sujeto Pedro) (objeto Raquel))
   (Relacion (tipo ESPOSO) (sujeto Paco) (objeto Teresa)))

;;;;;;; Cada relacion tiene una relacion dual que se produce al cambiar entre si objeto y sujeto. Por ejejmplo, Si x es HIJO de y, y es PADRE de x". Para poder deducirlo con una sola regla metemos esa informacion como hechos con la etiqueta dual, "Dual de HIJO PADRE", y asi con todas las relaciones consideradas
 
(deffacts duales
(dual HIJO PADRE) (dual ABUELO NIETO) (dual HERMANO HERMANO) (dual ESPOSO ESPOSO) (dual PRIMO PRIMO) (dual TIO SOBRINO) (dual CUNIADO CUNIADO) (dual YERNO SUEGRO))

;;;;;; Para deducir las reglas que se aplican son de composicion, del tipo "el HERMANO del PADRE es un TIO". Por comodidad, en lugar de crear una regla por cada posible composici?n, metemos como hechos la relacion que se obtiene por composicion. Solo metemos unas cuantas composiciones que sean suficientes para deducir cualquier cosa

(deffacts compuestos
(comp HIJO HIJO NIETO) (comp PADRE PADRE ABUELO) (comp PADRE ABUELO BISABUELO)(comp ESPOSO PADRE PADRE)(comp HERMANO PADRE TIO) (comp HERMANO ESPOSO CUNIADO) (comp ESPOSO HIJO YERNO) (comp ESPOSO HERMANO CUNIADO) (comp HIJO PADRE HERMANO) (comp ESPOSO CUNIADO CUNIADO) (comp ESPOSO TIO TIO)  (comp HIJO TIO PRIMO)  ) 


;;;;;; Para que cuando digamos por pantalla el parentesco lo espresemos correctamente, y puesto que el nombre que hemos puesto a cada relacion es el caso masculino, vamos a meter como hechos como se diaria esa relacion en femenino mediante la etiqueta femenino

(deffacts femenino
(femenino HIJO HIJA) (femenino PADRE MADRE) (femenino ABUELO ABUELA) (femenino BISABUELO BISABUELA) (femenino NIETO NIETA) (femenino HERMANO HERMANA) (femenino ESPOSO ESPOSA) (femenino PRIMO PRIMA) (femenino TIO TIA) (femenino SOBRINO SOBRINA) (femenino CUNIADO CUNIADA) (femenino YERNO NUERA) (femenino SUEGRO SUEGRA)) 


;;;;; REGLAS DEL SISTEMA ;;;;;

;;;; La dualidad es simetrica: si r es dual de t, t es dual de r. Por eso solo metimos como hecho la dualidad en un sentidos, pues en el otro lo podiamos deducir con esta regla

(defrule autodualidad
  (declare (salience 5000))
      (dual ?r ?t)
=> 
   (assert (dual ?t ?r)))


;;;; Si  x es R de y, entonces y es dualdeR de x

(defrule dualidad
   (declare (salience 5000))
   (Relacion (tipo ?r) (sujeto ?x) (objeto ?y))
   (dual ?r ?t)
=> 
   (assert (Relacion (tipo ?t) (sujeto ?y) (objeto ?x))))


;;;; Si  y es R de x, y x es T de z entonces y es RoT de z
;;;; a?adimos que z e y sean distintos para evitar que uno resulte hermano de si mismo y cosas asi.

(defrule composicion
    (declare (salience 5000))
   (Relacion (tipo ?r) (sujeto ?y) (objeto ?x))
   (Relacion (tipo ?t) (sujeto ?x) (objeto ?z))
   (comp ?r ?t ?u)
   (test (neq ?y ?z))
=> 
   (assert (Relacion (tipo ?u) (sujeto ?y) (objeto ?z))))

;;;;; Como puede deducir que tu hermano es tu cu?ado al ser el esposo de tu cu?ada, eliminamos los cu?ados que sean hermanos

(defrule limpiacuniados
    (declare (salience 5000))
    (Relacion (tipo HERMANO) (sujeto ?x) (objeto ?y))
    ?f <- (Relacion (tipo CUNIADO) (sujeto ?x) (objeto ?y))
=>
	(retract ?f) )

;;;;; Solicitamos el nombre de la primera persona sobre el que se desea informacion y guardamos y a?adimos ese hecho 

;;;;; Hacemos que nos diga por pantalla la relacion entre las persona introducidas. Como la forma de expresarlo dependera del sexo, usamos dos reglas, una para cada sexo

(defrule imprimirMensaje
  (declare (salience 1100))
=>
   (printout t "Las personas posibles son: " crlf)
)

(defrule hombresPosibles
(declare (salience 1000))   
    (hombre ?x)
=>
   (printout t ?x crlf)
)

(defrule mujeresPosibles
(declare (salience 900))
   (mujer ?y)
=>
   (printout t ?y crlf)
)

(defrule pregunta
(declare (salience 800)) 
=>
   (printout t "Nombre primera persona: " crlf)
   (assert (primerapersona (read)))
   (printout t "Las relaciones posibles son: " crlf)
)
   
   ;;;;; Solicitamos el nombre de la segunda persona 

(defrule relacionesPosibles
(primerapersona ?x)
(Relacion (tipo ?r) (sujeto ?y) (objeto ?x))
=>
   (printout t ?r crlf)
   (assert (primerapersona ?x))
)

(defrule pregunta2
(primerapersona ?primero)
=>
   (printout t "Nombre de la relaci�n: " crlf)
   (assert (relacion (read)))
)

(defrule segundomasculino
   (primerapersona ?x)		
   (relacion ?r)
   (Relacion (tipo ?r) (sujeto ?y) (objeto ?x))
   (hombre ?y)
 =>
   (printout t ?y " es " ?r " de " ?x crlf)
)

(defrule segundofemenino
   (primerapersona ?x)		
   (relacion ?r)
   (Relacion (tipo ?r) (sujeto ?y) (objeto ?x))
   (mujer ?y)
   (femenino ?r ?t)
 =>
   (printout t ?y " es " ?t " de " ?x crlf)
 )

