# **Juego de Cartas 21 (Blackjack)** 

## Participantes del Proyecto

   - Luis Miguel Viuche Madroñero (20212020082)
   - Daniel Alejandro Chave Bustos (20212020109)
   - Dilan Stive Arboleda Zambrano (20212020105)

 ## Descripción del Proyecto

El objetivo del juego es acercarse lo más posible a 21 sin pasarse, compitiendo contra la casa. El jugador puede pedir cartas (hit), quedarse con su mano actual (stand) o hacer un *split* si tiene dos cartas del mismo valor.

- **Enfoque funcional:** El programa no depende de variables globales o estados mutables. Las funciones reciben y retornan todos los valores necesarios, garantizando una ejecución más clara y modular.
- **Uso de listas de comprensión:** Para mejorar la legibilidad y la eficiencia, la mayor parte de la lógica se basa en listas de comprensión. Esto facilita operaciones como la creación de barajas, el cálculo de puntajes y la determinación de los ganadores.
- **Juego simple y directo:** El jugador y el "dealer" (la banca) reciben cartas, y el objetivo es que el jugador se acerque lo más posible a 21 puntos sin sobrepasar esa cantidad.

## Cómo Jugar
1. **Iniciar el Juego**: Al ejecutar el script, el programa mostrará un mensaje de bienvenida con las instrucciones básicas del juego.
2. **Reparto Inicial**: Se repartirán dos cartas al jugador y dos cartas a la casa.
3. **Opciones del Jugador**:
   - Si el jugador tiene dos cartas del mismo valor, se le preguntará si desea hacer un *split*.
   - El jugador puede pedir cartas adicionales (hit) o quedarse con su mano actual (stand).
4. **Turno de la Casa**: La casa pedirá cartas hasta que el valor de su mano sea de al menos 17.
5. **Comparación Final**: Se comparan las manos del jugador y la casa para determinar el ganador.

## Reglas del Blackjack
1. **Valor de las Cartas**:
   - Cartas numéricas (2-10): Su valor es el número que muestran.
   - Cartas con figuras (J, Q, K): Todas valen 10 puntos.
   - Ases (A): Pueden valer 1 u 11 puntos, dependiendo de lo que sea más favorable para la mano del jugador.

2. **Objetivo del Juego**: Lograr una mano con un valor total de 21 puntos o lo más cercano posible sin pasarse. Si el jugador o la casa se pasan de 21, pierden automáticamente.

3. ***Split***:
   - Si las dos cartas iniciales del jugador tienen el mismo valor (por ejemplo, dos 8s), el jugador puede optar por hacer un *split*, dividiendo su mano en dos manos separadas.
   - Cada mano se juega de manera independiente, siguiendo las reglas normales del juego.

4. **Obligación de la casa**:
   - La casa está obligada a pedir una carta adicional si el valor total de su mano es menor a 17.
   - Una vez que el crupier alcanza 17 o más, deja de pedir cartas.
   
4. **Ganar o Perder**:
   - Si el valor de la mano del jugador es mayor que el de la casa sin pasarse de 21, el jugador gana.
   - Si el valor de la mano de la casa es mayor que el del jugador sin pasarse de 21, la casa gana.
   - Si ambas manos tienen el mismo valor, es un empate.
  
## Requisitos
- Python 3.x
- No se requieren bibliotecas externas, ya que el proyecto solo utiliza bibliotecas estándar de Python (`random` para mezclar el mazo).

## Instrucciones de Ejecución
1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Descarga el archivo `blackjack.py`.
3. Ejecuta el archivo con el siguiente comando:

   ```bash
   python blackjack.py





