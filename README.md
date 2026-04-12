# UDB LAB WORKS

This repository contains MongoDB and scripting lab exercises.

## Contents

### 1. Insert Document in MongoDB
- Use database: `use myDatabase`
- Insert one document using `insertOne()`
- Insert multiple documents using `insertMany()`

### 2. Delete Document in MongoDB
- Delete a document using `deleteOne()`
- Delete using `_id` with `ObjectId`

### 3. Python EXIF Metadata Organizer
- Reads image files from a directory
- Extracts EXIF metadata (device model, user, GPS)
- Categorizes images based on:
  - Device brand
  - User name
  - GPS availability
  - Device category (Android / Apple / No Metadata)
- Organizes images into structured folders

### 4. API to MongoDB Automation Script
- Node.js script
- Hits an API every 1000ms
- Extracts date and time
- Inserts response into MongoDB collection

### 5. Update MongoDB Documents
- Update specific document using `updateOne()`
- Update latest inserted document using sort option

---

## Technologies Used
- MongoDB (mongosh)
- Python
- Node.js
- REST API

---

## Author
Debasmita Bose, B.Tech CSE (3rd yr)
