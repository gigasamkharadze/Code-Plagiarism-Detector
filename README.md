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