# UDB LAB WORKS

A collection of database and scripting lab exercises built around MongoDB, Python, Kafka, and automation workflows.

## Repository Overview

This project contains:
- MongoDB CRUD examples and lab notes
- A Kafka producer that generates sample IoT sensor data
- A Kafka consumer that ingests sensor events into MongoDB
- Python tooling and Docker Compose configuration for local development

## Project Contents

### MongoDB Labs
- Insert documents using `insertOne()` and `insertMany()`
- Delete documents using `deleteOne()` and object `_id`
- Update documents using `updateOne()` and query sorting
- Other MongoDB scripting exercises and examples

### Kafka + MongoDB Integration
- `producer.py`: publishes simulated IoT sensor messages to Kafka topic `iot_sensor_data`
- `consumer.py`: consumes Kafka messages and inserts them into MongoDB collection `iot_db.sensor_data`

### Additional Notes
- A Python EXIF metadata organizer is part of the lab exercises (described in repository notes)
- A Node.js API automation script was also included as a lab exercise

## Prerequisites

- Python 3.11+ (or compatible)
- Docker Desktop with Compose support
- A local Python virtual environment (optional but recommended)
- `pip` for installing dependencies

## Setup

1. Create and activate a virtual environment (if not already present):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install Python dependencies:
   ```bash
   .venv\Scripts\python -m pip install -r requirements.txt
   ```
3. Start Docker services:
   ```bash
   docker compose up -d
   ```

## Running the Kafka + MongoDB Demo

### Start the Kafka producer

```bash
.venv\Scripts\python producer.py
```

### Start the Kafka consumer

```bash
.venv\Scripts\python consumer.py
```

### Expected behavior

- The producer sends sample sensor payloads every second to Kafka
- The consumer reads messages from topic `iot_sensor_data`
- Each message is inserted into MongoDB at `mongodb://localhost:27017`

## Docker Compose Services

- `broker`: Apache Kafka broker available at `localhost:9092`
- `mongodb`: MongoDB server available at `localhost:27017`

## Dependency Summary

- `kafka-python==2.3.1`
- `pymongo==4.16.0`

## Useful Commands

- Stop Docker Compose:
  ```bash
  docker compose down
  ```
- View Docker Compose logs:
  ```bash
  docker compose logs -f
  ```

## File Summary

- `producer.py`: sends JSON sensor data to Kafka
- `consumer.py`: reads Kafka records and writes to MongoDB
- `docker-compose.yml`: launches Kafka and MongoDB services
- `requirements.txt`: Python dependencies
- `UDB.txt`: additional notes or lab references

## Author
Debasmita Bose, B.Tech CSE (3rd yr)
