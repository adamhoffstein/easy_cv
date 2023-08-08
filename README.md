# Easy CV

Are you exhausted with customizing your resume over and over for each job that you apply to?

Easy CV is a webapp to help you with exactly that. 
Acting as a repo for all your relevant job duties and skill lists, 
Easy CV can produce a customized and professional-looking CV from a copy-pasted job ad by 
show-casing the parts of your job duties that match it most.

# Quickstart

## Prerequisites

- Python (>= 3.11)
- Poetry (installed globally, see [Poetry Installation Guide](https://python-poetry.org/docs/#installation))

## Step 1: Clone the Project

Clone the existing Django project repository to your local machine:

```bash
git clone git@github.com:adamhoffstein/easy_cv.git
cd easy_cv
```

## Step 2: Install Dependencies
Navigate to the project directory and use Poetry to install project dependencies:
```bash
poetry shell && poetry install
```

## Step 4: Apply Migrations
```bash
poetry run python manage.py migrate
```

## Step 5: Run the Development Server
```bash
poetry run python manage.py runserver
```
* Now you can view the UI by opening up your favorite web browser and visiting [http://127.0.0.1:8000](http://127.0.0.1:8000)
* You will be asked to create an account and login

## Step 6: Enter Your Skill Tags
* Click on the link for [Skill Tags](http://127.0.0.1:8000/tags) and then [Bulk Add](http://127.0.0.1:8000/tags/bulk_import/).
* You will be prompted to enter a number of comma-delimited skills and a category.

## Step 7: Enter Your Resume Details
* You can start entering your experience by clicking on the link for [Job Experience](http://127.0.0.1:8000/resume_jobs)
and then clicking the 'Add' button. Fill out the required fields, including the "Job duty raw text" field. 
Your job duties should be formatted like this: 
```text
Job Duty A
* responsibility 1

Job Duty B
* responsibility 2
* responsibility 3
```
* When you click save, you will notice that it is now neatly formatted with headers and bullet points

## Step 8: Enter a Job Description
* You can enter a job description by clicking on the link for [Job Descriptions](http://127.0.0.1:8000/job_descriptions)
and then the 'Add' button.
* Simply copy-paste the text of the job description from LinkedIn or wherever into the 'raw text' field and click 'save'.
* You should notice some keywords have been highlighted in the job description based on what you added in Step 6

TO BE CONTINUED