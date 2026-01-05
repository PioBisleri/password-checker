
# 🔐 Password Strength Checker

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://pep8.org/)

A comprehensive password strength analyzer that helps users create secure passwords by evaluating multiple security criteria in real-time.

## 🌟 Features

- **Real-time Analysis**: Instant feedback on password strength as you type
- **Comprehensive Checks**:
  - ✅ Uppercase letters (A-Z)
  - ✅ Lowercase letters (a-z) 
  - ✅ Numbers (0-9)
  - ✅ Special characters (!, @, #, etc.)
  - ✅ Minimum length requirement (8+ characters)
- **Security Scoring**: Clear 5-point scoring system with visual indicators
- **Common Password Detection**: Warns against widely-used vulnerable passwords
- **Educational Tips**: Actionable advice for creating stronger passwords
- **User-Friendly Interface**: Clean, intuitive command-line experience
- **Exit Command**: Type 'quit' anytime to exit gracefully

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation
```bash
# Clone the repository
git clone https://github.com/PioBisleri/password-checker.git
cd password-checker

# No additional dependencies required!
```

### Usage
```bash
python password_checker.py
```

### Example Output
```
Enter your Password (or 'quit' to exit): SecureP@ss123
✓ Has Uppercase
✓ Has Lowercase
✓ Has Number
✓ Has Special Letter
✓ Has 8+ Letters

Score: 5/5
Password Strength: STRONG

💡 Tips for a stronger password:
• Consider using a passphrase: 4+ random words or a memorable phrase
• Longer is better than complex - aim for 15+ characters
• Avoid personal info that's on social media (names, birthdays, pets)
==================================================
```

## 🛡️ Security Considerations

**Important**: This tool is designed for educational purposes only. For production use:
- Passwords are processed locally and never stored or transmitted
- No internet connection required during operation
- All analysis happens in-memory with immediate cleanup
- **Never** use this tool to check actual production passwords in a shared environment

## 📊 Scoring System

| Criteria | Points | Requirement |
|----------|--------|-------------|
| Uppercase Letters | 1 | At least one A-Z |
| Lowercase Letters | 1 | At least one a-z |
| Numbers | 1 | At least one digit |
| Special Characters | 1 | Non-alphanumeric, non-space character |
| Length | 1 | 8+ characters |
| **Total** | **5** | **Maximum Score** |

**Strength Ratings:**
- **0-2 points**: WEAK - Easily crackable
- **3-4 points**: MEDIUM - Moderate protection
- **5 points**: STRONG - Good security foundation

## 🚧 Future Improvements

- [ ] Add entropy calculation for more accurate strength measurement
- [ ] Implement password history check against breach databases (via HaveIBeenPwned API)
- [ ] Add password generation functionality
- [ ] Create GUI version with visual strength meter
- [ ] Support custom rule configuration
- [ ] Add unit tests for validation logic

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

For questions, feature requests, or bug reports:
- Create an issue on GitHub
- Follow updates: [@PioBisleri](https://github.com/PioBisleri)

---

**Remember**: A strong password is your first line of defense against unauthorized access. This tool helps you understand what makes a password secure, but always follow best practices for password management in real-world applications.
