
class Task {
  final int id;
  final String title;

  Task({required this.id, required this.title});

  // Método para criar uma instância de Task a partir de um Map (deserialização)
  factory Task.fromJson(Map<String, dynamic> json) {
    print("criando task a partir de json $json -> ${json['id']}");
    final newTask = Task(id: json['id'], title: json['title']);
    print("task criada $newTask");
    return newTask;
  }

  // Método para converter uma instância de Task em um Map (serialização)
  Map<String, dynamic> toJson() {
    return {'id': id, 'title': title};
  }
}
