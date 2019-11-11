# api_studentdb
the urls for testing in httpie tool is:
•	winpty http --form POST http://127.0.0.1:8000/add (to add New student)
•	winpty http http://127.0.0.1:8000/students (List Students in the record with first names)
•	winpty http http://127.0.0.1:8000/student/<id> (get student details by id)
•	winpty http http://127.0.0.1:8000/students/<id> (update student by id)
•	winpty http http://127.0.0.1:8000/clear (delete entire records)
