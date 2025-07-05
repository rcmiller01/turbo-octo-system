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
        content: Text('$feature will be available soon.'),
        actions: [TextButton(onPressed: () => Navigator.pop(context), child: Text('OK'))],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AI Fitness Coach Lite')),
      body: ListView(
        padding: const EdgeInsets.all(24.0),
        children: [
          _buildButton(context, 'Start Workout'),
          _buildButton(context, 'View Daily Summary'),
          _buildButton(context, 'Progress Charts'),
          _buildButton(context, 'Daily Logs'),
          _buildButton(context, 'Export Data'),
          _buildButton(context, 'Settings'),
        ],
      ),
    );
  }

  Widget _buildButton(BuildContext context, String label) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12.0),
      child: ElevatedButton(
        onPressed: () => _showPlaceholder(context, label),
        child: Text(label, style: TextStyle(fontSize: 18)),
      ),
    );
  }
}
