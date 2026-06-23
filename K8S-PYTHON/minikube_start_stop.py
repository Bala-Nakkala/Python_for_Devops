#!/usr/bin/env python3

import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

choice = input("Enter start or stop: ").lower()

if choice == "start":
    run_command(["minikube", "start"])
elif choice == "stop":
    run_command(["minikube", "stop"])
else:
    print("Invalid choice")