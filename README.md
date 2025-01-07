# xssMan
A powerful XSS injection tool for identifying and exploiting Cross-Site Scripting vulnerabilities.

`xssMan` is a Python-based tool designed to help penetration testers and bug bounty hunters identify Cross-Site Scripting (XSS) vulnerabilities in web applications. It allows for streamlined injection testing with customizable payloads and flexible input methods.

---

## 🏗️ Installation
To install `xssMan`, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/xssMan

# Navigate to the directory
cd xssMan

# Install the tool
pip install .
```
---
## ⛏️ Usage
Use xssMan directly from the command line:

```bash
xssman -u [URL] -i [Input ID] -b [Button Value] -l [Payload List]
```
---
## 🚀 Examples
Injection Test
Test a single URL for XSS vulnerabilities using a predefined payload list:

```bash
xssman -u https://example.com -i search -b searchButton -l /path/to/xss_payload.txt
```

## 🤝 Contributing
Contributions are welcome! To contribute to xssMan, follow these steps:

1- Fork the repository.
2- Create a new branch.
3- Make your changes and commit them.
4- Submit a pull request.

## 🌟 Star History
If you find this project helpful, consider starring the repository to show your support!


[![Star History Chart](https://api.star-history.com/svg?repos=AliNayyef/xssman&type=Date)](https://star-history.com/#AliNayyef/xssman&Date)
