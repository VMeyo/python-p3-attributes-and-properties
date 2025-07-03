#!/usr/bin/env python3
#
#APPROVED_JOBS = [
 #   "Admin",
  #  "Customer Service",
   # "Human Resources",
    #"ITC",
    #"Production",
    #Legal",
    #"Finance",
    #"Sales",
    #"General Management",
    #"Research & Development",
    #"Marketing",
    #"Purchasing"
#]
#

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]
    # class attribute

    def __init__(self, name="John Doe", job="Admin"):
        self.name = name # Instance attribute
        self.job = job # Instance attribute

    @property
    def name(self):
        return self._name
    # Allows us to access name as an attribute

    @name.setter # Validates the name
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25: # Ensures the name is between 1 & 25 characters.
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    # Allows us to access job as an attribute

    @job.setter # Validates the job
    def job(self, value):
        if value in Person.approved_jobs: # Class variable is can be called by the class
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
