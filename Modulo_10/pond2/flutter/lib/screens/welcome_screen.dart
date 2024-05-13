import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../blocs/task_bloc.dart';
import 'tasks_screen.dart';

class WelcomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black54,
      appBar: AppBar(
          backgroundColor: Colors.white24,
          title: const DefaultTextStyle(
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 30),
            child: Text("TO-DO List"),
          )),
      body: Center(
        child: ElevatedButton(
  style: ButtonStyle(
    backgroundColor: MaterialStateProperty.all<Color>(Colors.blue),
    minimumSize: MaterialStateProperty.all<Size>(Size(200, 50)),
  ),
  onPressed: () {
    final taskBloc = BlocProvider.of<TaskBloc>(context, listen: false);
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => BlocProvider.value(
          value: taskBloc,
          child: TasksScreen(),
        ),
      ),
    );
  },
  child: DefaultTextStyle(
    style: TextStyle(fontSize: 20, color: Colors.white), // Set the text size to 20 and color to white
    child: Text("Go to Tasks"),
  ),
),
      ),
    );
  }
}
