# 🌐 Laboratorio 3 - Segunda: Algoritmos de Enrutamiento 

## 📚 1. Antecedentes
Con el objetivo de enviar mensajes a través de routers, es esencial conocer el destino final y reenviar el mensaje al vecino que ofrezca la mejor ruta hacia ese destino. Esta información vital se guarda en las tablas de enrutamiento. Sin embargo, debido al dinamismo esperado de Internet, estas tablas deben ser capaces de actualizarse y adaptarse a cambios en la infraestructura. Los algoritmos que actualizan estas tablas son conocidos como algoritmos de enrutamiento.

## 🎯 2. Objetivos
- 🌍 Conocer los algoritmos de enrutamiento utilizados en las implementaciones actuales de Internet.
- 🧠 Comprender cómo funcionan las tablas de enrutamiento.
- 💻 Implementar los algoritmos de enrutamiento y probarlos.

## 💡 3. Desarrollo
Los algoritmos de enrutamiento operan en nodos interconectados. Cada nodo conoce únicamente a sus vecinos. Esta información inicial se proporciona para cada nodo. A partir de esto, se simula manualmente el envío y recepción de mensajes entre nodos para construir sus tablas de enrutamiento. En esta fase, nos centraremos en los algoritmos de ruteo "offline", y cada integrante del grupo deberá implementar al menos un algoritmo.

Los algoritmos a implementar son:
- **Dijkstra**: Requiere topología (nodos, aristas).
- **Flooding**: Generalmente no requiere inputs, pero puede usar la topología si es necesario.
- **Flooding**: Unicamente depende de las distancias de costo entre dos nodos en la red.

### Instalaciones

Para poder ejecutar cada una de las carpetas correspondientes es necesario tener dentro del sistema maven, esto debido a que en ciertas implementaciones se opto por utilizar la biblioteca smack y en otras ocasiones la biblioteca slixmpp, que era java y python respectivamente. La instalacion de maven se realiza con la descarga de la pagina oficial agregandolo a la ruta del path.

Mientras que para la instalacion que slixmpp simplemente era necesario el uso de pip para obtener la libreria.

El uso tambien es bastante practico, simplemente con tener clonado el repositorio y ejecutar los programas principales correspondientes iniciaba la iteracion.

Siempre para cada terminal se solicita que nodo se utiliza y la cuenta que se asocia, asimismo que a su vez la interconectividad varia dependiendo de la implementacion.



### 📦 Paquetes
Los paquetes a enviar tendrán una estructura tipo JSON como la siguiente:
```json
{
  "type" : "message|echo|info",
  "headers" : ["from" : "foo", "to" : "bar", "hop_count" : 3, ...],
  "payload" : "loremipsum{contenido aquí}"
}
```

El elemento "type" indica el tipo de paquete. Los encabezados (headers) mínimos a usar y definir son: from (nodo origen), to (nodo destino) y hop_count (conteo de saltos). Se pueden definir más encabezados para facilitar la comunicación.



### 📖 Referencias

Enrutamiento en Internet
https://es.wikipedia.org/wiki/Encaminamiento

Algoritmo de Dijkstra:
https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra

Flooding:
https://es.wikipedia.org/wiki/Inundaci%C3%B3n_de_red#:~:text=La%20inundaci%C3%B3n%20(en%20ingl%C3%A9s%3A%20flooding,la%20que%20se%20ha%20recibido.

Distance Vector: 
Smith, B. R., Murthy, S., & Garcia-Luna-Aceves, J. J. (1997, February). Securing distance-vector routing protocols. In Proceedings of SNDSS'97: Internet Society 1997 Symposium on Network and Distributed System Security (pp. 85-92). IEEE.