# Login with Google

This is a simple Flask application that demonstrates how to implement a "Login with Google" functionality.

## Getting Started

### Prerequisites

- Python 3.6+ anaconda
- A Google Cloud Platform project with OAuth 2.0 credentials.

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requisitos.txt
   ```

4. **Create a `.env` file:**

   Create a `.env` file in the root directory of the project and add the following environment variables:

   ```
   GOOGLE_CLIENT_ID=<your-google-client-id>
   GOOGLE_CLIENT_SECRET=<your-google-client-secret>
   APP_SECRET_KEY=<your-app-secret-key>
   ```

### Running the Application

   ```bash
   flask run
   ```

   The application will be running at `http://127.0.0.1:5000`.
