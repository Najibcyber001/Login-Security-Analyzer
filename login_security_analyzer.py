from datetime import datetime
from pathlib import Path


LOG_FILE = Path(__file__).with_name("security_log.txt")


def analyze_logins(username, attempts):
    """Calculate security information from a list of login outcomes."""
    total_attempts = len(attempts)
    successful_logins = attempts.count("success")
    failed_logins = attempts.count("failed")
    success_rate = (successful_logins / total_attempts) * 100

    if failed_logins <= 2:
        security_status = "Normal"
        security_event = "Login activity is normal"
    elif failed_logins <= 4:
        security_status = "Warning"
        security_event = "Suspicious login activity detected"
    else:
        security_status = "Account Locked"
        security_event = "Account has been locked due to excessive failed login attempts"

    return {
        "username": username,
        "total_attempts": total_attempts,
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "success_rate": success_rate,
        "security_status": security_status,
        "security_event": security_event,
    }


def write_security_event(summary):
    """Append one security event to the text log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = (
        f"{timestamp} | username={summary['username']} | "
        f"total_attempts={summary['total_attempts']} | "
        f"successful_logins={summary['successful_logins']} | "
        f"failed_logins={summary['failed_logins']} | "
        f"success_rate={summary['success_rate']:.1f}% | "
        f"status={summary['security_status']} | "
        f"event={summary['security_event']}\n"
    )

    needs_newline = LOG_FILE.exists() and LOG_FILE.stat().st_size > 0
    if needs_newline:
        with LOG_FILE.open("rb") as file:
            file.seek(-1, 2)
            needs_newline = file.read(1) != b"\n"

    with LOG_FILE.open("a", encoding="utf-8") as file:
        if needs_newline:
            file.write("\n")
        file.write(log_line)


def get_positive_number(prompt):
    """Ask for a positive whole number until the user enters one."""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def get_login_result(attempt_number):
    """Ask whether one login attempt succeeded or failed."""
    while True:
        result = input(
            f"Attempt {attempt_number}: type success or failed: "
        ).strip().lower()
        if result in {"success", "s"}:
            return "success"
        if result in {"failed", "fail", "f"}:
            return "failed"
        print("Please type success or failed.")


def main():
    print("Login Security Analyzer")
    print("=" * 24)

    username = input("Enter the username: ").strip()
    while not username:
        print("Username cannot be empty.")
        username = input("Enter the username: ").strip()

    total_attempts = get_positive_number("How many login attempts? ")
    attempts = [
        get_login_result(attempt_number)
        for attempt_number in range(1, total_attempts + 1)
    ]

    summary = analyze_logins(username, attempts)
    write_security_event(summary)

    print("\nSecurity Summary")
    print("-" * 17)
    print(f"Username: {summary['username']}")
    print(f"Total login attempts: {summary['total_attempts']}")
    print(f"Successful logins: {summary['successful_logins']}")
    print(f"Failed logins: {summary['failed_logins']}")
    print(f"Success rate: {summary['success_rate']:.1f}%")
    print(f"Security status: {summary['security_status']}")
    print(f"Date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Security event: {summary['security_event']}")
    print(f"Saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()
