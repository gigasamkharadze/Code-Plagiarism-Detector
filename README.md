# Code Plagiarism Detection System

## A Modern Approach to Identifying Code Similarities Using AI, LLMs, and Vector Search

With the increasing availability of open-source code repositories and
collaborative software development platforms, code plagiarism detection
has become a significant challenge in academia and the software industry.
Developers and students often reuse existing code, sometimes without
proper attribution, leading to ethical and legal concerns. Identifying similar
or copied code across repositories requires an efficient and scalable system
capable of recognizing semantic similarities rather than just textual matches.
Traditional plagiarism detection methods, such as direct string comparison,
fail to capture cases where the code has been modified while retaining its
original logic.

This project aims to develop a code plagiarism detection system that can
analyze code snippets and compare them against existing repositories to
determine whether they are plagiarized. The system will employ
vector-based similarity search using embeddings generated from
pre-trained models. By leveraging machine learning techniques, the project
will index and store code representations in a vector database, enabling fast
and accurate similarity searches. The system will integrate a
retrieval-augmented generation (RAG) approach, combining vector-based
retrieval with large language models (LLMs) to provide precise plagiarism
detection results. The final implementation will feature a FastAPI-based
service that accepts code snippets, searches for similar content, and returns
a definitive answer on whether plagiarism has occurred.

## System Components

### 1. Indexing

The indexing service is responsible for processing and storing code snippets in a vector database. This involves:
- Parsing code repositories to extract individual code snippets.
- Generating embeddings for each code snippet using a pre-trained model.
- Storing the embeddings in a vector database for efficient similarity search.

Repositories are indexed **locally** that means we need to clone the repositories first.
The step can be completed by the following steps:
1. Update `config.py` with the path to the repositories.
2. Run `clone.py` to clone the repositories. *(you can run the script with no fear
  of overwriting the existing repositories, as it will only clone the ones that are not
  already cloned - checks the dir)*
3. Run `main.py` to retrieve the code snippets from the repositories and generate embeddings.
4. The `main.py` script will also store the embeddings in the `Pinecone` vector database.

The latest step is kind of a **preprocessing** step being the most baffling one. 
I approached it by manually providing:
- The list of file extensions to be read. (e.g. `[".py", ".java"]`) I need to think
  about a more generic approach to this. But, at the moment, seems kinda logical to me, as deciding what to parse cannot be generalized and needs to be specifically defined for the problem.
- The list of regex patterns removing predefined parts of the code. Mainly, I remove comments, docstrings, and
  some other parts of the code that are not relevant for the plagiarism detection.

### 2. Embedding Service

The embedding service generates vector representations (embeddings) of code snippets.
The service is built using a pre-trained model that is taken from Hugging Face - `Salesforce/codet5p-220m`

We do not need to train the model from scratch, as it is already trained on a large corpus of code.

As a service, it is very simple and straightforward.
Send post request to the `/generate/` endpoint with the code snippet in the body.
And, it will return the embedding of the code snippet.

### 3. API

This is the main service that interacts with users. Users send a post request
to the `/check` endpoint with a code snippet. For example:
```json
{
  "code": "def hello_world():\n    print('Hello, World!')"
}
```
1. The code snippet is to be processed.
2. The embedding service generates an embedding for the code snippet.
3. The API service retrieves the most similar code snippets from the vector database
   using the embedding generated in the indexing step.
4. The OpenAI API + context retrieved from the vector database is used to determine
   whether the code snippet is plagiarized or not.

### 4. Evaluation

The evaluation service assesses the performance of the plagiarism detection system.

| System Type | Description                                                                          |
|-------------|--------------------------------------------------------------------------------------|
| Only RAG    | Uses threshold on similar vectors retrieved from the database to predict plagiarism. |
| Only LLM    | Directly asks LLM whether the code snippet provided in the prompt is plagiarised     |
| Our system  | Use main api described above to predict plagiarism                                   |

