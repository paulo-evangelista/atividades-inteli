import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../blocs/task_bloc.dart';
import '../blocs/task_event.dart';
import '../blocs/task_state.dart';
import '../models/task.dart';

class TasksScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black54,
      appBar: AppBar(
        backgroundColor: Colors.white24,
        title: const DefaultTextStyle(
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 30),
            child: Text("Your TO-DOs"),
          ),
        actions: [
          IconButton(
            icon: Icon(Icons.add, color: Colors.white),
            onPressed: () => _showAddEditTaskDialog(context),
          ),
        ],
      ),
      body: BlocBuilder<TaskBloc, TaskState>(
        builder: (context, state) {
          if (state is TasksLoadInProgress) {
            BlocProvider.of<TaskBloc>(context).add(LoadTasks());
            return Center(child: CircularProgressIndicator());
          } else if (state is TasksLoadSuccess) {
            if (state.tasks.isEmpty) {
              return Center(
                  child: Text('🗿', style: 
                    TextStyle(fontSize: 40, color: Colors.grey),
                  ));
            }
            return ListView.builder(
              itemCount: state.tasks.length,
              itemBuilder: (context, index) {
                return _taskItem(context, state.tasks[index]);
              },
            );
          } else {
            return Center(child: Text('-'));
          }
        },
      ),
    );
  }

  Widget _taskItem(BuildContext context, Task task) {
    return ListTile(
      tileColor: Colors.white24,
      title: Text(task.title, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
      subtitle: Text(task.id.toString(), style: TextStyle(color: Colors.white12),),
      trailing: Row(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          IconButton(
            icon: Icon(Icons.edit, color: Colors.white,),
            onPressed: () => _showAddEditTaskDialog(context, task: task),
          ),
          IconButton(
            icon: Icon(Icons.delete, color: Colors.white),
            onPressed: () => _deleteTask(context, task.id.toString()),
          ),
        ],
      ),
    );
  }

  void _deleteTask(BuildContext context, String taskId) {
    BlocProvider.of<TaskBloc>(context).add(DeleteTask(taskId));
  }

  void _showAddEditTaskDialog(BuildContext context, {Task? task}) {
    final _titleController = TextEditingController(text: task?.title ?? 'sem titulo');
    final _descriptionController =
        TextEditingController(text: task?.id.toString() ?? '');

    showDialog(
      context: context,
      builder: (dialogContext) => AlertDialog(
        title: Text(task == null ? 'Adicionar Tarefa' : 'Editar Tarefa'),
        content: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: _titleController,
                decoration: InputDecoration(labelText: 'Tarefa'),
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            child: Text('Cancelar'),
            onPressed: () => Navigator.of(dialogContext).pop(),
          ),
          TextButton(
            child: Text('Salvar'),
            onPressed: () {
              final title = _titleController.text;

              if (task == null) {
                BlocProvider.of<TaskBloc>(context).add(AddTask(Task(id: 1, title: title)));
              } else {
                BlocProvider.of<TaskBloc>(context).add(UpdateTask(Task(id: task.id, title: title)));
              }

              Navigator.of(dialogContext).pop();
            },
          ),
        ],
      ),
    );
  }
}
