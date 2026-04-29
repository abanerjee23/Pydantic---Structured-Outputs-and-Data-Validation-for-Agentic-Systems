# Pydantic Input Validation

A simple and clean input validation system using Pydantic models, designed for user/agent interaction pipelines.

## Features

- **Email Validation**: Built-in email format validation using `EmailStr`
- **Mandatory Fields**: All input fields are required (strict validation)
- **Query Constraints**: Query field enforces 5-100 character length
- **Detailed Error Messages**: Clear error reporting with field names and validation messages

## Usage

```python
from pydantic import BaseModel, ValidationError, EmailStr, Field

class UserInput(BaseModel):
    name: str
    age: int
    email: EmailStr
    query: str = Field(..., min_length=5, max_length=100)

def validate_input(agent_input: dict):
    try:
        validated = UserInput(**agent_input)
        print("Input has been successfully validated!")
        return validated
    except ValidationError as e:
        errors = []
        for error in e.errors():
            errors.append(f"{error['loc'][0]}:{error['msg']}")
        return errors

# Example
test = {
    'name': "Abhinav",
    'age': 34,
    'email': 'banerjeeabhinav@outlook.com',
    'query': "I have forgotten my password"
}
result = validate_input(test)
```

## Installation

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.7+
- Pydantic 2.0+

## Project Structure

- `pydantic-project.ipynb` - Jupyter notebook with validation implementation and test case

## License

MIT
