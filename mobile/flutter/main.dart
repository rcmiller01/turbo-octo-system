import 'package:flutter/material.dart';

void main() => runApp(FitnessCoachApp());

class FitnessCoachApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Fitness Coach Lite',
      home: Scaffold(
        appBar: AppBar(title: Text('Welcome to AI Fitness Coach Lite')),
        body: Center(child: Text('This is the Flutter frontend placeholder.')),
      ),
    );
  }
}
