# Period_tracking_system_webapp

A user-friendly period tracking web application built with **HTML**, **CSS**, **JavaScript**, **Flask**, and **MS-SQL**. This app helps users monitor their menstrual cycles, predict future periods, and maintain personal health records.

---

## Features

- **User Authentication**: Secure login and registration.
- **Cycle Tracking**: Log period start and end dates.
- **Predictions**: Predict next period and fertile window.
- **Health Insights**: Track symptoms, mood, and flow intensity.

---

## Technologies Used

### Frontend
- **HTML**: Structure of the web pages.
- **CSS**: Styling and layout design.
- **JavaScript**: Interactive elements and client-side logic.

### Backend
- **Flask**: Web framework for handling routes, APIs, and server-side logic.
- **MS-SQL**: Database for storing user data securely.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jainasthaaa/Period_trcking_system_webapp.git
   cd Period_trcking_system_webapp
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   - Create an MS-SQL database.
   - Update the `config.py` file with your database credentials.

5. **Run the App**:
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000/`.

---

## Usage

1. **Sign Up/Login**: Create an account or log in.
2. **Track Your Cycle**: Log your period dates, symptoms, and mood.
3. **View Predictions**: Check the dashboard for upcoming cycle predictions and reminders.
4. **Intuitive Calendar**: Mark your dates for future.

---

## Folder Structure

```plaintext
period-tracker-web-app/
├── static/
│   ├── css/          # CSS files
│   ├── js/           # JavaScript files
│   ├── images/       # Static images
├── templates/        # HTML templates
├── app.py            # Flask app entry point
├── config.py         # Configuration settings
├── models.py         # Database models
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to enhance and bring new technology revolution into this project.

