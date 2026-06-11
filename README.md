Developer: Syed Munsif
Id: 2312347
Course: Introduction to DevOps
Project: A production-ready containerised microservice application that demonstrates 
mastery of the complete DevOps toolchain taught in the course. A live application running on a cloud server (AWS) that automatically tests and deploys itself every time you push code to GitHub. 
This is exactly how professional DevOps engineers work at companies around the world.
Tools Used:
Linux
Git & GitHub
Docker
Docker Compose
GitHub Actions  —  CI pipeline (lint + test), CD pipeline (auto-deploy to EC2 on push)
AWS EC2
PostgreSQL
Application architecture and requirements:
A FastAPI web application with a PostgreSQL database backend. 
The app exposes four REST API endpoints and persists data in a PostgreSQL container. 
Both services run via Docker Compose. 
The entire system deploys automatically to AWS EC2 whenever you push code to the main branch.
