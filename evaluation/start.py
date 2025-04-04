from predictors.predict_llm import predict as predict_llm
from predictors.predict_rag_context import predict as predict_rag_context
from predictors.predict_rag_threshold import predict as predict_rag_threshold

import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import matplotlib.pyplot as plt
import csv


def main():
    with open("test_data.json", "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    llm_predictions = []
    rag_context_predictions = []
    rag_threshold_predictions = []
    true_labels = []

    for case in test_cases:
        code = case["code"]
        true_label = case["is_plagiarism"]
        true_labels.append(true_label)

        llm_predictions.append(predict_llm(code))
        rag_context_predictions.append(predict_rag_context(code))
        rag_threshold_predictions.append(predict_rag_threshold(code))

    llm_precision = precision_score(true_labels, llm_predictions) if any(llm_predictions) else 0
    llm_recall = recall_score(true_labels, llm_predictions)
    llm_f1 = f1_score(true_labels, llm_predictions)
    llm_accuracy = accuracy_score(true_labels, llm_predictions)

    rag_context_precision = precision_score(true_labels, rag_context_predictions)
    rag_context_recall = recall_score(true_labels, rag_context_predictions)
    rag_context_f1 = f1_score(true_labels, rag_context_predictions)
    rag_context_accuracy = accuracy_score(true_labels, rag_context_predictions)

    rag_threshold_precision = precision_score(true_labels, rag_threshold_predictions)
    rag_threshold_recall = recall_score(true_labels, rag_threshold_predictions)
    rag_threshold_f1 = f1_score(true_labels, rag_threshold_predictions)
    rag_threshold_accuracy = accuracy_score(true_labels, rag_threshold_predictions)

    metrics = [
        ['Metric', 'LLM', 'RAG Context', 'RAG Threshold'],
        ['Precision', llm_precision, rag_context_precision, rag_threshold_precision],
        ['Recall', llm_recall, rag_context_recall, rag_threshold_recall],
        ['F1 Score', llm_f1, rag_context_f1, rag_threshold_f1],
        ['Accuracy', llm_accuracy, rag_context_accuracy, rag_threshold_accuracy]
    ]

    with open('evaluation_metrics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(metrics)

    print(metrics)

if __name__ == "__main__":
    main()
