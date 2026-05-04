# Albion-Online-Market
Este proyecto utiliza la API de Albion Online para analizar precios de objetos en distintas ciudades y detectar oportunidades de arbitraje.
API: https://www.albion-online-data.com/
Estado del proyecto
El proyecto no está terminado y presenta un problema con la validez de los precios.
La API puede devolver precios antiguos que siguen figurando como activos aunque el objeto ya se haya vendido. Esto provoca que el programa considere ofertas que en realidad ya no existen.
Problema
Intenté solucionarlo usando un sistema que verifica hace cuánto se publicó el precio, pero no es completamente confiable.
Si un objeto tenía un precio hace tiempo y luego vuelve a tener ese mismo precio, la API no permite distinguir entre ambos casos, por lo que el sistema lo interpreta como un precio antiguo.
Conclusión
Esta limitación no puede resolverse completamente desde el código, ya que depende de cómo la API maneja los datos.
