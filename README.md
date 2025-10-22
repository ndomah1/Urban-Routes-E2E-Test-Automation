# 🚖 Urban Routes — End-to-End Test Automation (Selenium + Pytest + POM)

This project implements a **complete end-to-end UI testing framework** for a web-based taxi booking application using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.  
It validates the entire flow of ordering a taxi — from entering pickup and drop-off addresses to verifying the car search modal.

## 🧩 Key Features

- **Page Object Model (POM):** Abstracted UI interactions for maintainability and scalability.  
- **Full E2E Coverage:** Automated tests cover every major user action in the booking workflow.  
- **Dynamic Element Handling:** Incorporated conditional logic and focus events to handle non-clickable or delayed elements.  
- **Network Log Parsing:** Used Chrome DevTools Protocol to intercept and extract SMS verification codes automatically.  
- **Stable & Scalable Tests:** Leveraged explicit waits, reusability, and idempotent test steps to minimize flakiness.  
- **Continuous Integration:** Configured a GitHub Actions pipeline to run Selenium tests in a headless Chrome environment.

## 🧪 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3.11** | Core scripting language |
| **Selenium 4** | Browser automation |
| **Pytest** | Testing framework |
| **ChromeDriver (headless)** | Test execution |
| **GitHub Actions** | CI automation |

## ✅ Test Scenarios

1. Set pickup and destination addresses  
2. Select the *Supportive* plan (with condition checks to avoid redundant clicks)  
3. Fill in and verify phone number (using `retrieve_phone_code()`)  
4. Add a credit card with focus handling for CVV  
5. Write and verify a driver comment  
6. Toggle blanket & handkerchiefs, then assert state change  
7. Add two ice creams  
8. Order taxi and assert that the car search modal appears  

## 🧠 Highlights

- Applied **object-oriented design** for modular test logic.  
- Practiced **synchronization strategies** for dynamic elements.  
- Demonstrated **CI/CD readiness** with cloud-based test execution.  
- Delivered a **production-level E2E test suite** that can integrate with larger QA workflows.

## 📈 Outcome

This project showcases advanced **automation architecture**, strong command of **Selenium and Pytest**, and the ability to design maintainable, scalable test suites for complex UI flows.
