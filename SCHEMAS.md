# SCHEMAS

## Database: Supabase (PostgreSQL)

### Table: `inquiries`
Stores user submissions from contact forms.

| Column Name      | Data Type | Constraints | Description |
|------------------|-----------|-------------|-------------|
| `id`             | uuid      | Primary Key | Unique identifier for the inquiry. |
| `created_at`     | timestamp | Default: now()| Timestamp of submission. |
| `full_name`      | text      | Nullable    | Name of the contact. |
| `phone_number`   | text      | Nullable    | Contact phone number. |
| `company_name`   | text      | Nullable    | Organization name. |

## JSON Objects

### Form Submission Payload
Structure of the object sent to Supabase:
```json
{
  "full_name": "string",
  "phone_number": "string",
  "company_name": "string"
}
```
