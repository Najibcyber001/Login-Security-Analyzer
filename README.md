# Login Security Analyzer

## Description

A Python-based defensive cybersecurity project that analyzes login activity, calculates login statistics, detects suspicious failed-login patterns, assigns a security status, and records security events with timestamps.

This project was created to practice Python programming concepts while applying them to a practical cybersecurity use case.

## Features

* Collects username information
* Records security events
* Accepts multiple login attempts
* Validates login attempt input
* Calculates successful and failed login attempts
* Calculates login success rate
* Assigns a security status based on failed login attempts
* Records security events with timestamps
* Saves security information to a local log file

## Security Status Logic

The program assigns a security status based on the number of failed login attempts:

* **0–2 failed attempts:** Normal
* **3–4 failed attempts:** Warning
* **5 or more failed attempts:** Account Locked

## How It Works

1. The user enters a username.
2. The program asks for the total number of login attempts.
3. The user records each login attempt as either `success` or `failed`.
4. The program counts successful and failed login attempts.
5. The login success rate is calculated.
6. The program assigns a security status based on failed login attempts.
7. A security event is generated when appropriate.
8. The current date and time are recorded.
9. The security information is saved to a local text log.

## Example

Example test with 8 login attempts:

```text
Login Security Analyzer
========================
Enter the username: Ado
How many login attempts? 8

Attempt 1: type success or failed: failed
Attempt 2: type success or failed: failed
Attempt 3: type success or failed: failed
Attempt 4: type success or failed: success
Attempt 5: type success or failed: success
Attempt 6: type success or failed: success
Attempt 7: type success or failed: success
Attempt 8: type success or failed: success

Security Summary
-----------------
Username: Ado
Total login attempts: 8
Successful logins: 5
Failed logins: 3
Success rate: 62.5%
Security status: Warning
```

## Usage

Run the program from the terminal:

```bash
python login_security_analyzer.py
```

Follow the prompts and enter `success` or `failed` for each login attempt.

## Technologies Used

* Python 3
* Python Standard Library
* `datetime`
* File handling
* Input validation
* Git
* GitHub
* Markdown

## Project Structure

```text
Login-Security-Analyzer/
│
├── login_security_analyzer.py
├── .gitignore
└── README.md
```

The `security_log.txt` file is intentionally excluded from GitHub using `.gitignore` because it contains locally generated security-event records.

## Future Improvements

* Add stronger input validation
* Detect repeated suspicious login patterns
* Improve the security status system
* Store logs in a structured format such as CSV or JSON
* Add automated tests
* Add more detailed login activity analysis
* Add a simple graphical user interface

## Author

**Najib Muhammad Salis**

Cybersecurity Student | Python & Networking Learner

This project was created as part of my journey to develop practical Python and cybersecurity skills.
