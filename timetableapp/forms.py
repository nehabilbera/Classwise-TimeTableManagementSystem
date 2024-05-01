from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm, TimeInput, MultipleChoiceField
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        label = {
            'password1':'Password', 'password2':'Password'
        }
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['user','course_id', 'course_name', 'course_type', "department", "professor", 'credit_hours', 'contact_hours']
        exclude = ['user']
        labels = {'course_id':'Subject id','course_name':'Subject name','course_type':'Subject type',"department":"Course",'credit_hours':'No of classes per week',
                  'contact_hours':'Total hours per week'}


class DateIn(DateInput):
    input_type = "date"


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['user','professor_id', 'professor_name','dob','professor_email', 'working_hours','available_hours']
        exclude = ['user']
        labels = {'dob':'DOB (DD-MM-YYYY)'}
        widgets = {
            "dob": DateIn()
        }

class TimeIn(TimeInput):
    input_type = "time"


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['user','class_id','class_name','class_strength','week_day','no_sessions','class_mins','start_time',
                    'end_time','break_start','break_end']
        exclude = ['user']
        labels = {
            # 'class_id':'Class ID',
            # 'class_name':'Class Name',
            'week_day':'Select the days when classes are conducted',
            'no_sessions':'Number of sessions per day',
            'class_mins':'Minutes per Session',
            'start_time':'Start of the Day',
            'end_time':'End of the Day',
            'break_start':'Short break start time',
            'break_end':'Short break end time',
            'break_start_2':'Long break start time',
            'break_end_2':'Long break end time',
        }
        widgets = {
            "start_time": TimeIn(),
            "end_time" : TimeIn(),
            "break_start": TimeIn(),
            "break_end": TimeIn(),
            "break_start_2": TimeIn(),
            "break_end_2": TimeIn(),
        }


class DepartmentForm(ModelForm):
    class Meta:
        model= Department
        field=['user','department_name','branch_name','semester','students_length']
        exclude=['user']
        labels={
            'branch_name': 'Course',
            'department_name': 'Department'
        }
        widgets = {
            
            
        }

    
class ClassCourseForm(ModelForm):
    class Meta:
        model = ClassCourse
        fields = ['user','class_id','course_id','professor_id']
        exclude = ['user']
        labels={'course_id':'Subject name','professor_id':'professor_name'}
    def __init__(self, *args,  **kwargs):
        super(ClassCourseForm, self).__init__(*args, **kwargs)
        self.fields['class_id'].queryset = Class.objects.filter()
        self.fields['professor_id'].queryset = Professor.objects.filter()
        self.fields['course_id'].queryset = Course.objects.filter()

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [ 'activity_type', 'course', 'day',
                  'start_time']
        labels = {
            'start_time':'Session Number'
        }
    WEEK_DAY = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')
    )
    day = MultipleChoiceField(choices=WEEK_DAY)
    def __init__(self, *args,  **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].initial = 1
        self.fields['course'].queryset = ClassCourse.objects.filter()


class ActivityFormUpdate(ModelForm):
    class Meta:
        model = Activity
        fields = ['user','activity_type','course']
        exclude = ['user']
        labels = {
            'activity_type':'Should be Fixed During Generation?(Fixed/Replace) '
        }
    def __init__(self, *args,  **kwargs):
        super(ActivityFormUpdate, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = ClassCourse.objects.filter()
