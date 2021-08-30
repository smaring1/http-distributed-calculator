# Reto Laboratorio 2 - Tópicos Especiales en Telemática - 2021-2 - Universidad EAFIT - http-distributed-calculator

##Conceptos Fundamentales:

Dos o más procesos / aplicaciones en Internet se pueden comunicar de diferentes maneras
para implementar un servicio distribuido. Uno de los mecanismos de comunicación más
utilizados es la comunicación Web Cliente/Servidor fundamentada en un protocolo de
comunicaciones HTTP y un lenguaje de marcación HTML, típicamente representado por un
Cliente (browser) y un Servidor (web server). Este modelo, nacido en sus orígenes de la Web
(web 1.0 o estática), ha evolucionado altamente hasta nuestros días, al punto que esta
arquitectura (web), protocolos (HTTP, websokets), lenguajes (HTML, JSON, JS, etc), son hoy
en día el fundamento de muchos sistemas distribuidos modernos (desde Facebook, hasta
netflix, quizás pasando por muchos otros).

Cuando 2 o más aplicaciones se comunican vía HTTP, aprovechan muchas de las
características del protocolo, para sustentar no solo la comunicación, sino que será el inicio
del estilo de comunicación basado en RPC (llamadas a procedimientos remotos) y primeras
nociones de un API (ej: API REST).

##Especificaciones:

1. Reutilice la misma aplicación desarrollada en el Lab1 y rediséñela e impleméntela
utilizando el protocolo de aplicación HTTP (ej: calculadora distribuida, chat, crud, etc)

2. Utilizar una librería HTTP en cualquier lenguaje de programación de su preferencia
(recomendado Python)

3. Defina, diseñe e implemente el mecanismo de comunicación (mensajes y codificación)
que requiera para implementar dicha aplicación.

4. Realice inicialmente todos los supuestos que requiera respecto a tipo de sistema: C/S o
P2P, tipo de arquitectura, y aplique algunos de los conceptos fundamentales de los
sistemas distribuidos que se verán en esta Lectura: Introducción a Sistemas Distribuidos.

5. Impleméntela en AWS Educate, para probar el sistema al menos instancie 3 máquinas
EC2.


### Fecha de entrega
* 27 de agosto 2021

## Integrantes 
-Alejandro Fernandez Restrepo
-Miguel Fernando Ramos
-Simón Marin Giraldo

#Solución

Para solucionar este reto creamos una calculadora basica usando python y haciendo uso de las maquinas virtuales y los sockets, tambien haciendo uso de la http de python paara lograr cumplir con los requerimientos del laboratorio.

Para el desarrollo de este reto hicimos uso de una arquitectura **Cliente-Servidor**

![Cliente-Servidor](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/1200px-Client-server-model.svg.png)

Este es un modelo de diseño de software para **sistemas distribuidos** en el cual las tareas se reparten entre los proveedores de reursos o servicios (servidores) y los demandantes (clientes). Un cliente realiza peticiones a otro programa ubicado en el **servidor**, quien le da la respuesta.

Este concepto es aplicable a programas que se ejecutan en una sola computadora, pero es más provechoso en un sistema operativo **multiusuario** distribuido a través de una red de computadoras.

En la arquitectura **cliente-servidor**, por cada **cliente** que llega al **servidor**, se crea un **hilo**.

#Instancias

Server

![image](https://user-images.githubusercontent.com/45807912/131283371-8b18654d-6658-4a45-98c3-801da128b2b3.png)

Cliente 0

![image](https://user-images.githubusercontent.com/45807912/131283396-bb18cebd-68f7-4172-bd67-45b8fb5e8a87.png)

cliente 1 

![image](https://user-images.githubusercontent.com/45807912/131283416-40e96cd6-7033-445e-8525-319f713e23f9.png)

#Funcionamiento

Nuestro programa es una calculadora, en la cual desde los **clientes** se realiza una operación, la cual es solucionada en el **servidor**, que devuelve una respuesta.

Al tener un **hilo** por cada cliente, nos aseguramos de que a cada usuario le llegue su respuesta correspondiente.

Para ejecutar primero tenemos que ejecutar el servidor con:

```bash
python server0.py
```
Despues de esto podemos ejecutar cualquiera de lso dos clientes con:

```bash
python client0.py
```
ó
```bash
python client1.py
```

Despues de esto podemos ingresar la operacion matematica en el cliente , el cual le mandara los datos al servidor a traves de http gracias a la libreria http.client de python.

![image](https://user-images.githubusercontent.com/45807912/131283652-f094ab45-0a60-4f5d-b171-61cafcf71990.png)

A lo cual el servidor retornara la respuesta al cliente que lo alla pedido.
