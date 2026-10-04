# Login Security Analyzer

## Description

A Python-based defensive cybersecurity project that analyzes login activity, calculates login statistics, detects suspicious failed-login patterns, assigns a security status, and records security events with timestamps.

## Features

- Collects username and security event information
- Calculates failed login attempts
- Calculates login success rate
- Assigns a security status based on failed login attempts
- Records security events with timestamps
- Stores security logs in a text file

## How It Works

1. The user enters a username.
2. The user enters a security event.
3. The program asks for the total number of login attempts.
4. The program asks for the number of successful logins.
5. Failed login attempts are calculated.
6. The login success rate is calculated.
7. The program assigns a security status based on failed login attempts.
8. The security event is recorded with the current date and time.
9. The security information is stored in a log file.

## Usage

Run the program from the terminal:

```bash
python login_security_analyzer.py
```

## Example Output

```text
Enter username: Ado
Enter security event: Multiple failed login attempts
Enter total login attempts: 8
Enter total successful login: 5

Failed logins: 3
Login success rate: 62.50%
Security status: Warning
Timestamp: 2026-10-02 17:30:00
```

## Technologies Used

- Python 3
- Python Standard Library
- `datetime`
- File handling
- Git and GitHub
- Markdown

## Project Structure

```text
Login-Security-Analyzer/
│
├── login_security_analyzer.py
├── security_log.txt
├── .gitignore
└── README.md
```

## Future Improvements

- Add stronger input validation
- Add more detailed login activity analysis
- Detect repeated suspicious login patterns
- Improve the security status system
- Store logs in a structured format
- Add a simple graphical user interface
- Add automated tests

## Author

**Najib Muhammad Salis**

Cybersecurity Student | Python & Networking Learner

This project was created as part of my journey to develop practical Python and cybersecurity skills.