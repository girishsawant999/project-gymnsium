from django.db import models

Gender_Choices = (('M', 'Male'), ('F', 'Female'))
Status_Choices = ((1, 'Active'), (0, 'Inactive'))


# Create your models here
class Customer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender_Choices)
    proof_id_no = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    user_map_id = models.IntegerField(editable=False)

    def __str__(self):
        return f'Customer : {self.name} (Id : {self.id})'


class CustomerStatus(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_fees = models.IntegerField()
    fees_paid = models.IntegerField()
    fees_remaining = models.IntegerField()
    status = models.IntegerField(choices=Status_Choices)

    def __str__(self):
        return f'Customer: {self.customer} | Status : {self.status}'

class UserAuth(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"User  : {self.user_id} . {self.username}"



