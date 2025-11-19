#!/bin/bash

# ASL Project Environment Setup Script
# This script sets up a Python 3.11 virtual environment for the project

echo "🔧 Setting up ASL Project environment..."

# Check if Python 3.11 is installed
if ! command -v python3.11 &> /dev/null; then
    echo "❌ Python 3.11 is not installed. Please install it first:"
    echo "   brew install python@3.11"
    exit 1
fi

echo "✅ Found Python 3.11: $(python3.11 --version)"

# Remove old virtual environment if it exists
if [ -d ".venv" ]; then
    echo "🗑️  Removing old virtual environment..."
    rm -rf .venv
fi

# Create new virtual environment with Python 3.11
echo "📦 Creating virtual environment with Python 3.11..."
python3.11 -m venv .venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate this environment in the future, run:"
echo "   source .venv/bin/activate"
echo ""
echo "To run the real-time detection:"
echo "   python scripts/realtime.py"
