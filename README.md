# tasky-api


task_manager/
├── app/
│   ├── __init__.py            # Initializes the Flask app
│   ├── models.py              # Defines database models
│   ├── routes.py              # Defines API routes
│   ├── schemas.py             # Optional: Handles serialization/validation with Marshmallow
│   ├── services.py            # Optional: Business logic or helper functions
│   └── config.py              # Configuration settings
├── migrations/                # For database migrations (if using Flask-Migrate)
├── tests/                     # Test cases
│   ├── test_app.py
│   └── test_routes.py
├── venv/                      # Virtual environment (optional but recommended)
├── requirements.txt           # Dependencies
├── run.py                     # Entry point to run the application
└── README.md                  # Project description/documentation