# AWS EC2 Start/Stop Automation Using Lambda & EventBridge

This project automates the **Start** and **Stop** of an EC2 instance using  
AWS **Lambda + EventBridge Scheduler**.

---

## 📁 Files in This Repository
- `start_lambda.py` → Automatically **starts** your EC2 instance  
- `stop_lambda.py` → Automatically **stops** your EC2 instance  
- `ec2-policy.json` → IAM policy for the Lambda execution role  

---

# 🏗️ Architecture Diagram

```
      +-----------------------------+
      |        EventBridge          |
      |   (Scheduler - Cron Jobs)   |
      +-------------+---------------+
                    |
                    |  Asynchronous Trigger
                    v
      +-----------------------------+
      |           Lambda            |
      |   StartEC2 / StopEC2 Fn     |
      +-------------+---------------+
                    |
                    |  boto3 API Call
                    v
      +-----------------------------+
      |             EC2             |
      |   Start or Stop Instance    |
      +-----------------------------+
```

---

# 🚀 Complete AWS Setup Guide (Step-by-Step)

Follow the steps below to automatically start and stop your EC2 instances using AWS services.

---

# ✅ Step 1 — Create IAM Role for Lambda

1. Open the **AWS Console**  
2. Search for **IAM**  
3. Go to **Roles**  
4. Click **Create Role**  
5. Select:
   - Trusted entity: **AWS Service**
   - Use Case: **Lambda**
6. Click **Next**  
7. Click **Create Policy**  
8. Open the **JSON** tab and paste the content from `ec2-policy.json`  
9. Name the policy: **EC2StartStopPolicy**  
10. Attach this policy to the role  
11. Name the role: **Lambda-EC2-StartStop-Role**

---

# ✅ Step 2 — Create Lambda Function (EC2 Start)

1. Go to **AWS Console → Lambda**  
2. Click **Create Function**  
3. Function Name: **StartEC2Instance**  
4. Runtime: **Python 3.12 / 3.11**  
5. Execution Role: **Lambda-EC2-StartStop-Role**  
6. Open the **Code** tab  
7. Delete the default code and paste `start_lambda.py`  
8. Click **Deploy**

---

# ✅ Step 3 — Create Lambda Function (EC2 Stop)

1. Click **Create Function**  
2. Function Name: **StopEC2Instance**  
3. Runtime: **Python**  
4. Execution Role: **Lambda-EC2-StartStop-Role**  
5. Open the **Code** tab  
6. Paste the code from `stop_lambda.py`  
7. Click **Deploy**

---

# 🧪 Step 4 — Create Test Event in Lambda

### How to Create a Test Event

1. Open your Lambda function  
2. Click **Test**  
3. Click **Create new event**  
4. Event Name:
   ```
   TestEvent
   ```
5. Event JSON:
   ```json
   {}
   ```
6. Click **Save**  
7. Press **Test** to run the Lambda manually.

---

# 🧪 Understanding Invocation  
### Synchronous (Manual Test)
- Runs immediately  
- Shows output in Lambda console  
- Triggered when using **Test** button  

### Asynchronous (EventBridge)
- Runs in background  
- Used by **EventBridge Scheduler**  

---

# ⏰ Step 5 — EventBridge Scheduler (Automation)

## Mon–Fri Start at 9 AM  
Cron Expression:
```
0 9 ? * MON-FRI *
```

## Mon–Fri Stop at 5 PM  
Cron Expression:
```
0 17 ? * MON-FRI *
```

### Steps:
1. Open **EventBridge → Scheduler**  
2. Click **Create Schedule**  
3. Choose **Cron Expression**  
4. Enter the cron  
5. Target → **Lambda Function**  
6. Select Start/Stop Lambda  
7. Click **Create Schedule**

---

# ✅ Automation Setup Completed Successfully
