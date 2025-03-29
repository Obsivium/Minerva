# 🎲 Minerva

A Python script that generates random names by fetching and processing data from multiple sources. The names are extracted from:

- 💎 **Gemstones**
- ⚡️ **Greek Gods**
- 🏛️ **Roman Deities**

---

## 📚 Overview

This script uses publicly available JSON datasets from [Darius Kazemi's Corpora Project](https://github.com/dariusk/corpora) to provide a random name based on different themes. It extracts and formats the names before displaying one at random.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/obsivium/minerva.git
cd minerva
```

### 2. Install Required Dependencies
The only dependency is `requests`. You can install it with:
```bash
pip install requests
```

### 3. Run the Script
```bash
python minerva.py
```

---

## ⚡️ How It Works

1. **Fetch Data:** The script sends HTTP requests to the specified URLs and retrieves JSON data.
2. **Process Data:** It extracts relevant elements from the JSON files and processes the names.
3. **Random Selection:** A random name is picked from the processed list and displayed.

---

## 🛠️ Customization

### Add New Sources
To add more sources or modify existing ones, update the `name_data` list in `minerva.py`:

```python
name_data = [
    {
        "link": "https://example.com/your-json-file.json",
        "element": "your_element",
        "extract_func": lambda x: x.split(" ")[-1]
    }
]
```

### Modify Name Extraction Logic
You can adjust the `extract_func` to apply different processing rules. For example:
- To take the **first word**:
```python
"extract_func": lambda x: x.split(" ")[0]
```
- To use the full name:
```python
"extract_func": lambda x: x.title()
```

---

## 🎁 Example Output
```
Minerva
```

---

## 🔥 Error Handling
If an error occurs while fetching or processing the data, the script will display an error message and return a fallback value:
```
Error fetching or parsing data: <error_message>
```

---

## 📝 Credits

This project uses data from [Darius Kazemi's Corpora Project](https://github.com/dariusk/corpora), which provides a variety of structured data in JSON format.

---

## 📜 License

This project is licensed under the **GNU GENERAL PUBLIC LICENSE V3.0**.


## ✉️ Support
For issues or contributions, open a GitHub issue!

**Author:** [Obsivium](https://github.com/Obsivium)


**The name (Minerva) was generated using this program 🚀**
