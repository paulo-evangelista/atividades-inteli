import 'package:http/http.dart' as http;
import 'dart:convert';
import '../models/task.dart';

class TaskService {
  final String baseUrl = 'http://10.0.2.2:5000';

  Future<List<Task>> fetchTasks() async {
    print("olá");
    final response = await http.get(Uri.parse('$baseUrl/getAllTasks'));
    if (response.statusCode == 200) {
      List<dynamic> parsed = json.decode(response.body);
      print(parsed);
      parsed.map((e) => print(e));
      return  parsed.map((e) => Task.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load tasks');
    }
  }

  Future<void> addTask(Task task) async {
    await http.post(
      Uri.parse('$baseUrl/createTask'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: json.encode({"title": task.title}),
    );
  }

  Future<void> deleteTask(String id) async {
    await http.delete(
      Uri.parse('$baseUrl/deleteTask/$id')
    );
  }

  Future<void> updateTask(Task task) async {
    await http.put(
      Uri.parse('$baseUrl/updateTask/${task.id}'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: json.encode({"title": task.title}),
    );
  }
}
