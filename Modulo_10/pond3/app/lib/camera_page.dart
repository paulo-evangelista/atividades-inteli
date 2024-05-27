import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:http/http.dart' as http;

class CameraPreviewPage extends StatefulWidget {
  const CameraPreviewPage({super.key});

  @override
  _CameraPreviewPageState createState() => _CameraPreviewPageState();
}

class _CameraPreviewPageState extends State<CameraPreviewPage> {
  late CameraController _controller;
  Future<void>? _initializeControllerFuture;
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _initializeCamera();
  }

  Future<void> _initializeCamera() async {
    try {
      final cameras = await availableCameras();
      final firstCamera = cameras.first;

      _controller = CameraController(
        firstCamera,
        ResolutionPreset.high,
      );

      _initializeControllerFuture = _controller.initialize();
      setState(() {});
    } catch (e) {
      print(e);
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _takePictureAndProcess() async {
    try {
      await _initializeControllerFuture;

      final image = await _controller.takePicture();
      setState(() {
        _isLoading = true;
      });

      final imageBytes = await image.readAsBytes();
      String base64Image = base64Encode(imageBytes);
      var response = await http.post(
        Uri.parse('http://192.168.135.12:5001/image'),
        headers: {"Content-Type": "application/json"},
        body: json.encode({'image': base64Image}),
      );

      setState(() {
        _isLoading = false;
      });

      if (response.statusCode == 200) {
        var decodedResponse = json.decode(response.body);
        String processedImageBase64 = decodedResponse['image'];
        _showImageModal(context, processedImageBase64);
      } else {
        print('Failed to process image');
      }
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
      print(e);
    }
  }

  void _showImageModal(BuildContext context, String imageData) {
    showDialog(
      context: context,
      barrierDismissible: true, // Permite fechar o diálogo tocando fora dele
      builder: (BuildContext context) {
        return Dialog(
          insetPadding: EdgeInsets.all(30),
          child: Transform.rotate(
              angle:
                  90 * 3.1415926535897932 / 180, // Converte graus para radianos

              child: Transform.scale(
                scale: 1.5,
                child:
                    Image.memory(base64Decode(imageData), fit: BoxFit.contain),
              )),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Camera'),
      ),
      body: Column(
        children: <Widget>[
          Expanded(
            child: _initializeControllerFuture == null
                ? const Center(child: CircularProgressIndicator())
                : FutureBuilder<void>(
                    future: _initializeControllerFuture,
                    builder: (context, snapshot) {
                      if (snapshot.connectionState == ConnectionState.done) {
                        return CameraPreview(_controller);
                      } else if (snapshot.hasError) {
                        return Center(child: Text('Error: ${snapshot.error}'));
                      } else {
                        return const Center(child: CircularProgressIndicator());
                      }
                    },
                  ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: _isLoading
                ? CircularProgressIndicator()
                : ElevatedButton(
                    onPressed: _takePictureAndProcess,
                    child: const Text('Tirar foto e processar'),
                  ),
          ),
        ],
      ),
    );
  }
}
