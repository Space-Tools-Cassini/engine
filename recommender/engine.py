#!/usr/bin/env python3
#
# Engine module
# This is the main code of the recommendator engine
# This must be a simple API.

class Process:
    
    def __init__(self,lat,lon,time_init):
        self.lat=lat #latitude
        self.lon=lon #longitude 
        self.scored_crops=[] #scored crops
        self.skipped_crops=[] #discarded crops
        self.time_init=time_init #Time where process starts
        self.time_stop = 0 #Time where process is ended

    def add_scored_crops(self, scored_crop):
        self.scored_crops.append(scored_crop)
    
    def add_skipped_crops(self, skipped_crop):
        self.skipped_crops.append(skipped_crop)

class Mapper:

    def __init__(self):
        self.crop_score = []

    def add_crop_score(self, crop, score):
        self.crop_score.append((crop,score))
        

def analize():
    """
    def 
    """
    # TODO:
    # - Implement the Process initializer.
    # - Implement the DataManager.
    # - Implement the Mapper.
    #
    # Process Inits --> DataManager gets and process data 
    # --> Mapper --> Add results of the mapping to the Process
    # --> return the Process data.
    pass
