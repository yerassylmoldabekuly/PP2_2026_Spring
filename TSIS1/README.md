# TSIS1: PhoneBook — Extended Contact Management

This project extends the PhoneBook application from previous practices with a richer data model, advanced console features, and additional PostgreSQL procedures and functions.

## Features

### Database Schema
- `contacts` table with:
  - name
  - email
  - birthday
  - group reference
  - created_at
- `groups` table for contact categories:
  - Family
  - Work
  - Friend
  - Other
- `phones` table for multiple phone numbers per contact
  - one-to-many relationship with contacts
  - phone type: `home`, `work`, `mobile`

### Console Features
- Add contacts with multiple phone numbers
- Filter contacts by group
- Search contacts by partial email
- Sort contacts by:
  - name
  - birthday
  - date added
- Paginated navigation with:
  - `next`
  - `prev`
  - `quit`

### Import / Export
- Export all contacts to JSON
- Import contacts from JSON
  - duplicate handling: `skip` or `overwrite`
- Import contacts from CSV with extended fields:
  - email
  - birthday
  - group
  - phone type

### Stored Procedures / Functions
- `add_phone(p_contact_name, p_phone, p_type)`
- `move_to_group(p_contact_name, p_group_name)`
- `search_contacts(p_query)`  
  searches by:
  - contact name
  - email
  - group
  - all phone numbers

## Repository Structure

```text
TSIS1/
├── phonebook.py
├── config.py
├── connect.py
├── schema.sql
├── procedures.sql
└── contacts.csv