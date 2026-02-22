#!/bin/bash
# Great Chat - Local Development Setup Script

echo "=========================================="
echo "  Great Chat - Local Setup"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Install dependencies
echo -e "${YELLOW}📦 Installing Python dependencies...${NC}"
pip install -r requirements.txt

echo ""
echo -e "${YELLOW}🗄️  Running database migrations...${NC}"
python manage.py migrate

echo ""
echo -e "${YELLOW}👥 Creating demo users...${NC}"
python manage.py create_demo_users --clear

echo ""
echo -e "${YELLOW}📁 Collecting static files...${NC}"
python manage.py collectstatic --noinput

echo ""
echo "=========================================="
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "=========================================="
echo ""
echo "📝 Demo User Accounts:"
echo "   • alice / demo1234"
echo "   • bob / demo1234"
echo "   • charlie / demo1234"
echo "   • diana / demo1234"
echo "   • admin / admin1234 (superuser)"
echo ""
echo "🚀 Starting development server..."
echo "   Access at: http://localhost:8000"
echo ""
echo "=========================================="
echo ""

# Start the development server
python manage.py runserver
