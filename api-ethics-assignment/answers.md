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
  Fix: Add timeout and sleep()

