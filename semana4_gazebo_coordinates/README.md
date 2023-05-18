# Pacote ROS em python que move um TurtleBot3 Burguer dentro do Gazebo para coordenada(s)
## Vídeo demonstração -> https://photos.app.goo.gl/KdwpTX2bpVphMhWX9

Nesse exercício, decidi desenvolver uma solução mais programática e menos matemática.
É o jeito mais trabalhoso, não tão preciso nem otimizado, porém exercita mais a lógica de programação.

## RACIOCÍNIO:
Pensei que fosse mais fácil mover-se em apenas um coordenada por vez.
O robo se mover no eixo X até o ponto desejado, e só então mover-se no Y para então alcançar a coordenada (X,Y).

Para tanto, descrevi as seguintes condições:


### Quando for movimentar-se no eixo X:
- se o X desejado é MENOR que o atual, temos que seguir no sentido NEGATIVO de X e tentar aproximar de 180° (horizontal para a esquerda)
- se o X desejado é MAIOR que o atual , tem que seguir no sentido POSITIVO de X e tentar aproximar de 0° (horizontal para a direita)

### Quando for movimentar-se no eixo Y:
- se o Y desejado é MENOR que o atual, temos que seguir no sentido NEGATIVO de Y e tentar aproximar de -90° (vertical para baixo)
- se o Y desejado é MAIOR que o atual , tem que seguir no sentido POSITIVO de Y e tentar aproximar de 90° (vertical para cima)

### O que significa o "tentar aproximar" acima?
    É impossível, com um comando, girar o robo para um grau especifíco.
    Logo, em vez disso, tento fazer com que ele fique o mais proximo do angulo desejado possivel.
    Ex:
        Digamos que estamos tentando seguir no sentido positivo de Y sem alterar nossa ordenada X, ou seja, exatos 90°.
        Como não é possível dizer "ande para cima exatamente em 90°", vamos dizer o seguinte:
        "ande para cima. Caso o angulo passe de 90°, vire um pouco para a direita. Caso o angulo esteja abaixo de 90°, vire um pouco para a esquerda."
        Assim, mesmo que não subamos exatamente no angulo desejado, o movimento do robô assume forma de uma espécie de função oscilatória, que, na média, nos deixa no ângulo desejado.

IMPORTANTE -> O angulo do robô NÃO VAI DE 0 A 360. Ele segue um esquema esquisito, de -180 a 180. Oeste é 180, leste é 0, sul é -90 e norte é 90.
