# Parliamentary Early-Warning Agent

### Restoring Newsroom Oversight Through Open, Human-Centred AI

---

## 📌 Abstract

This project is an open-source AI-powered newsroom early-warning system designed to transform fragmented, unstructured parliamentary data into timely, actionable editorial insight.

It does **not replace journalists**.
It restores their capacity to monitor legislation.

South Africa’s parliamentary data ecosystem is scattered across platforms such as:

* Parliament of South Africa (Parliament.gov.za)
* PMG
* Hansard archives
* Departmental portals and releases

Audio and video are uploaded without transcripts.
Transcripts arrive as flattened, non-machine-readable PDFs.
Critical bills move forward with little public visibility.

The stories exist — but journalists lack the time, tools, and staffing to surface them.

This project builds an automated **scraper → transcript → analysis → insight** pipeline that continuously monitors parliamentary activity and flags potential story leads in real time.

---

## The Problem

South Africa’s legislative data landscape is structurally broken for journalism:

* Fragmented archives across multiple government portals
* Delayed or missing transcripts for proceedings
* Non-machine-readable PDFs blocking analysis
* No unified tracking of bill changes over time
* No early-warning system for policy shifts or oversight failures

The result: **democratic opacity**.

Bills affecting water access, procurement, media regulation, public health, education, and social grants move through committees with minimal scrutiny.

The issue is not the absence of information — it is its inaccessibility.

---

## Project Goals

### 1️Continuous Data Acquisition

The agent will automatically:

* Scrape new documents and recordings from:

  * Parliament of South Africa
  * PMG
  * Hansard archives
* Monitor departmental portals
* Detect newly uploaded PDFs, videos, and statements

---

### Multilingual Transcription

Using multilingual ASR (Automatic Speech Recognition), the system will transcribe parliamentary recordings in:

* English
* isiZulu
* isiXhosa
* Afrikaans

This restores searchability and analysis capacity across languages commonly used in South African parliamentary proceedings.

---

### 3️NLP Processing & Entity Extraction

The pipeline will:

* Extract:

  * MPs and ministers
  * Departments
  * Bill titles
  * Event names
  * Committees
  * Constituencies
  * Topics
* Track bill versions and detect textual changes
* Cluster content by topic, bill, and region

---

### Anomaly & Signal Detection

The system will flag potential story leads such as:

* Sudden shifts in policy language
* Procurement or tender discussions
* Repeated absences of key ministers or MPs
* Underreported bills affecting daily life
* Recurring phrases tied to controversial reforms

This does **not** publish stories.
It surfaces **leads** for human investigation.

---

### Newsroom Delivery

Insights will be delivered via:

* Secure web dashboard
* Slack integration for newsroom alerts
* Bill-tracking module with change summaries
* Structured summaries of debates and committee discussions

Journalists decide what matters.
The agent ensures they don’t miss it.

---

## Project Architecture

```
Scraper Layer
    ↓
Document Normalisation
    ↓
Multilingual Transcription (ASR)
    ↓
NLP Processing (NER + Topic Modelling + Clustering)
    ↓
Anomaly Detection Engine
    ↓
Dashboard / Slack Alerts
```

---

## Pilot Phase

The initial pilot will focus on **five high-impact bills**, demonstrating:

* End-to-end scraper-to-insight pipeline
* Bill change tracking
* Real-time alerts for committee discussions
* Open technical documentation

---

## Expected Deliverables

* Working automated scraping system
* Multilingual transcription pipeline
* Entity extraction + clustering engine
* Anomaly detection module
* Secure monitoring dashboard
* Slack newsroom integration
* Open-source documentation

---

## Why This Matters

Democracy depends on oversight.
Oversight depends on visibility.
Visibility depends on tools.

This project restores the newsroom’s ability to:

* See patterns across debates
* Detect quiet policy shifts
* Track legislative language changes
* Surface underreported reforms
* Identify procurement red flags

It helps journalists **see the signal in the legislative noise**.

---

## Principles

* Human-centred (journalists remain decision-makers)
* Open-source
* Transparent methodology
* Multilingual by design
* Built for public-interest reporting

---

## Long-Term Vision

* Expansion beyond national Parliament to provincial legislatures
* Public-facing bill transparency portal
* Civil society access tools
* Cross-country adaptation

---

