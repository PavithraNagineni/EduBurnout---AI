# EduBurnout---AI

### Early Prediction of Academic Burnout and Cognitive Overload Using Behaviour Analysis

EduBurnout AI is an AI-powered project designed to support the early identification of academic burnout and cognitive overload by analyzing student behavioral patterns. The system aims to help identify potential signs of academic stress and provide insights that can encourage timely intervention and healthier study habits.

##  Objectives

- Identify potential indicators of academic burnout and cognitive overload.
- Analyze student behavioral data to support early risk prediction.
- Provide a user-friendly interface for interacting with the system.
- Store student account information and relevant analysis data.
- Support student well-being through data-driven insights.

##  Key Features

- **Student Authentication:** Registration and login functionality.
- **Behavioral Analysis:** Analyze relevant student behavioral information.
- **AI-Based Prediction:** Use machine learning to estimate potential burnout or cognitive overload risk.
- **Data Management:** Store and manage application data.
- **Web Interface:** Frontend for user interaction with the backend.
- **Docker Support:** Docker Compose configuration for containerized development and deployment.

##  Technology Stack

Update this list to match the technologies actually implemented in your project.

| Component | Technology |
|---|---|
| Frontend | React.js |
| Backend | Python, Flask |
| Database | MongoDB |
| AI/ML | Machine Learning / Deep Learning |
| API | REST API |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

##  Project Structure

```text
EduBurnout---AI/
├── Backend/                   # Backend API and application logic
├── frontend/                  # Frontend user interface
├── docker-compose.yml          # Docker Compose configuration
├── Overview (Flask).txt       # Backend overview
├── Project_Report.pdf         # Major project report
├── Review_Paper.docx          # Research/review paper
├── TEAM_ROLES_AND_VIVA_GUIDE.md
├── report.txt                 # Project report notes
├── running.txt                # Application running instructions
└── README.md                  # Project documentation
```

##  Prerequisites

Install the following tools before running the project:

- Python 3.x
- Node.js and npm
- MongoDB
- Git
- Docker Desktop (optional, if using Docker Compose)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PavithraNagineni/EduBurnout---AI.git
cd EduBurnout---AI
```

### 2. Configure the backend

Open the backend directory:

```bash
cd Backend
```

Install the Python dependencies using the dependency file provided by the project. For example, if `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in your `.env` file, including database connection settings and any application secrets.

Start the Flask application using the entry point specified by your backend configuration. For example, if the entry point is `app.py`:

```bash
python app.py
```

### 3. Configure the frontend

Open a separate terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
npm start
```

Use the development command configured in `package.json` if your project uses Vite or another frontend tool.

### 4. Access the application

Open the local frontend URL shown in your terminal. The backend API will run at the configured local address and port.

**Note:** The exact commands and URLs may vary depending on your project configuration.

## How It Works

1. **User Registration:** Students create an account and log in.
2. **Data Collection:** The application receives relevant student behavioral or academic inputs.
3. **Data Processing:** The backend validates and processes the submitted information.
4. **Risk Prediction:** The configured AI/ML model analyzes the input and generates a prediction.
5. **Results:** The application presents the available prediction or analysis to the user.

The actual inputs, prediction categories, and model outputs depend on the implementation in the project.

## Privacy and Security

- Keep credentials and API keys in environment variables.
- Do not commit `.env` files or other files containing secrets.
- Restrict access to student data and use appropriate security measures.
- Treat model predictions as indicative insights, not as a medical diagnosis.

## Future Enhancements

- Improve model performance through additional validation and evaluation.
- Add personalized study recommendations.
- Introduce progress tracking and visual analytics.
- Enhance privacy controls and secure data handling.
- Evaluate prediction quality on representative student datasets.

## Team

This project was developed as an academic major project. Add the names and contributions of your team members here.

## Documentation

Refer to the project report, review paper, and team viva guide included in this repository for additional information.

## Disclaimer

EduBurnout AI is intended for academic research and student well-being support. Predictions should not be used as a definitive assessment of a student's mental health or as a substitute for professional advice.

## License

No license has been specified yet. Add an appropriate open-source license if you intend to permit others to reuse or modify this project.
