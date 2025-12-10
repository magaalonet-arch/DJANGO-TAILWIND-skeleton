# Quick Start Guide

Get up and running with Django + Tailwind CSS in under 5 minutes!

## Prerequisites

- Python 3.12+
- Node.js 20+
- npm 10+

## Installation (3 steps)

### 1. Install Dependencies

```bash
# Python dependencies
pip install -r requirements.txt

# Node dependencies
npm install
```

### 2. Build Tailwind CSS

```bash
npm run build
```

### 3. Set Up Django

```bash
# Run migrations
python manage.py migrate

# (Optional) Create admin user
python manage.py createsuperuser
```

## Run the Development Server

Open **two terminals**:

**Terminal 1:**
```bash
python manage.py runserver
```

**Terminal 2:**
```bash
npm run dev
```

Visit: http://127.0.0.1:8000/

## What's Next?

- Check out `templates/index.html` to see Tailwind in action
- Edit `core/views.py` to add new views
- Modify `tailwind.config.js` to customize your design
- Read the full [README.md](README.md) for detailed documentation

## Tips

- The Tailwind watch mode (`npm run dev`) automatically rebuilds CSS when you save templates
- Use `python manage.py runserver` for Django hot reload
- Check `/admin` for the Django admin interface
- All Tailwind utility classes are available - see [Tailwind Docs](https://tailwindcss.com/docs)

## Troubleshooting

**CSS not loading?**
- Run `npm run build` to generate the CSS file
- Check that `static/css/output.css` exists

**Port already in use?**
- Use `python manage.py runserver 8001` to use a different port

**Need help?**
- Check the [README.md](README.md) for detailed documentation
- Review the [Django docs](https://docs.djangoproject.com/)
- Browse [Tailwind CSS docs](https://tailwindcss.com/docs)
