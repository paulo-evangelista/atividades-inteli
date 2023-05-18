# Código em python para fazer um desenho no turtleSim do ROS2

## Vídeo-demonstração -> https://photos.app.goo.gl/3YXXFDVcFeN5XPNa6

O código controla tartarugas no simulador para fazer um desenho.

Criei a classe "Turtle" que é resposável por controlar uma tartaruga.

Cada instância dessa classe criará um nó ROS que responsável por controlar uma única tartaruga.

A classe tem funções para mover a tartaruga, mudar a cor de seu rastro e mata-lá.

Ao instanciar, a classe recebe apenas o nome da tartaruga desejada. O nó ROS criado será homônimo.

Depois disso, apenas utilizamos dessa clase para criar e mover várias tartarugas e fazer nosso desenho :)
```
Para mudar de cor, criar e matar tartarugas, estamos usando clients para consumir serviços disponibilizados pelo turtlesim.
    acredito que foram usados serviços em vez de tópicos pois são ações mais "imediatas", extraordinárias.
    
Já para mover a tartaruga, estamos publicando em um tópico.
    como a movimentação é uma ação rotineira, que acontece várias vezes em sequência, faz sentido utilizar um tópico.
```
