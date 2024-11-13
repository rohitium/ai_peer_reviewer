# AI Peer Reviewer
AI Peer Reviewer is an automated peer-review system developed using Crew AI. This project is designed to facilitate the review process of scientific publications by simulating two distinct roles: Reviewer and Editor. Each role performs specific tasks on an input scientific text, generating a thorough and accurate review as well as detailed editing feedback. The system is particularly aimed at enhancing the peer-review process for complex, biophysics-focused research articles.

## Key files
`config/agents.yaml`: Defines the characteristics and goals for each agent in the review process.

* Reviewer: Acts as a Senior Biophysics Research Scientist who critically evaluates the scientific merit and accuracy of the text.
* Editor: Functions as a Scientific Publication Editor, identifying typos, grammatical errors, and semantic inconsistencies.
`config/tasks.yaml`: Outlines the tasks that each agent will perform.

* Review Task: Conducts a thorough review to identify major concerns and provide expert insight.
* Editing Task: Checks for clerical mistakes, grammatical errors, and logical inconsistencies.

`text.dat`: Contains the input text of a scientific article to be reviewed and edited by the agents.

## Outputs
`reviewer_report.md`: The Reviewer’s output, containing a summary of the article, major concerns, and minor comments.
`editor_report.md`: The Editor’s output, listing detailed points on typos, grammatical issues, and logical inconsistencies.

## Example Reports
In `reviewer_report.md` and `editor_report.md`, you will find example reports based on a biophysics publication discussing protein folding dynamics. Each report offers an overview of the article’s strengths, weaknesses, and areas for improvement, showcasing the Reviewer’s and Editor’s unique expertise.