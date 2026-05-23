# fraudulent-transaction-prediction-project

## project Overview
NovaPay is a rapidly growing digital money transfer company operating in a highly dynamic financial environment where transaction security is critical. As digital transactions increase globally, fraudulent activities such as identity theft, unauthorized transactions, and account takeovers have become more sophisticated and difficult to detect using traditional static rule-based systems.

This project focuses on developing a Machine Learning-based Fraud Detection System capable of identifying fraudulent transactions in real time while minimizing false positives. The proposed solution aims to improve fraud detection accuracy, enhance customer trust, and support operational scalability as NovaPay continues to expand globally.

The project leverages data analytics, machine learning, and model explainability techniques to build a fraud detection pipeline that is scalable, adaptive, and suitable for deployment within real-time transaction systems.

## Business Challenges

NovaPay currently faces several operational and security challenges associated with its existing fraud detection process:

1. Increasing Fraud Sophistication

Fraudsters continuously evolve their tactics, making static rule-based systems less effective in identifying new and complex fraud patterns.

2. High False Positives

The existing system incorrectly flags many legitimate transactions as fraudulent, causing:

Poor customer experience
Delayed transactions
Increased customer dissatisfaction
Higher manual review costs

3. Global Scalability Issues

As NovaPay expands internationally, transaction volumes continue to grow rapidly. The current fraud detection framework struggles to scale efficiently with increasing real-time transaction demands.

4. Lack of Adaptability

Traditional rule-based systems require constant manual updates and are unable to adapt quickly to emerging fraud behaviors and transaction anomalies.

5. Regulatory and Compliance Requirements

Financial institutions require transparent and explainable fraud detection systems. NovaPay needs a solution capable of providing interpretable fraud predictions to satisfy compliance and regulatory standards.

6 Need for Real-Time Detection

Because NovaPay operates in a fast-paced digital payment environment, fraud detection decisions must occur instantly without slowing down transaction processing.


## Target Variable
The target variable for this project is: is_fraud. This variable represents whether a transaction is fraudulent or legitimate. The target variable is encoded in 1 and 0, where 0 represent legitimate transaction and 1 represent fraudulent transaction.
