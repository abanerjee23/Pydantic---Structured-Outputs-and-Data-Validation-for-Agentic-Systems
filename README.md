# Pydantic Input Validation

A simple and clean input validation system using Pydantic models, designed for user/agent interaction pipelines.

## Features

- **Email Validation**: Built-in email format validation using `EmailStr`
- **Mandatory Fields**: All input fields are required (strict validation)
- **Query Constraints**: Query field enforces 5-100 character length
- **Detailed Error Messages**: Clear error reporting with field names and validation messages
- **Agentic Intake Flow**: Customer query form powered by OpenAI Agents, Pydantic validation, and Gradio

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

# Example - Valid Input
test = {
    'name': "Abhinav",
    'age': 34,
    'email': 'banerjeeabhinav@outlook.com',
    'query': "I have forgotten my password"
}
result = validate_input(test)

# Example - Invalid Input (demonstrates error handling)
sample_input = {
    'name': "Sam",
    'age': 34,
    'email': 'samjohn@outlook-com',
    'query': "I have forgotten my password and will need your help to reset it"
}
result = validate_input(sample_input)
# Returns: ['email:value is not a valid email address [type=value_error, input_value=\'samjohn@outlook-com\', input_type=str]']
```

## Customer Query Intake Demo

The `customer-query-project.ipynb` notebook demonstrates a simple production-style intake flow:

1. A Gradio form collects the customer's name, email, and query.
2. A validation agent calls a Pydantic-backed function tool.
3. A final reviewer agent tells the customer whether the query has been accepted for processing or which details need correction.

On successful validation, the user-facing response is:

```text
Your query has been accepted and is under processing.
```

## Installation

```bash
uv pip install -r requirements.txt
```

## Requirements

- Python 3.7+
- Pydantic 2.0+
- OpenAI Agents SDK
- Gradio

## Project Structure

- `pydantic-project.ipynb` - Jupyter notebook with validation implementation and test case
- `customer-query-project.ipynb` - Customer query intake workflow with agents, Pydantic validation, and Gradio UI

## License

MIT
