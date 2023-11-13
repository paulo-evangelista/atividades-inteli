# 🚙 Navegação SLAM


https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/d851dd1b-dd0c-4197-876f-9ba39f9f80d6

### O que aconteceu no vídeo?
- iniciamos o mundo de simulação no gazebo
- Iniciamos o primeiro launch que fiz: `map_launch.xml`. Essa é a parte de mapeamento.
- Por ser SLAM, usamos a interface do RVIZ para enviar destinos ao nav2, que vai mapeando enquanto anda.
- O mapa é salvado automaticamente a cada 5 segundos (vide o log que sublinhei no terminal). Quando terminamos de mapear, é só dar um CTRL+C em tudo.
- Agora já podemos usar o outro launch, `nav_launch.xml`
- Esse launch puxa o mapa salvo anteriormente automaticamente e navega pelos pontos pré-definidos no script
- Podemos navegar quantas vezes quisermos sem refazer o mapa ou a pose do robô
  🎇
## ❓ Como executar?
- **Clone o repositório**
- **Entre na pasta** *ros2_ws*: `cd ros2_ws/`
- **Faça a build do pacote:** `colcon build`
- **Instale o pacote** `source install/setup.sh`
- **Execute o script desejado:** `ros2 launch navigation map_launch.xml` ou `ros2 launch navigation nav_launch.xml`
  - Lembre-se: os tópicos do robô já devem estar disponiveis, ou seja, o gazebo já deve estar rodando.
