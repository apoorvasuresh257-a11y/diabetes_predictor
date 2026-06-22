#!/usr/bin/env python3
"""
Setup script for running the Diabetes Assessment App locally
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        return False
    print("✅ Python version:", sys.version.split()[0])
    return True

def install_packages():
    """Install required packages"""
    packages = [
        'streamlit',
        'pandas', 
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn', 
        'plotly',
        'joblib'
    ]
    
    print("\n📦 Installing packages...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    return True

def create_streamlit_config():
    """Create .streamlit/config.toml file"""
    os.makedirs('.streamlit', exist_ok=True)
    
    config_content = """[server]
headless = true
address = "0.0.0.0"
port = 8501

[theme]
base = "light"
"""
    
    with open('.streamlit/config.toml', 'w') as f:
        f.write(config_content)
    print("✅ Streamlit config created")

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'diabetes_model.py', 
        'medicine_recommendations.py',
        'educational_content.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing files:", missing_files)
        return False
    
    print("✅ All required files present")
    return True

def run_app():
    """Run the Streamlit app"""
    print("\n🚀 Starting the app...")
    print("The app will open in your browser automatically.")
    print("If it doesn't open, go to: http://localhost:8501")
    print("\n--- Press Ctrl+C to stop the app ---\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 App stopped!")

def main():
    print("🩺 Diabetes Assessment App - Local Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check required files
    if not check_required_files():
        print("\n❌ Please make sure all files are in the current directory")
        return
    
    # Create config
    create_streamlit_config()
    
    # Install packages
    if not install_packages():
        print("\n❌ Package installation failed")
        return
    
    print("\n✅ Setup complete!")
    
    # Ask user if they want to run the app
    response = input("\nRun the app now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        run_app()
    else:
        print("\nTo run later, use: streamlit run app.py")

if __name__ == "__main__":
    main()