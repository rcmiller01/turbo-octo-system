import 'package:flutter/material.dart';

void main() => runApp(FitnessCoachApp());

class FitnessCoachApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Fitness Coach Lite',
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  void _showPlaceholder(BuildContext context, String feature) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(feature),
        content: Text('$feature feature is not yet fully implemented.'),
        actions: [TextButton(onPressed: () => Navigator.pop(context), child: Text('OK'))],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AI Fitness Coach Lite')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            ElevatedButton(
              onPressed: () => _showPlaceholder(context, 'Daily Logs'),
              child: Text('View Daily Logs'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _showPlaceholder(context, 'Progress Charts'),
              child: Text('View Progress Charts'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _showPlaceholder(context, 'Daily Summary'),
              child: Text('View Daily Summary'),
            ),
          ],
        ),
      ),
    );
  }
}
