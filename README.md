# HCL Hackathon

**PROBLEM STATEMENT**

Participants must design and implement a robust retail data pipeline that:

* Ingests high-volume transactional data from multiple sources
* Validates and cleans data using predefined quality rules
* Accurately calculates customer loyalty points
* Performs customer segmentation using behavioral metrics
* Identifies high-value and at-risk customers for targeted engagement

The system should be scalable, auditable, and suitable for real-world retail environments.



The pipeline was intentionally designed to remain database-agnostic, ensuring that infrastructure constraints would not prevent insight generation while maintaining compatibility with relational database systems.

---

## Technology Stack

**Language**
- Python  

**Libraries**
- Pandas  
- NumPy  
- Faker
- Streamlit
- DateTime

**Development Tools**
- VS Code
- Google Colab

---

## Data Pipeline

### Data Ingestion
Raw retail datasets were loaded from CSV files representing multi-store transactional records.

### Data Cleaning
Preprocessing steps included:

- Standardizing column names  
- Handling missing values  
- Removing duplicate records  
- Correcting datatype inconsistencies  
- Resolving schema mismatches  

### Data Normalization
The master dataset was decomposed into structured entities aligned with relational modeling practices:

- Stores  
- Products  
- Customer Details  
- Promotion Details  
- Sales Transactions  
- Line Items  

This approach improves data integrity and prepares the system for downstream database storage.

### Analytics Layer
The processed datasets enabled analysis of key retail metrics, including:

- Customer purchasing behavior  
- Identification of high-value customers  
- Transaction patterns across stores  
- Product performance trends  

---

## Key Outcomes

- Successfully processed high-volume transactional data  
- Built a resilient preprocessing and normalization pipeline  
- Generated meaningful retail intelligence from raw datasets  
- Designed a modular system ready for relational database integration  

---

## Challenges

- Aligning schema across merged datasets  
- Managing inconsistent column formats  
- Handling incomplete and anomalous records  
- Addressing infrastructure limitations during the hackathon  

These challenges were mitigated through flexible pipeline design and robust preprocessing techniques.

---

## Engineering Consideration

The pipeline was deliberately engineered to be independent of database infrastructure so that data processing and insight generation could proceed without operational blockers. This design choice reflects production data engineering principles where resiliency and modularity are prioritized.

---

## Future Improvements

- Deploy the pipeline on cloud infrastructure  
- Integrate with MySQL or PostgreSQL  
- Automate ETL workflows  
- Implement real-time ingestion capabilities  
- Develop dashboards for visualization  
- Enhance data quality monitoring  

---

## Team

- Mahalakshmi
- Rasuri Kaushik
- Sirana Harsha Vardhan
- Jyothi Prasad K

---

## Conclusion

This project demonstrates the design of a structured retail data pipeline capable of transforming raw transactional data into actionable insights. The system emphasizes scalability, modularity, and readiness for enterprise-grade deployment.
