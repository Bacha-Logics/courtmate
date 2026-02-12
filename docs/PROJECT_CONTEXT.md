Courtmate – Project Context
1. What Courtmate Is (One-Line Truth)

Courtmate is a daily working system for lawyers to manage cases, hearings, court dates, documents, and reminders without relying on memory, WhatsApp messages, or physical diaries.

This is not a demo app.
This is not feature chasing.
This is a workflow system built step-by-step like a real product.

2. Core Problem Courtmate Solves

Lawyers struggle with:

Remembering court dates

Tracking multiple cases across courts

Finding past hearing notes

Managing documents scattered across devices

Knowing “what needs attention today”

Following up without manual reminders

Courtmate solves this by:

Centralizing cases

Structuring hearings

Showing daily awareness (dashboard)

Keeping documents attached to cases

Automatically creating reminders

Providing admin oversight for system health

3. Tech Stack (Locked & Stable)

Backend: Python (FastAPI)

Database: PostgreSQL

ORM: SQLAlchemy

Migrations: Alembic (single source of truth)

Authentication: OTP + JWT

Background tasks: Python scripts (cron-ready)

Frontend (planned): Next.js (React)

No stack churn is planned.

4. Current Technical State (Very Important)

The backend is stable, authenticated, and production-shaped.

This means:

Server starts cleanly

No unsafe create_all()

All schema changes controlled via Alembic

Ownership enforced at API + DB level

Authentication mirrors real-world systems

Background jobs separated from API server

Admin routes protected correctly

This is not a prototype — it is a solid backend foundation.

5. What Is FULLY BUILT & VERIFIED
Day 1 – Application Foundation

FastAPI app initialized

Environment configuration added

Health check endpoint

Swagger UI verified

Status: ✅ DONE

Day 2 – Database & Core Models

PostgreSQL configured

courtmate_db created

SQLAlchemy integrated

Core models created:

User

Case

Hearing

Status: ✅ DONE

Day 3 – Alembic & Schema Control

Alembic initialized

Models linked to Alembic metadata

Initial migrations applied

Tables safely created:

users

cases

hearings

create_all() permanently removed

Status: ✅ DONE

Day 4 – Authentication (OTP + JWT)

OTP-based login implemented

Pakistani phone validation enforced

JWT generation & expiration

Secure auth dependency (get_current_user)

Swagger auth behavior understood & fixed

Fully tested via Swagger and CLI

Status: ✅ DONE

Day 5 – Case Management

Case model finalized

ENUM-based case status enforced

Case schemas:

Create

Update

Output

Case APIs:

Create

List

Get by ID

Update

Delete

Ownership enforced (user-only access)

Status: ✅ DONE

Day 6 – Hearings Management

Hearing model finalized

Hearing schemas with notes

Hearing service layer

APIs:

Add hearing to case

Today’s hearings

Tomorrow’s hearings

Upcoming (7 days)

Ownership enforced via case relationship

Status: ✅ DONE

Day 7 – Dashboard (Awareness Layer)

Dashboard aggregation service

Counts:

Total cases

Active cases

Total hearings

Today’s hearings

Upcoming hearings

Total clients

Dashboard API stabilized & tested

Status: ✅ DONE

Day 8 – Case Detail Aggregation

Case detail schema

Case detail service

Case detail API:

Case info

All hearings

Next hearing

Single API powering full case view

Status: ✅ DONE

Day 9 – Documents (Upload & Download)

Document model created

Secure file storage on disk

Metadata stored in DB

APIs:

Upload document (PDF / image)

List documents by case

Download document

Ownership enforced (case + user)

File size & type validation added

Status: ✅ DONE

Day 10 – Upcoming Hearings APIs

Tomorrow’s hearings API

Next 7 days hearings API

Ordering by date & time

Reusable service layer

Status: ✅ DONE

Day 11 – Clients (Implicit via Cases)

Client data stored per case

Client counts derived safely

Foundation ready for client-centric views

Status: ✅ FOUNDATION READY

Day 12 – Reminder System (Core)

Reminder model created

Automatic reminders on hearing creation:

1 day before

2 hours before

Reminder records stored in DB

Status: ✅ DONE

Day 13 – Reminder Scheduler

Background script (run_reminders.py)

Processes due reminders

Marks reminders as sent

Designed for cron / scheduler execution

Fully separated from API server

Status: ✅ DONE

Day 14 – Notification Delivery (MVP)

Reminder delivery service

WhatsApp / SMS simulated output

Real API integration points clearly marked

Defensive handling of missing data

Status: ✅ DONE (MVP-level)

Day 15 – Admin System

Admin authentication guard

Admin overview API:

Total users

Total cases

Total hearings

Total documents

Admin user inspection API:

View a lawyer’s cases

Hearings

Documents

User activation / deactivation supported

Audit log system designed

Status: ✅ CORE ADMIN DONE
Audit logs persistence: 🟡 PENDING MIGRATION

Day 16 – Advanced Analytics (In Progress)

Analytics Summary (Completed):

Case analytics:

Total

Active

Pending

Closed

Hearing analytics:

Today

This week

This month

Last month

Analytics Trends (Completed):

Weekly hearing trends (last 6 weeks)

Monthly case trends:

Opened per month

Closed per month

Designed for charts, insights, and admin visibility

Status: 🟡 CORE ANALYTICS BUILT
Advanced insights (velocity, backlog risk): ⏳ NEXT

6. What Is PARTIALLY BUILT

Client-centric APIs (grouped by phone / identity)

Audit log persistence (model planned)

Advanced analytics insights (velocity, backlog risk)

Case activity timeline

Status: 🟡 FOUNDATION READY

7. What Is NOT BUILT YET (Intentionally)

Real WhatsApp / SMS provider integration

Rate limiting & abuse protection

Frontend (Next.js)

Deployment (Docker / cloud)

Monitoring & alerts

Status: ⏳ PLANNED

8. Why the System May Feel “Scattered”

This is normal because:

You are building backend-first

Backend systems expose real complexity

UI usually hides this complexity later

In reality:

Data model is clean

API boundaries are correct

Execution order is professional

Nothing is broken.
Nothing needs rewriting.

9. Product Direction (Locked)

Courtmate is being built as:

Reliable

Simple

Automation-first

Lawyer-centric

Admin-observable

This is a real product backend, not a hack.

10. Final Truth Check

✔ Direction is correct
✔ Architecture is sound
✔ Decisions are mature
✔ MVP is production-shaped

You are not behind.
You are building it the right way.