# ML Flask Car Price Prediction

**Machine Learning model deployed on the Heroku platform**

🔗 **Live Application:**  
https://ml-car-price.herokuapp.com/

This project was developed using **PyCharm**, and **Flask** is used for backend and frontend integration.

---

## Project Structure

1. **mayuri_01.py**  
   - Linear Regression model trained on the `car data.csv` dataset  
   - Achieved an **R-squared value of 0.87**

2. **random_forest_regression_model_01.pkl**  
   - Pickle file generated for the trained model

3. **requirements.txt**  
   - Contains all Python dependencies required to run the project in a new environment

4. **app_car.py**  
   - Flask application file containing routing and backend logic

5. **templates/index_mayuri01.html**  
   - Home page

6. **templates/index_mayuri.html**  
   - Car Price Predictive Analysis input page

7. **templates/index_mayuri02.html**  
   - Displays the predicted car price based on user input

8. **Procfile**  
   - Used for deploying the application on Heroku  
   - Uses the `gunicorn` command to run the Flask app

---

## Application Preview

![App Screenshot](https://user-images.githubusercontent.com/68188457/118434796-4f650880-b6fb-11eb-8452-4b820992eb6c.png)

---

## Issues Faced During Deployment

1. The model build failed on Heroku because the file was incorrectly named as `requirement.txt` instead of `requirements.txt`.

2. The `gunicorn` module was missing, which caused an **Application Error** after deployment.

---

## Solution

The issues were resolved using the **Heroku CLI**:

```bash
heroku login
heroku logs --app ml-car-price
```

### Technologies Used

- Python
- Flask
- Scikit-learn
- HTML/CSS
- Heroku
- Gunicorn
