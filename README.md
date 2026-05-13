markdown
# Freelancer Business Activities Dataset API

This API provides programmatic access to the Freelancer Business Activities Dataset, enabling users to query, filter, and analyze data efficiently. It is designed for entrepreneurs, researchers, policymakers, and individuals seeking specific freelancer services in Abu Dhabi.

## Features

- Query freelancer activities by category.
- Retrieve data in English or Arabic.
- Access metadata about the dataset.
- Retrieve data in JSON format for integration with other applications.

## Endpoints

### Get Freelancer Activities

**URL:** `/api/freelancer_activities`

**Method:** `GET`

**Query Parameters:**

- `category` (optional): Filter activities by category (e.g., "sports").
- `language` (optional): Specify the language for the response (`English` or `Arabic`). Default is `English`.

**Response:**

A JSON array of freelancer activities, each with an `Activity_ID` and a name in the specified language.

**Example Request:**


GET /api/freelancer_activities?category=sports&language=Arabic


**Example Response:**


[
    {
        "Activity_ID": 101,
        "Arabic_Name": "خدمات رياضية"
    },
    {
        "Activity_ID": 102,
        "Arabic_Name": "تصوير تحت الماء"
    }
]


### Get Metadata

**URL:** `/api/metadata`

**Method:** `GET`

**Response:**

A JSON object containing metadata about the dataset.

**Example Request:**


GET /api/metadata


**Example Response:**


{
    "release_date": "2023-11-01",
    "update_frequency": "Annually",
    "data_owner": "Abu Dhabi Department of Economic Development",
    "language": ["English", "Arabic"],
    "access_level": "Public"
}


## Installation

1. Clone the repository:
   
   git clone https://github.com/your-repo-name/freelancer-api
   

2. Navigate to the project directory:
   
   cd freelancer-api
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Run the application:
   
   python app.py
   

5. Access the API at `http://localhost:5000`

## Requirements

- Python 3.8+
- Flask
- Pandas
- OpenPyXL

Install the required libraries using the `requirements.txt` file.

## Feedback and Contributions

We welcome feedback and contributions to improve this API. Please open an issue or submit a pull request at [GitHub Repository](https://github.com/your-repo-name/freelancer-api).
