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


---


# The Kratky Method (How To Grow Plants The Easy Way)

Use these resources for growing plants using the Kratky hydroponic technique.

## Set Up Instructions
### Materials Needed:

- Seeds of the plant you wish to grow
- Rockwool cubes
- Vermiculite
- Non-transparent container (large enough to hold your plant's root system, e.g., plastic tubs or mason jars)
- Hydroponic nutrients
- Water
- pH test kit
- pH Up/Down solution
- Seedling heat mat (optional, depending on plant type and your local climate)
- Grow lights (optional, depending on your indoor light conditions)
- Seedling tray or propagation dome (optional, for initial germination)

### Steps:

1. Soak your rockwool cubes in water with a pH level around 5.5-6.5 for about an hour.
2. Place your soaked rockwool cubes in a seedling tray or propagation dome if available. If not, any shallow container will work.
3. Place your seeds into the holes in the rockwool cubes. Some seeds may require more than one seed per cube.
4. Cover the seeds with a small amount of vermiculite. This helps retain moisture and blocks light from reaching the seed.
5. If using a seedling heat mat, place your seedling tray on it and maintain the temperature suitable for your specific type of plant seed.
6. Keep the rockwool cubes moist but not oversaturated, usually, a daily light watering is enough until seeds germinate.
7. Once the seeds have sprouted and developed a couple of sets of true leaves, they're ready to be moved to the non-transparent container.
8. Fill the non-transparent container with water until it’s just touching the bottom of the rockwool cube. The water level should not be so high that the rockwool cube is submerged.
9. Add the hydroponic nutrients to the water following the manufacturer's instructions for the proper concentration.
10. Test the pH of your nutrient solution. Most plants prefer a pH range between 5.5 and 6.5 for hydroponic systems. Adjust the pH if necessary using your pH Up/Down solution.
11. Place the rockwool cubes with your seedlings into the non-transparent container, ensuring that the roots are in the nutrient solution but the rockwool cube is not submerged.
12. Place the container in a location with a sufficient light source. If sunlight is not available or sufficient, set up your grow lights.
13. As the plant grows, the roots will reach down into the nutrient solution. The water level will also drop, leaving an air gap for the roots to access oxygen.
14. Monitor the plant growth, ensuring the roots are moist and the plants are healthy. If the water level gets too low (less than a quarter of the original volume), add more nutrient solution, ensuring you maintain the air gap.
15. Harvest the plant when it reaches the desired size. For continuous growing, start new seeds in rockwool cubes when your current plant is nearing readiness for harvest.

The Kratky method is a **passive** hydroponic system, and one of its key aspects is **not to refill** the nutrient solution to the top after the plant has started growing. This is because the plant requires an air gap to breathe, which is created naturally as the plant consumes the nutrient solution.

![image](https://github.com/kevingduck/kratky/assets/2180038/d05c0a8e-90ca-439f-8900-2d85fbd9bfbb)
