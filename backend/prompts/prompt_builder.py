import textwrap


def build_testcase_prompt(
    repository_context: dict,
    file_name: str,
    code: str,
):
    """
    Builds a concise, endpoint-focused prompt for AI test case generation.
    """

    endpoint = repository_context.get("current_endpoint")

    models = repository_context.get(
        "models",
        {},
    )

    database_analysis = repository_context.get(
        "database_analysis",
        {},
    )

    authentication_analysis = repository_context.get(
        "authentication_analysis",
        {},
    )

    # ---------------------------------------------------------
    # Endpoint Information
    # ---------------------------------------------------------

    if endpoint:

        endpoint_details = f"""
Method            : {endpoint.get("method")}
Path              : {endpoint.get("path")}
Function          : {endpoint.get("function")}
Request Model     : {endpoint.get("request_model")}
Response Model    : {endpoint.get("response_model")}
Status Code       : {endpoint.get("status_code")}
Tags              : {", ".join(endpoint.get("tags", []))}
Summary           : {endpoint.get("summary")}
Description       : {endpoint.get("description")}
"""

    else:

        endpoint_details = """
No endpoint detected.

Generate test cases based on the source code only.
"""

    # ---------------------------------------------------------
    # Model Information
    # ---------------------------------------------------------

    model_details = ""

    if models:

        model_details += "REQUEST / RESPONSE MODELS\n\n"

        for model_name, model in models.items():

            model_details += f"Model : {model_name}\n"

            for field in model.get("fields", []):

                model_details += (
                    f"- {field['name']} "
                    f"({field['type']}) "
                    f"Required={field['required']}\n"
                )

            model_details += "\n"

    else:

        model_details = "No models discovered."

    # ---------------------------------------------------------
    # Database Information
    # ---------------------------------------------------------

    db_details = ""

    if database_analysis:

        tables = database_analysis.get(
            "tables",
            [],
        )

        if tables:

            db_details += "DATABASE TABLES\n"

            for table in tables:

                db_details += f"- {table}\n"

        crud_operations = database_analysis.get(
            "crud_operations",
            [],
        )[:5]

        if crud_operations:

            db_details += "\nCRUD OPERATIONS\n"

            for crud in crud_operations:

                db_details += (
                    f"- {crud['operation']} "
                    f"({crud['file']}:{crud['line']})\n"
                )

    else:

        db_details = "No database information discovered."

    # ---------------------------------------------------------
    # Authentication
    # ---------------------------------------------------------

    auth_details = ""

    if authentication_analysis:

        auth_details += (
            f"Authentication Type : "
            f"{authentication_analysis.get('type')}\n\n"
        )

        protected = authentication_analysis.get(
            "protected_endpoints",
            [],
        )[:10]

        if protected:

            auth_details += "Protected Endpoints\n"

            for ep in protected:

                if "method" in ep:

                    auth_details += (
                        f"- {ep['method']} "
                        f"{ep['path']}\n"
                    )

                else:

                    auth_details += (
                        f"- {ep['function']}\n"
                    )

    else:

        auth_details = "No authentication discovered."

    # ---------------------------------------------------------
    # Source Code
    # ---------------------------------------------------------

    source_code = textwrap.dedent(code)

    # ---------------------------------------------------------
    # Final Prompt
    # ---------------------------------------------------------

    prompt = f"""
You are a Principal QA Architect with 15+ years of API Testing experience.

Generate HIGH QUALITY manual API Test Cases.

==========================================================
PROJECT INFORMATION
==========================================================

Repository
----------
{repository_context.get("repository_name")}

Language
--------
{repository_context.get("language")}

Framework
---------
{repository_context.get("framework")}

Database
--------
{repository_context.get("database")}

ORM
---
{repository_context.get("orm")}

==========================================================
CURRENT FILE
==========================================================

{file_name}

==========================================================
CURRENT ENDPOINT
==========================================================

{endpoint_details}

==========================================================
MODELS
==========================================================

{model_details}

==========================================================
DATABASE
==========================================================

{db_details}

==========================================================
AUTHENTICATION
==========================================================

{auth_details}

==========================================================
SOURCE CODE
==========================================================

{source_code}

==========================================================
TASK
==========================================================

Generate ONLY 5-8 Manual API Test Cases.

Focus ONLY on:

- Current Endpoint
- Current Source Code
- Current Request Model
- Current Response Model

Ignore unrelated repository information.

Cover:

- Positive
- Negative
- Boundary
- Validation
- Authentication
- Authorization
- CRUD
- Security
- Error Handling

==========================================================
OUTPUT RULES
==========================================================

Return ONLY VALID JSON.

The FIRST character MUST be [

The LAST character MUST be ]

Do NOT return:

- Markdown

- Explanation

- Notes

- Code block

- Triple backticks

Use DOUBLE QUOTES ONLY.

Each object MUST follow EXACTLY this schema:

[
  {{
    "title": "",
    "module": "",
    "priority": "",
    "severity": "",
    "test_type": "",
    "preconditions": "",
    "steps": [
      ""
    ],
    "expected_result": ""
  }}
]

Return ONLY JSON.
"""

    return prompt.strip()