# **Actividad Práctica: Patrones de Diseño** 
**Estudiante: Fermini Mara**.  
**Cátedra: Programacion Avanzada.**  
**Profesor: Luparello Diego.**  
**Carrera: Tecnicatura Universitaria en Programación.**  
**Universidad Nacional de Almirante Brown.**  
___
### Ejercicio 1:  
*Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos.*  
Las críticas principales a los patrones de diseño giran en torno a su uso indebido. Se los cuestiona por promover la sobreingeniería y por resolver deficiencias del lenguaje de programación. También se critica que en muchas oportunidades se aplican sin una necesidad real.  
Se considera que los patrones de diseño son fallas de diseño en los lenguajes de programación, en muchas oportunidades el programador se ve obligado a implementar manualmente estructuras complejas para resolver problemas comunes.  
El uso desmedido de patrones es el problema más común, es frecuente que el programador intente encajar patrones en todos lados, incluso en donde sería suficiente con una función, violando principios fundamentales como *KISS*.  
Algunos patrones quedaron obsoletos frente a las nuevas buenas prácticas. Cada patrón introduce capas de abstracción, que implica llamadas a métodos y búsquedas en memoria, lo que genera menor rendimiento.  
Por todos estos motivos se considera que el verdadero arte de la arquitectura de software no radica en saber cómo implementar un patrón, sino en saber cuándo no es necesario usarlo.  
Ejemplos:  
* El Patrón Singleton garantiza la existencia de una única instancia de una clase a nivel global. Su principal crítica es que introduce un estado global oculto dentro de la aplicación.  
* El Patrón Strategy se utiliza para alternar diferentes algoritmos en tiempo de ejecución, generando la creación de una interfaz y de una clase independiente por cada variante del algorítmo.  
* El Patrón Abstract Factory provee una interfaz para generar familias de objetos relacionados sin especificar sus clases concretas. Es un patrón propenso a desencadenar el antipatrón de diseño conocido como Golden Hammer.  
___
### Ejercicio 3:  
*Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño.*  
**Planificación de una clase:**  
Diseñar el programa de contenidos de un curso requiere de reahcerlo constantemente frente a la cancelación de clases por diversos motivos. Mediante el uso de Template Method, se crea una plantilla con pasos fijos, inicio, desarrollo y evaluación del contenido, el esqueleto se mantiene y solo cambia contenido específico evitando reorganizar todo el año.  
**Cocinar para toda la semana.**  
Cocinar todos los días no es una opción, quita tiempo de descanso y genera una mala alimentación. Se cocina varias porciones en un mismo día, la unica acción que resta es calentar la comida el día que sea necesario, empaquetando en esta acción el trabajo de toda la semana (Command).  
**Recordar claves.**  
La parte más dificil de las mil sesiones que iniciamos por día, para no olvidar las contraseñas se utiliza el patrón Factory, en lugar de memorizar veinte claves se memoriza una regla de producción. Al registrarse en un sitio nuevo se aplica la regla mental y se crea la nueva clave.  
___

