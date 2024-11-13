#!/usr/bin/env python
import sys
import warnings

from ai_peer_reviewer.crew import AIPeerReviewer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def fetch_paper_text():
    """
    Fetch text from text.dat file.
    """
    try:
        with open("text.dat", "r") as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file 'text.dat' was not found.")

def run():
    """
    Run the crew.
    """
    paper_text = fetch_paper_text()
    inputs = {
        'research_article': paper_text
    }
    AIPeerReviewer().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    paper_text = fetch_paper_text()
    inputs = {
        "research_article": paper_text
    }
    try:
        AIPeerReviewer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AIPeerReviewer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    paper_text = fetch_paper_text()
    inputs = {
        "research_article": paper_text
    }
    try:
        AIPeerReviewer().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
