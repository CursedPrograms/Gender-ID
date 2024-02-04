import os
import subprocess

def main():
    print("Python Project")

    scripts = {
    "1": {
        "name": "Run 'gender-age-predictor-output.py'",
        "description": "This script predicts gender and age.",
        "file_name": "scripts/gender-age-predictor-output.py"
    },
    "2": {
        "name": "Run 'gender-predictor-output.py'",
        "description": "This script predicts gender with image output.",
        "file_name": "scripts/gender-predictor-output.py"
    },
    "3": {
        "name": "Run 'gender-predictor.py'",
        "description": "This script predicts gender.",
        "file_name": "scripts/gender-predictor.py"
    },
    "4": {
        "name": "Run 'gender-age-predictor-feed.py'",
        "description": "This script predicts gender from webcam feed.",
        "file_name": "scripts/gender-age-predictor-feed.py"
    },
    "00": {
        "name": "Run 'Install Dependencies'",
        "description": "Install dependencies",
        "file_name": "scripts/install-dependencies.py"
    },
}

    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nAvailable Scripts:")
        for key, script_info in scripts.items():
            print(f"{key}: {script_info['name']} - {script_info['description']}")
        
        user_choice = input("Enter the number of the script you want to run (or 'q' to quit): ").strip()
        
        if user_choice == 'q':
            break
        
        if user_choice in scripts:
            selected_script = scripts[user_choice]
            script_file_name = selected_script["file_name"]
            script_file_path = os.path.join(current_script_dir, script_file_name)
            
            if os.path.exists(script_file_path):
                try:
                    subprocess.run(["python", script_file_path])
                except Exception as e:
                    print(f"An error occurred while running the script: {e}")
            else:
                print(f"Script file '{script_file_name}' does not exist.")
        else:
            print("Invalid choice. Please select a valid script number.")

if __name__ == "__main__":
    main()
