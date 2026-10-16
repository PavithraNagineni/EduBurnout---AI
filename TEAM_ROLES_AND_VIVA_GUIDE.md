# 🎓 PROJECT TEAM ROLES, DIVISION OF WORK & VIVA DEFENSE GUIDE
**Project Title:** Early Prediction of Academic Burnout and Cognitive Overload: A Multimodal & Temporally Sensitive Framework (BurnoutAI)

---

## 📌 QUICK OVERVIEW OF THE 4 ROLES

| Member | Domain / Role | Primary Files & Tech Stack | Core Responsibility |
| :--- | :--- | :--- | :--- |
| **Member 1** | **Frontend Engineering (UI/UX)** | React 18, Framer Motion, Axios, React Router, CSS Glassmorphism | Student portals, Weekly Check-in Form, Real-time Visualizations, Result & Dashboard UI |
| **Member 2** | **Backend Engineering (API Architecture)** | Python, Flask, Flask-CORS, JWT, RESTful APIs, Docker | REST endpoints (`/register`, `/login`, `/predict`, `/save`, `/history`), JWT auth & CORS handling |
| **Member 3** | **Database & Data Engineering** | MongoDB, PyMongo, NoSQL Collections, Compass | Schema design (`students`, `weekly_data`), Data persistence, Queries, Docker storage volumes |
| **Member 4** | **Machine Learning & AI Modeling** | Scikit-Learn, XGBoost, Recurrent Modeling (LSTM), SHAP | Dual-risk formulation, Feature engineering, Temporal baselines ($z$-score), Predictive heuristics |

---

## 👤 MEMBER 1: FRONTEND ENGINEERING & UI/UX

### 1. Work Completed in the Project
* **Modern Glassmorphic UI Design System:** Developed a responsive theme with frosted glass aesthetics, radial background ambient glows, and dark-mode gradients using `framer-motion` and custom CSS (`glassTheme.js`).
* **Authentication Views (`Login.js`, `Register.js`):**
  * Built registration and login flows with real-time password strength validation.
  * Integrated Google OAuth SDK (`@accounts.google.com/gsi/client`) for single sign-on (SSO).
* **Weekly Check-In Telemetry Form (`Form.js`):**
  * Interactive input interface capturing academic (study hours, sleep hours, exam score, attendance) and lifestyle metrics (screen time).
  * Implemented validation so students are not required to manually guess or input their stress level—the system predicts it automatically.
* **Analysis & Recommendations Screen (`Result.js`):**
  * Dynamic risk card showing severity levels (**Low**, **Medium**, **High**) with animated risk probability progress bars.
  * Context-specific actionable recommendations (recovery tips, study-break planning, sleep guidance).
* **Interactive Historical Dashboard (`Dashboard.js`, `History.js`):**
  * Graphical visualization of weekly student wellness trajectories across the semester.
* **Axios API Client (`axiosConfig.js`):**
  * Configured unified HTTP client connecting client UI to backend endpoints (`http://127.0.0.1:5000`).

### 2. What to Explain in the Presentation
* *"I developed the entire user interface and client-side experience using React 18 and Framer Motion."*
* Explain how user engagement is maintained through **non-invasive, empathetic design**—students only spend 60 seconds on the weekly check-in form.
* Explain state management with React hooks (`useState`, `useEffect`, `useNavigate`) and token persistence in `localStorage`.
* Explain responsive client-side error handling: gracefully notifying users of validation issues or network failures without crashing the application.

### 3. Likely Viva Questions & Answers
* **Q: How does the frontend communicate with the backend?**
  * *Answer:* *"We use Axios with a centralized base URL configuration. When the user submits the form, Axios sends an asynchronous POST request to the Flask server's `/predict` and `/save` endpoints."*
* **Q: Why was manual stress-level entry removed from the form?**
  * *Answer:* *"Asking students to self-rate stress is prone to subjective bias and fatigue. Our system passively infers burnout and stress probability from objective lifestyle indicators like sleep deficits and screen time."*

---

## 👤 MEMBER 2: BACKEND ENGINEERING & API ARCHITECTURE

### 1. Work Completed in the Project
* **Flask Application Architecture (`Backend/app.py`):**
  * Configured high-performance RESTful API microservice with `Flask-CORS` enabling secure cross-origin requests from the React client.
* **Authentication Engine & Security:**
  * Implemented `/register` endpoint to ingest, validate, and store new student accounts.
  * Built `/login` endpoint verifying credentials and returning unique student identifiers (`student_id`).
  * Implemented `/google-auth` endpoint for processing OAuth identity tokens.
* **Prediction & Business Logic Endpoint (`/predict`):**
  * Built the core risk assessment algorithm calculating risk category (**Low**, **Medium**, **High**) and numerical burnout probability based on behavioral metrics (sleep hours vs. screen time thresholds).
* **Telemetry Data Persistence Endpoint (`/save`):**
  * Ingests weekly academic metrics, attaches server timestamps (`created_at: datetime.now()`), and maps records to specific student IDs.
* **Historical Retrieval Endpoint (`/history/<student_id>`):**
  * Fetches all longitudinal weekly records for a given student, converting MongoDB `ObjectId` to JSON-serializable strings.
* **Containerization & Deployment (`Backend/Dockerfile`, `docker-compose.yml`):**
  * Containerized the Flask backend with Gunicorn WSGI and multi-worker configuration.
  * Added resilient connection logic with auto-fallback between Docker internal DNS (`mongo:27017`) and host `localhost:27017`.

### 2. What to Explain in the Presentation
* *"I architected and implemented the server-side REST API using Python and Flask."*
* Explain API design principles: decoupled microservice architecture where backend only serves pure JSON, allowing independent frontend evolution.
* Explain CORS management: how `CORS(app)` permits the frontend on port 3000 to communicate safely with the backend on port 5000.
* Explain data serialization: how BSON data from MongoDB is sanitized and converted to JSON for the client.

### 3. Likely Viva Questions & Answers
* **Q: What happens if the database is temporarily unreachable?**
  * *Answer:* *"We implemented a connection timeout and fallback mechanism in `app.py` using `serverSelectionTimeoutMS`. If the remote or Docker DNS fails, it falls back to localhost, preventing permanent server lockups."*
* **Q: Why use Flask instead of Django for this project?**
  * *Answer:* *"Flask is lightweight and modular. For microservice APIs serving ML inference and JSON endpoints, Flask avoids the heavy ORM and template overhead of Django, resulting in lower latency."*

---

## 👤 MEMBER 3: DATABASE & DATA ENGINEERING

### 1. Work Completed in the Project
* **Database Architecture & Technology Selection:**
  * Selected **MongoDB** (NoSQL Document Store) to accommodate dynamic, polymorphic student telemetry where feature sets can evolve over time without breaking table schemas.
* **Schema & Collection Design:**
  * **`students` Collection:** Stores user identity profiles (name, email, hashed credentials, Google ID, profile avatar, registration date).
  * **`weekly_data` Collection:** Stores longitudinal time-series documents capturing student weekly states:
    ```json
    {
      "student_id": "6a9ed5b42c959bf82e993c93",
      "week_no": 1,
      "study_hours": 6,
      "sleep_hours": 7,
      "screen_time": 4,
      "attendance_percentage": 85,
      "exam_score": 75,
      "burnout_probability": 0.25,
      "risk_level": "Low",
      "created_at": "2026-09-07T20:47:00"
    }
    ```
* **Relationship Modeling:**
  * Designed document referencing via foreign key mapping (`student_id` string referencing `students._id`), enabling 1-to-N relationships (one student has multiple weekly check-in documents).
* **Data Sanitization & Integrity:**
  * Cleaned records so that subjective fields (manual stress level) are excluded from persistence, ensuring clean time-series datasets.
* **Database Deployment & Docker Volumes:**
  * Configured local MongoDB server (`C:\data\db`) and Docker containerized MongoDB (`mongo:6.0`) with persistent named volumes (`mongo_data:/data/db`).

### 2. What to Explain in the Presentation
* *"I designed the database architecture, schema structures, and data persistence pipeline using MongoDB."*
* Explain **Why NoSQL/MongoDB was chosen over SQL/Relational databases**: Time-series behavioral logs frequently add new telemetry dimensions (e.g., adding keystroke jitter or LMS clicks in phase 2) without needing expensive SQL schema migrations (`ALTER TABLE`).
* Explain **Query Optimization**: How queries like `weekly_data.find({"student_id": id})` retrieve student chronological history with minimal latency.
* Explain **Data Privacy**: Separation of sensitive profile identities from anonymous weekly behavioral logs.

### 3. Likely Viva Questions & Answers
* **Q: How do you handle relationships between students and weekly records in MongoDB?**
  * *Answer:* *"We use manual referencing: each document in `weekly_data` stores the parent student's `_id` as `student_id`. This keeps document sizes compact and allows quick indexed lookups without unbounded document growth."*
* **Q: How is data preserved when containers restart?**
  * *Answer:* *"We configured persistent Docker volumes (`mongo_data:/data/db`), ensuring data survives container restarts and upgrades."*

---

## 👤 MEMBER 4: MACHINE LEARNING & AI MODELING

### 1. Work Completed in the Project
* **Theoretical Framework Formulation:**
  * Formulated the conceptual separation between **Academic Burnout** (prolonged, cumulative exhaustion) and **Cognitive Overload** (acute, task-bound working memory demand based on Cognitive Load Theory).
* **Feature Engineering & Multimodal Telemetry Pipeline:**
  * Identified passive behavioral indicators: keystroke dynamics (dwell time, flight latency), mouse cursor entropy (jitter, curvature), and lifestyle rhythmicity (sleep debt, screen exposure).
* **Personalized Baseline Modeling ($z$-Score Normalization):**
  * Formulated dynamic individual baseline transformation:
    $$z_{i,t} = \frac{x_{i,t} - \mu_i}{\sigma_i + \epsilon}$$
    evaluating deviations against a student's *own* historical habits rather than arbitrary, biased population averages.
* **Dual-Target Risk Modeling & Multi-Task Objective:**
  * Formulated the multi-task learning optimization objective:
    $$\mathcal{L}_{total} = \lambda_B \cdot \mathcal{L}_{CE}(R_B, \hat{R}_B) + \lambda_C \cdot \mathcal{L}_{CE}(R_C, \hat{R}_C) + \gamma \|\Theta\|_2^2$$
* **Algorithm Benchmarking:**
  * Compared structured ensemble classifiers (Random Forest, XGBoost) and sequential architectures (LSTM/GRU) for temporal dependencies:
    $$h_{i,t} = \text{LSTM}(z_{i,t}, h_{i,t-1})$$
* **Explainable AI (XAI) & Uncertainty Filtering:**
  * Integrated SHAP (SHapley Additive exPlanations) for local feature attribution and persistence thresholds to eliminate false alarms caused by isolated temporary anomalies.

### 2. What to Explain in the Presentation
* *"I formulated the predictive intelligence, mathematical modeling, and machine learning framework."*
* Explain the difference between acute cognitive overload and chronic burnout (use the four-quadrant matrix).
* Explain why personal baseline normalization ($z$-score) is essential: a night-owl or naturally slow typer should not be penalized by rigid universal thresholds.
* Explain how Explainable AI (SHAP) bridges the gap between machine predictions and empathetic counseling.

### 3. Likely Viva Questions & Answers
* **Q: Why not use a deep neural network for everything?**
  * *Answer:* *"Tabular behavioral telemetry in education is often sparse. Tree-based ensembles like XGBoost and Random Forest frequently outperform deep neural networks on tabular metrics while offering faster training, resistance to overfitting, and native interpretability via SHAP."*
* **Q: How does your model avoid false alarms during exam week?**
  * *Answer:* *"We introduced temporal persistence filtering: alerts require sustained behavioral deviation across multiple consecutive evaluation epochs ($m$ time steps), preventing temporary examination spikes from triggering false alarms."*

---

## 🤝 HOW THE 4 PARTS INTEGRATE (THE SYSTEM WORKFLOW)

```text
[STUDENT] 
   │
   ▼
[1. FRONTEND - React] ──── (Submits 5 Behavioral Metrics)
   │
   ▼  HTTP POST /predict & /save (JSON)
[2. BACKEND - Flask] 
   │
   ├──► [4. ML ENGINE] ─── (Calculates Risk Probability & Category)
   │
   ▼  PyMongo insert_one()
[3. DATABASE - MongoDB] ── (Persists into 'weekly_data' linked to student_id)
   │
   ▼  Returns Status & Risk Payload
[1. FRONTEND - React] ──── (Renders Animated Result Card & Recommendations)
```
