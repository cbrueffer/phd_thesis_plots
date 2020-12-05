#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Christian Brueffer
"""

import pylab as pl
from matplotlib.patches import Rectangle
pl.style.use('classic')


color_all_data = "#CCCCCC"
color_training = "#baed91"
color_test = "#b2cefe"
color_validation = "#FECD0066"

def create_cv(box_data = color_all_data,
              box_train = color_training,
              box_test = color_test,
              box_validation = color_validation):
    fig = pl.figure(figsize=(9, 6), facecolor='w')
    ax = pl.axes((0, 0, 1, 1),
                 xticks=[], yticks=[], frameon=False)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)

    patches = [Rectangle((0.9, 5.5), 8, 0.5, fc=box_data),
               
               # training data
               Rectangle((0.9, 4.8), 5.4, 0.5, fc=box_train),
               # test data
               Rectangle((6.4, 4.8), 2.5, 0.5, fc=box_validation),
               
               # first row
               Rectangle((0.9, 3.9), 1, 0.5, fc=box_data),
               Rectangle((2, 3.9), 1, 0.5, fc=box_data),
               Rectangle((3.1, 3.9), 1, 0.5, fc=box_data),
               Rectangle((4.2, 3.9), 1, 0.5, fc=box_data),
               Rectangle((5.3, 3.9), 1, 0.5, fc=box_data),
               
               # second row
               Rectangle((0.9, 3.26), 1, 0.5, fc=box_test),
               Rectangle((2, 3.26), 1, 0.5, fc=box_train),
               Rectangle((3.1, 3.26), 1, 0.5, fc=box_train),
               Rectangle((4.2, 3.26), 1, 0.5, fc=box_train),
               Rectangle((5.3, 3.26), 1, 0.5, fc=box_train),
               
               # third row
               Rectangle((0.9, 2.62), 1, 0.5, fc=box_train),
               Rectangle((2, 2.62), 1, 0.5, fc=box_test),
               Rectangle((3.1, 2.62), 1, 0.5, fc=box_train),
               Rectangle((4.2, 2.62), 1, 0.5, fc=box_train),
               Rectangle((5.3, 2.62), 1, 0.5, fc=box_train),
               
               # fourth row
               Rectangle((0.9, 1.98), 1, 0.5, fc=box_train),
               Rectangle((2, 1.98), 1, 0.5, fc=box_train),
               Rectangle((3.1, 1.98), 1, 0.5, fc=box_test),
               Rectangle((4.2, 1.98), 1, 0.5, fc=box_train),
               Rectangle((5.3, 1.98), 1, 0.5, fc=box_train),
               
               # fifth row
               Rectangle((0.9, 1.34), 1, 0.5, fc=box_train),
               Rectangle((2, 1.34), 1, 0.5, fc=box_train),
               Rectangle((3.1, 1.34), 1, 0.5, fc=box_train),
               Rectangle((4.2, 1.34), 1, 0.5, fc=box_test),
               Rectangle((5.3, 1.34), 1, 0.5, fc=box_train),
               
               # sixth row
               Rectangle((0.9, 0.7), 1, 0.5, fc=box_train),
               Rectangle((2, 0.7), 1, 0.5, fc=box_train),
               Rectangle((3.1, 0.7), 1, 0.5, fc=box_train),
               Rectangle((4.2, 0.7), 1, 0.5, fc=box_train),
               Rectangle((5.3, 0.7), 1, 0.5, fc=box_test),
               
               # final test data
               Rectangle((6.4, 0.0), 2.5, 0.5, fc=box_validation),
               
               # "brace"
               Rectangle((6.4, 0.64), 0.01, 3.82, fc="black"),
               Rectangle((6.4, 0.64), -0.1, 0.01, fc="black"),
               Rectangle((6.4, 4.45), -0.1, 0.01, fc="black"),
               Rectangle((6.4, 2.545), 0.15, 0.02, fc="black"),
               ]
               
   
    for p in patches:
        ax.add_patch(p)
    
    pl.text(4.9, 5.73, "All Data",
            ha='center', va='center', fontsize=14)
    
    pl.text(3.5, 5.04, "Training data",
            ha='center', va='center', fontsize=14)
    
    pl.text(7.6, 5.04, "Validation data",
            ha='center', va='center', fontsize=14)
    
    # first row
    pl.text(1.41, 4.14, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 4.14, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 4.14, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 4.14, "Fold 4",
            ha='center', va='center', fontsize=14)
    pl.text(5.82, 4.14, "Fold 5",
            ha='center', va='center', fontsize=14)
    
    # second row
    pl.text(0.1, 3.5, "Split 1", 
            ha='left', va='center', fontsize=14)
    pl.text(1.41, 3.5, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 3.5, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 3.5, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 3.5, "Fold 4",
            ha='center', va='center', fontsize=14)
    pl.text(5.82, 3.5, "Fold 5",
            ha='center', va='center', fontsize=14)
        
    # third row
    pl.text(0.1, 2.86, "Split 2", 
            ha='left', va='center', fontsize=14)
    pl.text(1.41, 2.86, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 2.86, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 2.86, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 2.86, "Fold 4",
            ha='center', va='center', fontsize=14)
    pl.text(5.82, 2.86, "Fold 5",
            ha='center', va='center', fontsize=14)
        
    # fourth row
    pl.text(0.1, 2.22, "Split 3", 
            ha='left', va='center', fontsize=14)
    pl.text(1.41, 2.22, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 2.22, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 2.22, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 2.22, "Fold 4",
            ha='center', va='center', fontsize=14)
    pl.text(5.82, 2.22, "Fold 5",
            ha='center', va='center', fontsize=14)
    
    # fifth row
    pl.text(0.1, 1.58, "Split 4", 
            ha='left', va='center', fontsize=14)
    pl.text(1.41, 1.58, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 1.58, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 1.58, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 1.58, "Fold 4",
            ha='center', va='center', fontsize=14,)
    pl.text(5.82, 1.58, "Fold 5",
            ha='center', va='center', fontsize=14)
    
    # sixth row
    pl.text(0.1, 0.94, "Split 5", 
            ha='left', va='center', fontsize=14)
    pl.text(1.41, 0.94, "Fold 1",
            ha='center', va='center', fontsize=14)
    pl.text(2.52, 0.94, "Fold 2",
            ha='center', va='center', fontsize=14)
    pl.text(3.62, 0.94, "Fold 3",
            ha='center', va='center', fontsize=14)
    pl.text(4.72, 0.94, "Fold 4",
            ha='center', va='center', fontsize=14)
    pl.text(5.82, 0.94, "Fold 5",
            ha='center', va='center', fontsize=14)
    
    pl.text(7.6, 0.23, "Validation data",
            ha='center', va='center', fontsize=14)

    pl.text(6.7, 2.55, "Parameter\noptimization",
            ha='left', va='center', fontsize=14)
    
    pl.text(0.2, 5.86, "B.",
            ha='center', va='center', fontweight='bold', fontsize=22)
       
    return fig
    

def create_normal_split(box_data = color_all_data,
                        box_train = color_training,
                        box_test = color_test,
                        box_validation = color_validation):
    fig = pl.figure(figsize=(9, 6), facecolor='w')
    ax = pl.axes((0, 0, 1, 1),
                 xticks=[], yticks=[], frameon=False)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)

    patches = [Rectangle((0.9, 5.5), 8, 0.5, fc=box_data),
               
               # training data
               Rectangle((0.9, 4.8), 2.6, 0.5, fc=box_train),
               # test data
               Rectangle((3.6, 4.8), 2.6, 0.5, fc=box_test),
               # validation data
               Rectangle((6.3, 4.8), 2.6, 0.5, fc=box_validation),
               ]
   
    for p in patches:
        ax.add_patch(p)
    
    pl.text(4.9, 5.73, "All Data",
            ha='center', va='center', fontsize=14)
    
    pl.text(2.23, 5.04, "Training data",
            ha='center', va='center', fontsize=14)
    
    pl.text(4.9, 5.04, "Test data",
            ha='center', va='center', fontsize=14)
    
    pl.text(7.6, 5.04, "Validation data",
            ha='center', va='center', fontsize=14)
    
    pl.text(0.2, 5.86, "A.",
            ha='center', va='center', fontweight='bold', fontsize=22)
        
    return fig


f = create_cv()
f.savefig("ml_data_split_cv.pdf", bbox_inches='tight')

f = create_normal_split()
f.savefig("ml_data_split_normal.pdf", bbox_inches='tight')
