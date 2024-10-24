import pyedflib
import numpy as np
import scipy 
import pandas as pd
import polars as pl

class EdfFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_info = None
        self.file_dur = None
        self.code = None
        self.sex = None
        self.dob = None
        self.name = None
        self.equipment = None
        self.labels = None
        self.dimension = None
        self.header = None
        self.frequencies = None
        self.start_time = None
        self.ECG_A = None
        self.ECG_B = None
        self.HR = None
        self.RR_int = None
        self.resp = None
        self.skin_imp = None
        self.RR = None
        self.skin_temp = None
        self.ACC_X = None
        self.ACC_Y = None
        self.ACC_Z = None
        self.posture = None
        self.posture_fine = None
        self.activity = None
        self.body_temp = None

    def read_file(self):
        f = pyedflib.EdfReader(self.file_path)
        self.file_info = f.file_info_long()
        self.file_dur = f.getFileDuration()
        self.code = f.getPatientCode()
        self.sex = f.getSex()
        self.dob = f.getBirthdate()
        self.name = f.getPatientName()
        self.equipment = f.getEquipment()
        self.labels = f.getSignalLabels()
        self.dimension = f.getPhysicalDimension(0)
        self.header = f.getHeader()
        self.frequencies = f.getSampleFrequencies()
        self.start_time = f.getStartdatetime()

        self.ECG_A = f.readSignal(0)
        self.ECG_B = f.readSignal(1)
        self.HR = f.readSignal(2)
        self.RR_int = f.readSignal(3)
        self.resp = f.readSignal(4)
        self.skin_imp = f.readSignal(5)
        self.RR = f.readSignal(6)
        self.skin_temp = f.readSignal(7)
        self.ACC_X = f.readSignal(8)
        self.ACC_Y = f.readSignal(9)
        self.ACC_Z = f.readSignal(10)
        self.posture = f.readSignal(11)
        self.posture_fine = f.readSignal(12)
        self.activity = f.readSignal(13)
        self.body_temp = f.readSignal(14)

        f.close()