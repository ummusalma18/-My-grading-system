# School Grading System

This is a simple **School Grading System** that helps check and calculate the grades of students. By entering their name and scores for different subjects, this system computes the final grade and displays it accordingly.

## Features
- Enter student details (name and scores).
- Calculate grades based on predefined score ranges.
- Display the final grade for the student.

## Prerequisites
Before running this system, ensure you have the following:
- Python 3.x installed on your machine.
- Basic knowledge of Python programming.

## How It Works
1. Enter the student's **name**.
2. Enter the student's **scores** for each subject.
3. The system computes the **final grade** based on the input scores and displays the result.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/school-grading-system.git
   ```

2. Navigate to the project folder:
   ```bash
   cd school-grading-system
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the grading system:
   ```bash
   python grading_system.py
   ```

2. Enter the student's name when prompted.
3. Enter the scores for the respective subjects.
4. The system will calculate and display the final grade.

### Example:
```plaintext
Enter Student Name: John Doe
Enter Math Score: 85
Enter Science Score: 78
Enter English Score: 92

Final Grade for John Doe: A
```

## Grade Calculation

The grade is assigned based on the following score ranges:

- **A**: 90 and above
- **B**: 80 to 89
- **C**: 70 to 79
- **D**: 60 to 69
- **F**: Below 60

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
