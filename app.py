from flask import Flask, render_template, redirect, url_for, request
from models import db, Bin, Plant, Log
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kratky_garden.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# List of top 15 garden plants with estimated harvest days and amounts (lbs)
TOP_PLANTS = [
    {"name": "Basil", "days_to_harvest": 30, "expected_harvest_amount": 0.5},
    {"name": "Lettuce", "days_to_harvest": 20, "expected_harvest_amount": 0.3},
    {"name": "Spinach", "days_to_harvest": 25, "expected_harvest_amount": 0.4},
    {"name": "Kale", "days_to_harvest": 30, "expected_harvest_amount": 0.5},
    {"name": "Cilantro", "days_to_harvest": 20, "expected_harvest_amount": 0.3},
    {"name": "Arugula", "days_to_harvest": 20, "expected_harvest_amount": 0.3},
    {"name": "Mint", "days_to_harvest": 30, "expected_harvest_amount": 0.5},
    {"name": "Chives", "days_to_harvest": 30, "expected_harvest_amount": 0.2},
    {"name": "Parsley", "days_to_harvest": 40, "expected_harvest_amount": 0.4},
    {"name": "Thyme", "days_to_harvest": 40, "expected_harvest_amount": 0.2},
    {"name": "Oregano", "days_to_harvest": 40, "expected_harvest_amount": 0.3},
    {"name": "Pepper", "days_to_harvest": 60, "expected_harvest_amount": 0.8},
    {"name": "Tomato", "days_to_harvest": 60, "expected_harvest_amount": 1.0},
    {"name": "Cucumber", "days_to_harvest": 50, "expected_harvest_amount": 0.7},
    {"name": "Strawberry", "days_to_harvest": 45, "expected_harvest_amount": 0.5}
]


# Home Route
@app.route('/')
def index():
    bins = Bin.query.all()
    logs = Log.query.order_by(Log.timestamp.desc()).all()
    total_bins = len(bins)
    total_plants = sum(len(bin.plants) for bin in bins)
    available_spaces = sum(bin.plant_spaces - len(bin.plants) for bin in bins)
    now = datetime.now().date()
    upcoming_harvests = Plant.query.filter(Plant.expected_harvest_date >= now).order_by(Plant.expected_harvest_date).limit(5).all()
    overdue_harvests = Plant.query.filter(Plant.expected_harvest_date < now, Plant.status != 'Harvested').all()

    return render_template('index.html', total_bins=total_bins, total_plants=total_plants,
                           available_spaces=available_spaces, upcoming_harvests=upcoming_harvests,
                           overdue_harvests=overdue_harvests, logs=logs)


# Bins Routes
@app.route('/bins')
def bins():
    bins = Bin.query.all()
    now = datetime.now().date()
    return render_template('bins.html', bins=bins, now=now)


@app.route('/bins/new', methods=['GET', 'POST'])
def new_bin():
    if request.method == 'POST':
        name = request.form['name']
        gallons = request.form['gallons']
        plant_spaces = request.form['plant_spaces']
        new_bin = Bin(name=name, gallons=gallons,
                      plant_spaces=plant_spaces)
        db.session.add(new_bin)
        db.session.commit()
        return redirect(url_for('bins'))
    return render_template('new_bin.html')

@app.route('/bins/<int:bin_id>')
def bin_detail(bin_id):
    bin = Bin.query.get_or_404(bin_id)
    now = datetime.now().date()
    return render_template('bin_detail.html', bin=bin, now=now)

@app.route('/bins/<int:bin_id>/edit', methods=['GET', 'POST'])
def edit_bin(bin_id):
    bin = Bin.query.get_or_404(bin_id)
    if request.method == 'POST':
        bin.name = request.form['name']
        bin.gallons = request.form['gallons']
        bin.plant_spaces = request.form['plant_spaces']
        db.session.commit()
        return redirect(url_for('bin_detail', bin_id=bin.id))
    return render_template('edit_bin.html', bin=bin)

@app.route('/bins/<int:bin_id>/delete', methods=['POST'])
def delete_bin(bin_id):
    bin = Bin.query.get_or_404(bin_id)
    db.session.delete(bin)
    db.session.commit()
    return redirect(url_for('bins'))

# Plants Routes
@app.route('/bins/<int:bin_id>/add_plant', methods=['GET', 'POST'])
def add_plant(bin_id):
    bin = Bin.query.get_or_404(bin_id)
    if request.method == 'POST':
        plant_type = request.form['plant_type']
        name = request.form['name'] if plant_type == 'Other' else plant_type
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        expected_days = int(request.form['expected_days'])
        expected_harvest_date = start_date + timedelta(days=expected_days)
        expected_harvest_amount = float(request.form['expected_harvest_amount'])
        notes = request.form['notes']
        number_of_plants = int(request.form['number_of_plants'])

        for _ in range(number_of_plants):
            new_plant = Plant(
                name=name,
                bin_id=bin.id,
                start_date=start_date,
                expected_harvest_date=expected_harvest_date,
                expected_harvest_amount=expected_harvest_amount,
                status='Growing',
                notes=notes
            )
            db.session.add(new_plant)

        db.session.commit()
        return redirect(url_for('bin_detail', bin_id=bin.id))

    return render_template('add_plant.html', bin=bin, top_plants=TOP_PLANTS)


@app.route('/plants/<int:plant_id>')
def plant_detail(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    return render_template('plant_detail.html', plant=plant)

@app.route('/plants/<int:plant_id>/edit', methods=['GET', 'POST'])
def edit_plant(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    if request.method == 'POST':
        plant.name = request.form['name']
        plant.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        plant.expected_harvest_date = datetime.strptime(request.form['expected_harvest_date'], '%Y-%m-%d')
        plant.expected_harvest_amount = request.form['expected_harvest_amount']
        plant.status = request.form['status']
        plant.notes = request.form['notes']
        db.session.commit()
        return redirect(url_for('plant_detail', plant_id=plant.id))
    return render_template('edit_plant.html', plant=plant)

@app.route('/plants/<int:plant_id>/delete', methods=['POST'])
def delete_plant(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    bin_id = plant.bin_id
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('bin_detail', bin_id=bin_id))

@app.route('/logs/new', methods=['GET', 'POST'])
def add_log():
    bins = Bin.query.all()
    if request.method == 'POST':
        description = request.form['description']
        timestamp = datetime.strptime(request.form['timestamp'], '%Y-%m-%d')
        bin_ids = request.form.getlist('bin_ids')
        bin_ids_str = ','.join(bin_ids)

        new_log = Log(description=description, timestamp=timestamp, bin_ids=bin_ids_str)
        db.session.add(new_log)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_log.html', bins=bins)


if __name__ == '__main__':
    app.run(debug=True)
