# 🤖 AI-Summarizer

AI-powered content summarizer with **asynchronous processing**, built in **Python**, designed to run locally with Docker and scale seamlessly on **AWS**.

---

## 🚀 Overview

The **AI-Summarizer** is a backend service that receives large text content, processes it asynchronously, and returns a summarized version using AI models.

The architecture is designed to be:
- ✅ Scalable
- ✅ Cloud-ready (AWS)
- ✅ Asynchronous by default
- ✅ Easy to run locally with Docker

---

## 🧠 Architecture (High Level)

```text
Client
  |
  v
FastAPI (API)
  |
  v
SQS (Queue)
  |
  v
Worker (Async Processor)
  |
  v
DynamoDB (Results Storage)
