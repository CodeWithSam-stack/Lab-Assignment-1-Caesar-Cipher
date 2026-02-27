# Lab Assignment 1 – Caesar Cipher

## Course Information
Course: Information Security  
Semester: Spring 2026  
University: COMSATS University Islamabad, Attock Campus  

## Student Information
Name: Samrina Manahil
Roll Number: FA24-BSE-052 
Class: SE 4  

---

## Project Description
This project implements the Caesar Cipher encryption and decryption algorithm using Python.

The program:
- Encrypts a message using a given shift value.
- Decrypts the encrypted message back to its original form.
- Maintains uppercase and lowercase letters.
- Keeps spaces and special characters unchanged.

---

## Functions Implemented

### 1. caesar_encrypt(text, shift)
Encrypts the given text using the specified shift value.

### 2. caesar_decrypt(ciphertext, shift)
Decrypts the encrypted text back to the original message.

---

## How to Run the Program

1. Make sure Python is installed.
2. Open terminal or command prompt.
3. Navigate to the project folder.
4. Run:

python Assignment01_Code.py

5. Enter the message and shift value when prompted.

---

## Security Analysis (Summary)

The Caesar Cipher is a classical substitution cipher.  
It shifts letters by a fixed number of positions.

However:
- It has only 25 possible keys.
- It is vulnerable to brute-force attacks.
- It is not secure for modern communication systems.

---

## Files Included

- Assignment01_Code.py → Python Implementation
- FA24-BSE-052 (Assignment01).pdf → Detailed explanation and analysis
