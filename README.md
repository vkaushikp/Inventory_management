# Inventory Management System

A brutalist-styled Django application for managing inventory items and suppliers. Built with a focus on simplicity and usability.

## Features

- **Inventory Management**
	- Track item quantities and costs
	- Set reorder levels with low stock alerts
	- View total value calculations
	- Detailed item history

- **Supplier Management**
	- Maintain supplier contact information
	- Track items per supplier
	- Full CRUD operations for suppliers

- **Brutalist Design**
	- High contrast black and white interface
	- Bold borders and rounded corners
	- Clear typography and spacing
	- Responsive layout

## Requirements

- Python 3.8+
- Django 5.1+
- SQLite (default database)

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd inventory-management
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install django
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## Usage

### Managing Inventory

1. Add new items through the "Add Item" button
2. Set quantities, costs, and reorder levels
3. Monitor stock levels with automatic alerts
4. View detailed item information

### Managing Suppliers

1. Add suppliers with contact details
2. Associate items with suppliers
3. Track supplier-specific inventory
4. Manage supplier information

## Structure

```
inventory_management/
├── inventory/
│   ├── models.py         # Data models
│   ├── views.py          # View logic
│   ├── admin.py          # Admin interface
│   └── templates/        # HTML templates
├── static/               # Static assets
└── manage.py            # Django management
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.