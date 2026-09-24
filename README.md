# NYC Taxi Data Engineering ETL Pipeline with Apache Airflow & PostgreSQL
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-3.3.0-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=Docker&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=Pandas&logoColor=white)
Simple ETL pipeline orchestration on the New York City (NYC) Yellow Taxi trip records into a PostgreSQL database. The pipeline is orchestrated using **Apache Airflow (TaskFlow API)** inside **Docker**, implementing **Airflow XCom** for inter-task metadata communication and task dependency passing.
