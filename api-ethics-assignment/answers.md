# Task 1 — Classify and Handle PII Fields
**1. full_name**
  Type: Direct PII
  Action: Drop 
  Why: Directly identifies a person 
  
**2. email**
  Type: Direct PII
  Action: Mask or Drop
  Why: Highly sensitive and uniquely identifies individuals. Mask (e.g., g***@mail.com) if partial visibility is needed; otherwise drop
  
**3. date_of_birth**
  Type: Indirect PII
  Action: Mask
  Why: Can identify individuals when combined with other fields
  
**4. zip_code**
  Type: Indirect PII
  Action: Mask
  Why: Narrow geographic data can help re-identify someone
  
**5. job_title**
  Type: Indirect PII
  Action: Keep
  Why: Usually safe alone
  
**6. diagnosis_notes**
  Type: Sensitive Personal Data (Special Category PII)
  Action: Mask / Pseudonymize
  Why: Contains health information (highly sensitive)

# Task 2 — Audit the API Script for Ethical Compliance

**Violation 1: Hardcoded API Key (TOS Violation)**
  Problem: Exposes sensitive credentials in code and can be leaked via GitHub
  Fix: Use Environment Variables

**Violation 2: No Rate Limit Handling**
  Problem: No timeout
  Fix: Add timeout and time.sleep(1)


```
import os
import time
import requests

# Load API key securely from environment variable
API_URL = "https://healthstats-api.example.com/records"
API_KEY = os.getenv("API_KEY")

records = []

for page in range(1, 101):
    try:
        response = requests.get(
            API_URL,
            params={"page": page, "key": API_KEY},
            timeout=5
        )
        data = response.json()
        records.extend(data["results"])

        # Respect API rate limits
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        break

save_to_database(records)
```

