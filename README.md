# GigBoard API – Campus Freelance Marketplace

## Project Overview
**GigBoard API** is a localized freelance marketplace API designed specifically for the university ecosystem. It connects students offering services such as coding, laundry, graphic design, and printing with other students who need these services. 

## Problem Statement
Campus commerce is currently fragmented, relying on WhatsApp statuses, word of mouth, and physical notice boards. This makes it difficult to find verified service providers or track the progress of a job. There is no centralized platform to manage campus gigs effectively. 

## Goal
The goal of **GigBoard API** is to formalize campus "hustle culture" by providing a RESTful API that manages the full lifecycle of a campus gig—from posting a service to booking, tracking status, and reviewing completed work.

## Features (Planned)
- **Service Posting**: Students can offer their services with descriptions, pricing, and availability.  
- **Job Booking**: Students in need of a service can browse and book gigs.  
- **Status Tracking**: Both parties can track the progress of ongoing jobs.  
- **Reviews & Ratings**: Users can provide feedback after a job is completed.  

## Tech Stack (Suggested)
- **Backend**: Python with Django REST Framework 
- **Database**: PostgreSQL 
- **Authentication**: JWT-based secure authentication  
- **Deployment**: Render

## Target Users
- University students offering services  
- University students seeking services  

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/Scripts/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Run server: `python manage.py runserver`

## API Endpoints
- `POST /api/auth/register/` - Create account
- `GET /api/services/` - List gigs
- `POST /api/orders/` - Place an order

---

*GigBoard API aims to make campus freelancing transparent, organized, and reliable, empowering students to monetize their skills and find trusted services on campus.*
