#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_agent.crew import ContentAgentCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'brand_name': 'funny and engaging',
        'target_audience': 'founders and entrepreneurs',
        'topic': 'Self Improvement'
    }
    ContentAgentCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Self Improvement"
    }
    try:
        ContentAgentCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ContentAgentCrew().crew().replay(task_id=sys.argv[0])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) > 1:
        if sys.argv[1] == "train":
            if len(sys.argv) > 2:
                train()
            else:
                print("Please provide the number of iterations for training.")
        elif sys.argv[1] == "replay":
            if len(sys.argv) > 2:
                replay()
            else:
                print("Please provide the task ID for replay.")
    else:
        # If no arguments, run the default run() function
        run()