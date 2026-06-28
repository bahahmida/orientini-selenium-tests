# 🎓 Orientini.com - Selenium Automated Test Suite

**CI1 Project — Software Engineering 2025-2026**

[![Tests](https://img.shields.io/badge/tests-38-blue)](https://github.com/your-username/orientini-selenium-tests)
[![Passing](https://img.shields.io/badge/passing-28-green)](https://github.com/your-username/orientini-selenium-tests)
[![Failing](https://img.shields.io/badge/failing-10-red)](https://github.com/your-username/orientini-selenium-tests)
[![Success Rate](https://img.shields.io/badge/success-73.68%25-yellow)](https://github.com/your-username/orientini-selenium-tests)

---

## 📋 About

This project contains an **automated test suite** for [Orientini.com](https://orientini.com/), a Tunisian educational and professional orientation portal. The tests are implemented using **Python**, **Selenium WebDriver**, and the **unittest** framework.

---

## 📊 Test Results Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases** | 38 |
| **✅ Passed** | 28 |
| **❌ Failed** | 10 |
| **Success Rate** | 73.68% |
| **Bugs Detected** | 10 |

---

## 🏗️ Project Structure

orientini-selenium-tests/
├── test_TC01_TC14.py # Navigation & UI tests
├── test_TC15_TC23.py # Search, Orientation & Auth tests
├── test_TC24_TC38.py # Advanced Auth, Forms & Bug tests
├── README.md # Documentation
├── requirements.txt # Dependencies
└── .gitignore # Ignored files


---

## 🧪 Test Modules Covered

| Module | Test Cases | Status |
|--------|------------|--------|
| **Navigation** | TC-01 to TC-06, TC-12, TC-14, TC-33 to TC-37 | 10 ✅ / 4 ❌ |
| **Responsive** | TC-07 | ❌ |
| **Performance** | TC-08 | ❌ |
| **Filières** | TC-09, TC-21, TC-24 | ✅ |
| **UI** | TC-10, TC-38, TC-39 | 2 ✅ / 1 ❌ |
| **Articles** | TC-11 | ✅ |
| **Orientation** | TC-13, TC-18, TC-23 | ✅ |
| **Search** | TC-15, TC-19, TC-20, TC-22 | ✅ |
| **Authentication** | TC-16, TC-17, TC-26 to TC-29 | 4 ✅ / 2 ❌ |
| **Forms** | TC-30, TC-31, TC-32 | 2 ✅ / 1 ❌ |

---

## 📝 Detailed Test Cases

### Navigation Tests (TC-01 to TC-06, TC-12, TC-14, TC-33 to TC-37)

| ID | Title | Status |
|----|-------|--------|
| TC-01 | Homepage Loading | ✅ PASS |
| TC-02 | Navigation Menu Verification | ✅ PASS |
| TC-03 | Page Translation (FR/AR) | ❌ FAIL |
| TC-04 | Navigation to Notifications | ✅ PASS |
| TC-05 | Navigation to Messages | ✅ PASS |
| TC-06 | Navigation via Sidebar | ✅ PASS |
| TC-12 | Partners Space | ✅ PASS |
| TC-14 | Social Media Links | ✅ PASS |
| TC-33 | Language Selector | ✅ PASS |
| TC-34 | Orientation Submenu | ✅ PASS |
| TC-35 | French URL in Fresh Session | ❌ FAIL |
| TC-36 | Duplicate Links in Menu | ❌ FAIL |
| TC-37 | Reorientation Mars Page | ✅ PASS |

### UI & Responsive Tests

| ID | Title | Status |
|----|-------|--------|
| TC-07 | Mobile Display (375px) | ❌ FAIL |
| TC-10 | Open and Close Advert | ❌ FAIL |
| TC-38 | Loading Spinner | ✅ PASS |
| TC-39 | Empty Page Title | ✅ PASS |

### Performance Tests

| ID | Title | Status |
|----|-------|--------|
| TC-08 | Page Loading Time | ❌ FAIL |

### Filières Tests

| ID | Title | Status |
|----|-------|--------|
| TC-09 | Categories Section | ✅ PASS |
| TC-21 | University Branches Search | ✅ PASS |
| TC-24 | Filtering University Branches | ✅ PASS |

### Articles Tests

| ID | Title | Status |
|----|-------|--------|
| TC-11 | News Section | ✅ PASS |

### Orientation Tests

| ID | Title | Status |
|----|-------|--------|
| TC-13 | Important Dates Display | ✅ PASS |
| TC-18 | Orientation Score Calculation | ✅ PASS |
| TC-23 | Important Dates Section | ✅ PASS |

### Search Tests

| ID | Title | Status |
|----|-------|--------|
| TC-15 | Search Functionality | ✅ PASS |
| TC-19 | Job Offers Search | ✅ PASS |
| TC-20 | Vocational Training Search | ✅ PASS |
| TC-22 | Scholarships Search | ✅ PASS |

### Authentication Tests

| ID | Title | Status |
|----|-------|--------|
| TC-16 | Account Creation (Sign Up) | ❌ FAIL |
| TC-17 | Login (Authentication) | ❌ FAIL |
| TC-26 | Wrong Password Rejected | ✅ PASS |
| TC-27 | Invalid Email Rejected | ❌ FAIL |
| TC-28 | SQL Injection Blocked | ✅ PASS |
| TC-29 | Logout Redirection | ✅ PASS |

### Forms Tests

| ID | Title | Status |
|----|-------|--------|
| TC-30 | Contact Form & Submit Button | ✅ PASS |
| TC-31 | Email Validation on Registration | ❌ FAIL |
| TC-32 | Contact Form Required Fields | ✅ PASS |

---

## 🐞 Detected Bugs

| ID | Title | Module | Severity | Priority | Related TC |
|----|-------|--------|----------|----------|------------|
| B-01 | Incomplete page translation (FR/AR) | Navigation | High | P1 | TC-03 |
| B-02 | French URL displays Arabic in fresh session | Navigation | High | P2 | TC-35 |
| B-03 | Duplicate links in menu | Navigation | Medium | P3 | TC-36 |
| B-04 | Mobile display (375px) broken | Responsive | High | P2 | TC-07 |
| B-05 | Page loading time > 5 seconds | Performance | High | P1 | TC-08 |
| B-06 | Advert close button not responding | UI | High | P3 | TC-10 |
| B-07 | Account creation fails | Authentication | Critical | P1 | TC-16 |
| B-08 | Login page missing fields | Authentication | Critical | P2 | TC-17 |
| B-10 | Invalid email accepted by server | Authentication | Medium | P2 | TC-27 |
| B-11 | Registration page PHP fatal error | Forms | Critical | P1 | TC-31 |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.x |
| **Test Framework** | unittest |
| **Browser Automation** | Selenium WebDriver |
| **Browser** | Microsoft Edge |
| **OS** | Windows / Linux / macOS |

