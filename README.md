# 🍽️ Dynamic Recipe Generator (DRG) 5.0

[![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AI Powered](https://img.shields.io/badge/AI-Powered-ff6600.svg)](https://huggingface.co/)

An AI-powered recipe generation platform built by **ALPHA SQUAD** that helps users discover, save, and plan their meals intelligently.

## 🚀 Features

### Current Features (DRG 5.0)
- 🍽️ **AI Recipe Generation** - Generate recipes using Hugging Face AI models
- ❤️ **Favorites System** - Save and manage your favorite recipes
- 📜 **Recipe History** - Auto-tracking of all generated recipes with timestamps
- 🧠 **AI Meal Planner** - Generate complete 7-day meal plans with dietary preferences
- 📥 **PDF Export** - Download recipes as formatted PDFs
- 🛒 **Shopping Lists** - Auto-generated ingredient lists
- 🎉 **Seasonal Recipes** - Explore recipes based on festivals and regions
- 🔍 **Advanced Search** - Filter by dietary preferences and cuisine types
- 🌶️ **Flavor Twist** - Modify recipes to be spicy, healthy, or cheesy

## 📋 Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Team](#team)
- [Changelog](#changelog)
- [License](#license)

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Hugging Face API key (free tier available)

### Setup Steps

1. **Clone the repository**
   ```bash
   cd dynamic_recipe_generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Open `main.py`
   - Replace the placeholder on line 16:
     ```python
     HUGGINGFACE_API_KEY = "your_actual_api_key_here"
     ```
   - Get a free API key at: https://huggingface.co/settings/tokens

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**
   - Open your browser and navigate to: http://127.0.0.1:8000

## ⚙️ Configuration

### Environment Variables
You can set the following in `main.py`:
- `HUGGINGFACE_API_KEY` - Your Hugging Face API key (required)
- `HF_MODEL` - The model to use (default: "HuggingFaceH4/zephyr-7b-beta")

### Data Storage
- **Development**: Uses browser localStorage for favorites, history, and meal plans
- **Production**: Ready for PostgreSQL/MySQL integration (see upgrade path below)

## 🎯 Usage

### Generating a Recipe
1. Navigate to the **Recipes** page
2. Enter ingredients or a recipe name
3. (Optional) Select dietary preferences or cuisine type
4. Click "Search Recipe"
5. Save to favorites or add ingredients to shopping list

### Using the Meal Planner
1. Go to **Meal Planner** page
2. Select dietary preference (Vegan, Keto, etc.)
3. Choose cuisine type (optional)
4. Click "Generate My Meal Plan"
5. Print or save the 7-day plan

### Managing Favorites
1. Generate a recipe you like
2. Click "❤️ Save to Favorites"
3. Access saved recipes anytime from the **Favorites** page
4. Click on any favorite to regenerate it

### Viewing History
- All generated recipes are automatically saved
- View up to 50 recent recipes in **History**
- Click any recipe to regenerate it
- Clear history anytime

## 📁 Project Structure

```
dynamic_recipe_generator/
├── main.py                 # FastAPI application & routes
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css          # Centralized stylesheet
├── templates/
│   ├── index.html         # Home page
│   ├── search.html        # Recipe search & generation
│   ├── favorites.html     # Saved recipes
│   ├── history.html       # Recipe history
│   ├── meal_planner.html  # AI meal planning
│   ├── shopping.html      # Shopping list
│   ├── about.html         # About & team info
│   ├── contact.html       # Contact form
│   ├── seasonal.html      # Seasonal recipes
│   └── accessories.html   # Kitchen accessories
└── README.md              # This file
```

## 👥 Team - ALPHA SQUAD

- **Chauhan Karm** - Leader, DB/Server Manager & Backend Developer
- **Desai Sahil** - Co-leader & Backend Developer
- **Patel Devang** - Planning & Communication Lead
- **Prajapati Ronak** - Frontend Developer

## 📝 Changelog

### Version 5.0.0 - November 29, 2025

#### 🎨 UI/UX Overhaul
**Changes made by: Karm Chauhan**  
**Date & Time: November 29, 2025 at 12:37 AM IST**

- ✅ Centralized all styles to `static/style.css`
- ✅ Implemented modern design system with:
  - Deep Orange primary color (#ff6600)
  - Dark theme with glassmorphism effects
  - Poppins font family from Google Fonts
  - Smooth animations (fade-in, zoom, hover effects)
- ✅ Updated all 10 HTML templates with consistent styling
- ✅ Redesigned footer across all pages:
  - Removed social media links (email, GitHub, Instagram)
  - Simplified to show: Brand + About/Contact + Copyright
  - Modern gradient background with orange accent border

#### 🆕 New Features (DRG 5.0 MVP)
**Changes made by: Karm Chauhan**  
**Date & Time: November 29, 2025 at 12:37 AM IST**

- ✅ **Favorites System**
  - Created `templates/favorites.html` page
  - Added "Save to Favorites" button in search page
  - Implemented localStorage-based storage
  - Duplicate check to prevent saving same recipe twice
  - Remove and regenerate functionality

- ✅ **Recipe History**
  - Created `templates/history.html` page
  - Auto-save every generated recipe with timestamp
  - Stores last 50 recipes automatically
  - Click-to-regenerate functionality
  - Clear all history option

- ✅ **AI Meal Planner**
  - Created `templates/meal_planner.html` page
  - Added `/api/generate-meal-plan` API endpoint
  - 7-day meal plan generation
  - Filters for dietary preferences and cuisine types
  - Print and save functionality

- ✅ **Enhanced Search Features**
  - Dietary preferences dropdown
  - Cuisine type selector
  - "Surprise Me" random recipe button
  - "What's in my Fridge?" search
  - "Flavor Twist" buttons (Spicy, Healthy, Cheesy)

#### 🔧 Backend Updates
**Changes made by: Karm Chauhan**  
**Date & Time: November 29, 2025 at 12:37 AM IST**

- ✅ Added new routes in `main.py`:
  - `GET /favorites` - Favorites page
  - `GET /history` - History page
  - `GET /meal-planner` - Meal planner page
  - `POST /api/generate-meal-plan` - Meal plan generation API

- ✅ Updated navigation across all pages to include:
  - 📅 Meal Planner
  - ❤️ Favorites
  - 📜 History

#### 🐛 Bug Fixes
**Changes made by: Karm Chauhan**  
**Date & Time: November 29, 2025 at 12:37 AM IST**

- ✅ Fixed duplicate HTML content in `index.html`
- ✅ Fixed duplicate HTML content in `about.html`
- ✅ Corrected footer styling across all templates
- ✅ Fixed navigation links on homepage

---

### Version 4.0.0 - Previous Release
- Initial release with basic recipe generation
- PDF export functionality
- Shopping list generation
- Seasonal recipes
- Kitchen accessories recommendations

## 🔮 Roadmap (DRG 6.0)

Planned features for future releases:
- 🗣️ Voice-Activated Cooking Assistant
- 🔐 User Login System with database backend
- 📧 Recipe Scheduler with email integration
- 🏆 Recipe Ratings & Reviews
- 📱 Mobile App (iOS & Android)
- 💾 PostgreSQL database integration
- 🌍 Multi-language support

## 📈 Upgrade Path to Production

When ready for production deployment:
1. Set up PostgreSQL/MySQL database
2. Create database models (User, Recipe, Favorite, MealPlan)
3. Implement JWT-based authentication
4. Migrate from localStorage to database API calls
5. Add email service (SendGrid/AWS SES)
6. Set up proper environment variable management
7. Configure CORS for specific domains
8. Add rate limiting and security headers

## 🔒 Security Notes

- Change `HUGGINGFACE_API_KEY` from placeholder to actual key
- Update CORS settings in production (currently allows all origins)
- Implement proper session management for production
- Add input validation and sanitization
- Use HTTPS in production

## 📄 License

© 2025 Dynamic Recipe Generator - ALPHA SQUAD. All rights reserved.

## 🤝 Contributing

This project is developed and maintained by ALPHA SQUAD. For questions or suggestions, please contact the team through the Contact page.

## 📞 Support

- **Email**: support@drgfoods.org
- **Website**: http://127.0.0.1:8000 (local development)

---

**Built with ❤️ by ALPHA SQUAD**  
*Making cooking smarter, one recipe at a time.*
