import boto3
import csv
import io
from models import Todo


AWS_ACCESS_KEY = 'Your AWS IAM Access Key'
AWS_SECRET_KEY = 'Your AWS IAM Secret Key'
BUCKET_NAME = 'Your Bucket Name'

def upload_csv_to_s3(todos: list[Todo]) -> str:
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Title", "Description", "Due Date", "Created At", "Completed"])

    for todo in todos:
        writer.writerow([
            todo.id,
            todo.title,
            todo.description,
            todo.due_date,
            todo.created_at,
            todo.completed
        ])

    filename = "todos_export.csv"
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=output.getvalue(), ContentType="text/csv")

    return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
