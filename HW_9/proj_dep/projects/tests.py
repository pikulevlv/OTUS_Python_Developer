import math
# import logging
# logging.basicConfig(level = logging.DEBUG)
# logging.debug( u'This is a debug message' )

from django.test import TestCase, Client
from .models import Staff, StaffListPosition, Direction, \
    Sertificate, Project, Stage, Role
from django.contrib.auth.models import User

import datetime


# Create your tests here.

class TestModels(TestCase):

    def setUp(self):
        print('-'*10, 'setUp', '-'*10)
        self.sert_1 = Sertificate.objects.create(name='Prof_ERP')
        self.sert_2 = Sertificate.objects.create(name='Spec_ERP')
        self.sert_3 = Sertificate.objects.create(name='Expert')
        self.dir_1 = Direction.objects.create(name='ERP')
        self.dir_2 = Direction.objects.create(name='ZUP')
        self.dir_3 = Direction.objects.create(name='DO')
        self.sl_pos_1 = StaffListPosition.objects.create(name='KONS')
        self.sl_pos_2 = StaffListPosition.objects.create(name='DEV')
        self.sl_pos_3 = StaffListPosition.objects.create(name='PM')

        # staff_1
        self.staff_1 = Staff.objects.create(name='Inna', surname='Petrova',
                                      salary=140_000, is_staff=True)
        self.staff_1.sl_position.add(self.sl_pos_1)
        self.staff_1.direct.set([self.dir_1, self.dir_3])
        self.staff_1.serts.set([self.sert_1, self.sert_2])
        self.staff_1.serts.create(name='Prof_UU')
        self.staff_1.save()

        # staff_2
        self.staff_2 = Staff.objects.create(name='Andrey', surname='Mirzaev',
                                      salary=160_000,
                                      is_staff=True)
        self.staff_2.sl_position.add(self.sl_pos_2)
        self.staff_2.direct.set([self.dir_1, self.dir_2, self.dir_3])
        self.staff_2.serts.add(self.sert_1)
        self.staff_2.serts.add(self.sert_2)
        self.staff_2.serts.add(self.sert_3)
        self.staff_2.save()

        # staff_3
        self.staff_3 = Staff.objects.create(name='Leonid', surname='Pulman',
                                      salary=180_000,
                                      is_staff=True)
        self.staff_3.sl_position.add(self.sl_pos_3)
        self.staff_3.direct.set([self.dir_1, self.dir_3])
        self.staff_3.save()

        # proj_1
        self.proj_1 = Project.objects.create(name='Project_Alpha',
                                             description='A - description...')
        self.proj_1.direction.set([self.dir_1])
        self.stage_1_1 = Stage.objects.create(name='Stage_1_Alpha',
                                              proj=self.proj_1,
                                              start_plan=datetime.date(2020, 10, 1),
                                              start_fact=datetime.date(2020, 10, 5),
                                              end_plan=datetime.date(2020, 10, 25),
                                              end_fact=datetime.date(2020, 10, 28),
                                              exp_plan=500_000,
                                              exp_fact= 515_000,
                                              is_completed= True)
        self.stage_1_2 = Stage.objects.create(name='Stage_2_Alpha',
                                              proj=self.proj_1,
                                              start_plan=datetime.date(2020, 11, 1),
                                              start_fact=datetime.date(2020, 11, 1),
                                              end_plan=datetime.date(2020, 11, 30),
                                              # end_fact=datetime.date(2020, 11, 30),
                                              exp_plan=800_000,
                                              # exp_fact= 800_000,
                                              is_completed= False)
        self.role_1_pm = Role.objects.create(name='PM in Alpha',
                                        proj=self.proj_1,
                                        staff=self.staff_3)
        self.role_1_pm.stages.set([self.stage_1_1, self.stage_1_2])

        self.role_1_kons = Role.objects.create(name='KONS in Alpha',
                                        proj=self.proj_1,
                                        staff=self.staff_1)
        self.role_1_kons.stages.set([self.stage_1_1, self.stage_1_2])

        self.role_1_dev = Role.objects.create(name='DEV in Alpha',
                                        proj=self.proj_1,
                                        staff=self.staff_2)
        self.role_1_dev.stages.set([self.stage_1_2])



    def tearDown(self):
        print('-'*10, 'tearDown', '-'*10)
        return

    def test_str(self):
        print('-'*10, 'test_str', '-'*10)
        self.assertEqual(str(self.sert_1), self.sert_1.name)
        self.assertEqual(str(self.sert_2), self.sert_2.name)
        self.assertEqual(str(self.sert_3), self.sert_3.name)
        self.assertEqual(str(self.dir_1), self.dir_1.name)
        self.assertEqual(str(self.dir_2), self.dir_2.name)
        self.assertEqual(str(self.dir_3), self.dir_3.name)
        self.assertEqual(str(self.sl_pos_1), self.sl_pos_1.name)
        self.assertEqual(str(self.sl_pos_2), self.sl_pos_2.name)
        self.assertEqual(str(self.sl_pos_3), self.sl_pos_3.name)
        self.assertEqual(str(self.staff_1), f"{self.staff_1.name} "
                                            f"{self.staff_1.surname} "
                                            f"(id# {self.staff_1.id})")
        self.assertEqual(str(self.staff_2), f"{self.staff_2.name} "
                                            f"{self.staff_2.surname} "
                                            f"(id# {self.staff_2.id})")
        self.assertEqual(str(self.staff_3), f"{self.staff_3.name} "
                                            f"{self.staff_3.surname} "
                                            f"(id# {self.staff_3.id})")
        self.assertEqual(str(self.proj_1), self.proj_1.name)
        self.assertEqual(str(self.stage_1_1), f"{self.stage_1_1.name} "
                                            f"of {self.stage_1_1.proj}")
        self.assertEqual(str(self.stage_1_2), f"{self.stage_1_2.name} "
                                            f"of {self.stage_1_2.proj}")
        self.assertEqual(str(self.role_1_pm), f"{self.role_1_pm.name} "
                                            f"in {self.stage_1_1.proj}")
        self.assertEqual(str(self.role_1_kons), f"{self.role_1_kons.name} "
                                            f"in {self.role_1_kons.proj}")
        self.assertEqual(str(self.role_1_dev), f"{self.role_1_dev.name} "
                                            f"in {self.role_1_dev.proj}")

    def test_project_resource_count(self):
        print('-' * 10, 'test_project_resource_count', '-' * 10)
        self.assertEqual(self.proj_1.project_resource_count(), 3)