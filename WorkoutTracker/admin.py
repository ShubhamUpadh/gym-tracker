from django.contrib import admin
from .models import user_table, date_workout_table, set_detail_table, predefined_exercise_table, custom_exercise
# Register your models here.

@admin.register(user_table)
class user_table_admin(admin.ModelAdmin):
    list_display = ('id','name','phone','email')

@admin.register(predefined_exercise_table)
class predefined_exercise_table_admin(admin.ModelAdmin):
    list_display = ('id','exercise_name','exercise_type','major_muscle')

@admin.register(date_workout_table)
class date_workout_table_admin(admin.ModelAdmin):
    list_display = ('id','exercise_id','user_id','workout_date')

@admin.register(set_detail_table)
class set_detail_table_admin(admin.ModelAdmin):
    list_display = ('id','date_workout_id','set_number','weight','repetition','remarks')

@admin.register(custom_exercise)
class custom_exercise_admin(admin.ModelAdmin):
    list_display = ('id','user_id','exercise_name','major_muscle','exercise_type')