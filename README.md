# Functional Dependency Identification

## Project Overview
This project focuses on identifying **functional dependencies** in a database using Python. Functional dependencies are constraints that specify relationships between attributes in a database, helping to eliminate redundancies and improve database efficiency. The project aims to develop a **Django Application** that reads user input from a **CSV file** or through a provided interface, identifies potential functional dependencies, and displays or writes the output to the console or a file.

---

## What are Functional Dependencies?
A functional dependency is a constraint that specifies the relationship between two sets of attributes, where one set can accurately determine the value of another set. It is denoted as \( X \rightarrow Y \), where:
- \( X \) is the **determinant** (set of attributes that determine the value of \( Y \)).
- \( Y \) is the **dependent** (set of attributes whose value is determined by \( X \)).

### Types of Functional Dependencies
1. **Trivial Functional Dependency**
2. **Non-Trivial Functional Dependency**
3. **Multivalued Functional Dependency**
4. **Transitive Functional Dependency**

---

## Motivations
- **Eliminate Redundancies**: Functional dependencies help remove redundant data, making the database faster and more storage-efficient.
- **Maintain Consistency**: They help avoid insertion anomalies and maintain data integrity.
- **Real-World Application**: Implementing functional dependencies in a software environment provides insights into their workings and challenges.

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries/APIs**:
  - `NumPy`: For numerical computations.
  - `SciPy`: For scientific computations.
  - `Pandas`: For data manipulation and analysis.
  - `functional-dependencies`: For identifying functional dependencies.
  - `Django` : For Web-based Interaction

---

## How It Works
1. **Input**:
   - The program reads user input from a **CSV file** or through a provided interface.
   - The input consists of a valid table with attributes and their corresponding values.
2. **Processing**:
   - The program identifies potential functional dependencies in the dataset.
   - It can also find **minimal functional dependencies** and **keys** from the given data.
3. **Output**:
   - The program displays the identified functional dependencies on the console.
   - It can also write the output to a file for further analysis.

---

## Project Timeline
- **Phase 1**: Research and understanding of functional dependencies.
- **Phase 2**: Development of the CLI program.
- **Phase 3**: Implementation of additional features (minimal dependencies, key identification).
- **Phase 4**: Optional development of a web-based GUI.

---

## Future Scope
- **Expand Functionality**: Add support for more complex functional dependencies (e.g., multivalued and transitive dependencies).
- **Enhance User Interface**: Develop a fully functional web-based GUI for easier interaction.
- **Integration with Databases**: Integrate the program with real-world databases for practical applications.

---

## Contributors
- Jaimin Babaria (https://github.com/jaiminbabaria) - Project Developer
- Guided by **Anuja Nair**

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Inspired by database normalization principles.
- Special thanks to our guide, **Anuja Nair**, for her support and guidance.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Functional-Dependency-Identification.git
