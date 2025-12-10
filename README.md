# Django + Tailwind CSS Skeleton

A clean, modern starter template for Django 5 projects with integrated Tailwind CSS workflow. This skeleton uses Node-based Tailwind (not django-tailwind) for full Django 5+ compatibility and a decoupled frontend build process.

## 🚀 Features

- **Django 5.2.9**: Latest Django with modern Python support
- **Tailwind CSS 3.x**: Utility-first CSS framework with Node-based build
- **Hot Reload**: Automatic CSS rebuilding during development
- **Clean Structure**: Minimal, flexible foundation for rapid development
- **Production Ready**: Optimized build process with minification

## 📋 Requirements

- Python 3.12+ (Designed for 3.14.0)
- Node.js 20+ (Designed for v22.21.1)
- npm 10+ (Designed for 10.9.4)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd DJANGO-TAILWIND-skeleton
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Set Up Node Environment

```bash
# Install Node dependencies
npm install
```

### 4. Build Tailwind CSS

```bash
# Initial build
npm run build
```

### 5. Set Up Django

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 6. Configure Environment Variables (Optional)

For production or custom configuration:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and set your SECRET_KEY and other settings
```

**Important for Production:** Always set a unique `SECRET_KEY` in your environment variables or `.env` file. Never use the default key in production!

## 🏃 Development Workflow

### Running the Development Server

You'll need **two terminal windows**:

**Terminal 1 - Django Server:**
```bash
python manage.py runserver
```

**Terminal 2 - Tailwind Watch Mode:**
```bash
npm run dev
```

The Tailwind watch mode will automatically rebuild your CSS when you modify templates or add new Tailwind classes.

Visit `http://127.0.0.1:8000/` to see your application.

## 📁 Project Structure

```
DJANGO-TAILWIND-skeleton/
├── config/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Main Django app
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/              # Global templates
│   ├── base.html
│   └── index.html
├── static/
│   ├── css/
│   │   ├── input.css      # Tailwind source
│   │   └── output.css     # Generated CSS (gitignored)
│   └── js/
├── manage.py
├── requirements.txt        # Python dependencies
├── package.json           # Node dependencies
├── tailwind.config.js     # Tailwind configuration
└── postcss.config.js      # PostCSS configuration
```

## 🎨 Using Tailwind CSS

### In Templates

Simply use Tailwind utility classes in your HTML:

```html
<div class="flex items-center justify-center min-h-screen bg-gray-100">
    <h1 class="text-4xl font-bold text-blue-600">Hello, Tailwind!</h1>
</div>
```

### Customizing Tailwind

Edit `tailwind.config.js` to customize your design system:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#your-color',
      },
    },
  },
}
```

## 📦 Building for Production

### Environment Configuration

Before deploying to production:

1. **Set Environment Variables:**
   ```bash
   export SECRET_KEY="your-unique-secret-key-here"
   export DEBUG="False"
   export ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
   ```

2. **Or use a `.env` file** (recommended):
   ```bash
   cp .env.example .env
   # Edit .env with your production settings
   ```

3. **Generate a secure SECRET_KEY:**
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

### Build and Deploy

```bash
# Build optimized CSS
npm run build

# Collect static files
python manage.py collectstatic --noinput
```

**Security Reminder:** Never commit your `.env` file or expose your `SECRET_KEY` in version control!

## 🔍 Key Configuration Files

### Django Settings (`config/settings.py`)

- `STATICFILES_DIRS`: Points to `static/` for development
- `STATIC_ROOT`: Points to `staticfiles/` for production
- `TEMPLATES['DIRS']`: Includes global `templates/` directory
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`: Configured via environment variables (with safe defaults for development)

### Tailwind Config (`tailwind.config.js`)

- `content`: Paths to scan for Tailwind classes
- `theme`: Customize design tokens
- `plugins`: Add Tailwind plugins

### Package.json Scripts

- `npm run dev`: Watch mode for development
- `npm run build`: Minified production build

## 🌟 Why This Approach?

This skeleton uses **Node-based Tailwind** instead of the `django-tailwind` package because:

1. **Django 5+ Compatibility**: Full support for latest Django versions
2. **Decoupled Architecture**: Frontend tooling independent of Django
3. **Standard Workflow**: Uses official Tailwind CLI
4. **Flexibility**: Easy to integrate additional Node-based tools
5. **Performance**: Faster builds and better optimization

## 🛠️ Common Tasks

### Adding a New App

```bash
python manage.py startapp myapp
```

Don't forget to:
1. Add it to `INSTALLED_APPS` in `settings.py`
2. Include its URLs in `config/urls.py`

### Creating New Templates

Place templates in:
- `templates/` for global templates
- `app_name/templates/app_name/` for app-specific templates

### Adding Custom CSS

You can add custom styles in `static/css/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700;
  }
}
```

## 🐛 Troubleshooting

### CSS Not Loading?

1. Ensure `npm run build` or `npm run dev` was run
2. Check that `output.css` exists in `static/css/`
3. Verify Django's dev server is running

### Tailwind Classes Not Working?

1. Check `tailwind.config.js` content paths
2. Ensure template files are in the correct location
3. Restart the Tailwind watch process

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Django + Tailwind Best Practices](https://tailwindcss.com/docs/guides/django)

