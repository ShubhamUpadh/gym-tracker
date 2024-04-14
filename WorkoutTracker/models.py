from django.db import models

# Create your models here.

class user_table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

class predefined_exercise_table(models.Model):
    id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length=100)
    major_muscle = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=50)

class date_workout_table(models.Model):
    id = models.AutoField(primary_key=True)
    # links date_workout_table to predefined_exercise_table
    exercise_id = models.ForeignKey(predefined_exercise_table,on_delete=models.CASCADE, related_name='workouts')
    # links date_workout_table to user_table
    user_id = models.ForeignKey(user_table,on_delete=models.CASCADE,related_name='workouts')               
    workout_date = models.DateField()

class set_detail_table(models.Model):
    id = models.AutoField(primary_key=True)
    # links set_detail_table to date_workout_table
    date_workout_id = models.ForeignKey(date_workout_table,on_delete=models.CASCADE, related_name="sets")
    set_number = models.IntegerField()
    weight = models.IntegerField()
    repetition = models.IntegerField()
    remarks = models.CharField(max_length=50)

class custom_exercise(models.Model):
    id = models.AutoField(primary_key=True)
    # links custom_exercise to user_table
    user_id = models.ForeignKey(user_table,on_delete=models.CASCADE, related_name="customs")
    exercise_name = models.CharField(max_length=100)
    major_muscle = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=50)
