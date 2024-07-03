# Password Strength Assessment

This repository contains a Python tool to assess the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides feedback to users on the password's strength.

## Features

- **Length Check:** Ensures the password is at least 8 characters long.
- **Uppercase Letter Check:** Ensures the presence of at least one uppercase letter.
- **Lowercase Letter Check:** Ensures the presence of at least one lowercase letter.
- **Digit Check:** Ensures the presence of at least one digit.
- **Special Character Check:** Ensures the presence of at least one special character.
- **Feedback:** Provides detailed feedback based on the password's strength.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/password-strength-assessment.git
   cd password-strength-assessment

## Usage
### Running the Script
You can run the script by executing the following command in your terminal:
`python password_strength.py`

## Example Usage
### Here is an example of how you can use the script:

1. Input a Password: When you run the script, you will be prompted to enter a password to assess.

2. Receive Feedback: The script will evaluate the password and provide a strength score along with specific feedback on how to improve it.

### Example:
 ```
 Enter a password to assess: MyPassw0rd!
 Password Strength: 5/5
 Password is very strong.
```
## How It Works
### The script evaluates the password based on the following criteria:
#### 1. Length Check:

- The password should be at least 8 characters long.
- If the length is less than 8 characters, feedback will be provided to suggest increasing the length.

#### 2. Uppercase Letter Check:

- The password should contain at least one uppercase letter (A-Z).
- If no uppercase letter is found, feedback will be provided to suggest adding an uppercase letter.

#### 3. Lowercase Letter Check:

- The password should contain at least one lowercase letter (a-z).
- If no lowercase letter is found, feedback will be provided to suggest adding a lowercase letter.

#### 4. Digit Check:

- The password should contain at least one digit (0-9).
- If no digit is found, feedback will be provided to suggest adding a digit.

#### 5. Special Character Check:

- The password should contain at least one special character (e.g., @, $, !, %, *, ?, &, #).
- If no special character is found, feedback will be provided to suggest adding a special character.

#### 6. Feedback Based on Strength:

- The script calculates a strength score (0-5) based on the above checks.
- Detailed feedback is provided based on the score:
- 5/5: Password is very strong.
- 4/5: Password is strong.
- 3/5: Password is moderate.
- 2/5: Password is weak.
- 1/5 or 0/5: Password is very weak.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
