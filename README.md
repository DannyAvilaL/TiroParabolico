# Tiro Parabólico
Repositorio de la SemanaTec para el programa del Tiro Parabólico  
Iniciamos con el código base de Tiro Parabólico  
* Tap para crear el proyectil de acuerdo a la posición del mouse al dar click. 
* Revisar si los objetos están dentro de la pantalla
* Dibujar a la pelota y los proyectiles 
* Movimiento de la pelota y proyectiles. Checa colisiones entre el proyectil y los targets y cuando un target llegue al borde izquierdo, se detiene todo.
## Agregamos:
### Daniela Avila Luna: 
Incremento de la velocidad del proyectil y los targets.

```python
target_speed = 6
ball_speed = vector(300, 300)

 if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + ball_speed.x) / 30
        speed.y = (y + ball_speed.y) / 25
        
 for target in targets:  # velocidad de los targets
        target.x -= target_speed
```

### Liam Garay Monroy: 
Hacer que el juego nunca termine, reposicionando los balones del lado derecho de la pantalla 

```python
for target in targets:
        if not inside(target):
            target.x = 200
```