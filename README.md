# 🌱 Kratky Garden Manager

**Kratky Garden Manager** is a web application built with Flask to manage hydroponic garden setups using the Kratky method. It allows users to create and manage bins, add multiple plants at once, track their growth stages, and visualize plant statuses with intuitive emoji-based representations.

## 🚀 Features

- **CRUD Operations for Bins**: Create, read, update, and delete bins to organize your plants.
- **Add Multiple Plants**: Easily add multiple plants to a bin with a single submission.
- **Pre-Populated Plant Types**: Choose from the top 15 popular garden plants or add a custom "Other" plant.
- **Auto-Filled Plant Stats**: Automatically fill in estimated days to harvest and expected yield when selecting a plant type.
- **Visual Plant Statuses**: View plant statuses as emojis for a quick overview.
- **Responsive Design**: Mobile-friendly interface with a modern and clean layout.

## 📋 Pre-requisites

- **Python 3.9+**
- **Flask** and related libraries
- **SQLite** (for the default database)

## ⚙️ Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/kratky-garden-manager.git
   cd kratky-garden-manager
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   ```

5. **Run the development server:**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000`.

## 🛠 Configuration

- The default database is set up using SQLite. You can change the database URI in `app.py` if you want to use PostgreSQL, MySQL, or another database.
- To enable debug mode, set the environment variable `FLASK_ENV=development`.

## 🌿 Usage

1. **Create a Bin**: Click on "Add New Bin" on the `/bins` page to create a new bin, specifying its name, capacity in gallons, and number of plant spaces.
2. **Add Plants**: After creating a bin, click on "Add Plant" to add multiple plants at once. Choose a plant type from the dropdown, or select "Other" to specify a custom plant. Set the start date and other details.
3. **View Bin Details**: Click on a bin name to view its detailed page. The page shows a visual representation of the plants in the bin, using emojis like:
   - 🌱 - Growing
   - 🌿 - Ready to harvest
   - 🥀 - Needs attention (overdue)
   - ⬜ - Empty spot
4. **Manage Plants**: Click on a plant's name to view its details, edit its information, or delete it.

## 🧑‍💻 Project Structure

```
kratky_garden_manager/
├── app.py                 # Main Flask application
├── models.py              # SQLAlchemy models for Bins and Plants
├── templates/             # HTML templates for different pages
│   ├── base.html
│   ├── index.html
│   ├── bins.html
│   ├── bin_detail.html
│   ├── add_plant.html
│   ├── edit_plant.html
│   └── new_bin.html
├── static/                # Static files (CSS, JavaScript)
│   ├── css/
│   │   └── style.css
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## 📚 Technologies Used

- **Flask** - Lightweight web framework for Python.
- **SQLAlchemy** - ORM for managing database models.
- **Jinja2** - Templating engine for rendering dynamic HTML.
- **Bootstrap** - For responsive, mobile-friendly design.
- **JavaScript** - For enhancing interactivity in the UI.

## 🚧 Known Issues and Limitations

- **Orphaned Plants**: If a bin is deleted, its associated plants must be managed manually to prevent orphaned records.
- **Limited Customization**: Pre-defined plant types are estimated based on a general Kratky 24-hour light system and may need customization for specific user setups.

## 📝 Future Improvements

- **Authentication**: Add user login functionality to manage individual gardens securely.
- **Notifications**: Send email reminders for upcoming or overdue harvests.
- **Advanced Analytics**: Provide growth and yield analytics over time for each bin.
- **Improved Database Management**: Automatically handle deletion of orphaned plants when bins are removed.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find bugs, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## ✨ Acknowledgments

- Inspired by the Kratky hydroponic method for quick and efficient plant growth.
- Thanks to the community for supporting open-source projects and sharing knowledge.
