
import datetime
from Ejercicio03.Utils import format_date
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, ValidationError

class TaskForm(FlaskForm):

    fecha = DateField('Fecha', validators=[InputRequired(message="La fecha es requerida")])
    descripcion = TextAreaField('Descripcion', validators=[InputRequired(message="La descripcion es requerida")])
    prioridad = SelectField(choices=[(i, i) for i in range(6)], coerce=int)
    estado = SelectField(choices=[(0, 'Pendiente'), (1, 'En proceso'), (2, 'Completada')], coerce=int)

    def __init__(self, update, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update = update
        if not self.fecha.data:
            self.fecha.data = datetime.date.today()

    def validate_fecha(self, field):
        past = format_date(field.data)
        past_date = datetime.datetime(past.year, past.month, past.day)
        present_date = datetime.datetime.now() - datetime.timedelta(days=1)
        
        if past_date < present_date and not self.update:
            raise ValidationError("La fecha no puede ser anterior a la actual")


class SelectTaskForm(FlaskForm):

    id = IntegerField('ID de la tarea', validators=[InputRequired(message="El ID de la tarea es requerida")])

    def __init__(self, task_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_list = task_list    

    def validate_id(self, field):
        if not any(task.id == field.data for task in self.task_list):
            raise ValidationError("El ID de la tarea no existe")

class TaskListForm(FlaskForm):
    
    prioridad = SelectField(choices=[(i, i) for i in range(6)], coerce=int)
    estado = SelectField(choices=[(0, 'Pendiente'), (1, 'En proceso'), (2, 'Completada')], coerce=int)
