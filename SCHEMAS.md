# SCHEMAS

## Database: Supabase (PostgreSQL)

### Table: `inquiries`
Stores user submissions from contact forms.

| Column Name      | Data Type | Constraints | Description |
|------------------|-----------|-------------|-------------|
| `id`             | int8      | Primary Key | Unique identifier for the inquiry. |
| `created_at`     | timestamptz| Default: now()| Timestamp of submission. |
| `full_name`      | text      | Not Null    | Name of the lead. |
| `email_address`  | text      | Not Null    | Contact email. |
| `phone_number`   | text      | Optional    | Contact phone number. |
| `company_name`   | text      | Optional    | Organization name. |
| `project_interest`| text     | Optional    | Selected service of interest. |

## JSON Objects

### Form Submission Payload
Structure of the object sent to Supabase:
```json
{
  "full_name": "string",
  "email_address": "string",
  "phone_number": "string",
  "company_name": "string",
  "project_interest": "string"
}
```
