# CentraComm

## Description
CentraComm is a centralized communication tool designed to enhance project execution by resolving technical queries and facilitating efficient communication across cross-functional teams. By leveraging CentraComm, teams can quickly find answers to technical questions, access relevant project documentation, and identify the right individuals with experience in similar tasks. This leads to improved efficiency and better project outcomes.

## Problem Statement
In technical projects, challenges often arise related to concepts, workflows, or technologies. CentraComm addresses these issues by providing answers to technical queries and identifying experts within the organization who have tackled similar problems. This promotes smoother communication and better understanding across teams, accelerating project execution.

## Project Concept
CentraComm utilizes a RAG (Retrieval-Augmented Generation) based chatbot to store and retrieve unstructured data such as project reports, research documents, and training manuals. While the ideal implementation supports both PDFs and text files, this demonstration focuses on text files to illustrate the concept.

For PoC on PDF processing: [reference link](https://github.com/AKA-SSH/Text-Summarizer/blob/main/README.md)

## Project Workflow
1. **Data Extraction**: Extract raw text from documents.
2. **Tokenization**: Convert the text into tokens for processing.
3. **Vector Embedding**: Transform tokens into vector embeddings for efficient storage and retrieval.
4. **Storing**: Store the vector embeddings in a database.
5. **Retrieval**: Fetch relevant information based on user queries.
6. **Generation**: Generate responses to queries using the retrieved information.

## How to Run
1. Prepare a set of text files containing project documentation.
2. Set the path to the text files in the configuration.
3. Navigate to the root directory of the project.
4. Set the `PYTHONPATH` to the current directory: `set PYTHONPATH=%cd%`
5. Run the main script: `python src\main.py`

## License
This project is licensed under the MIT License.

## Contact
For further assistance or queries, please contact the project maintainers or consult the CentraComm documentation.

---

CentraComm streamlines communication and boosts efficiency by connecting team members with the information and expertise they need, enabling faster and more informed decision-making.
