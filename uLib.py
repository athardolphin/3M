import numpy as np

def r2p():
    return  x**p

def p2c(r,t):# receive angle in rad
    x = r*np.cos(t)
    y = r*np.sin(t)
    return x,y

def R(alp):
    return np.array([[np.cos(alp),np.sin(alp)],[-np.sin(alp),np.cos(alp)]])

def R1(alp):
    return np.array([[1,0,0],[0,np.cos(alp),np.sin(alp)],[0,-np.sin(alp),np.cos(alp)]])

def R2(alp):
    return np.array([[np.cos(alp),0,-np.sin(alp)],[0,1,0],[np.sin(alp),0,np.cos(alp)]])

def R3(alp):
    return np.array([[np.cos(alp),np.sin(alp),0],[-np.sin(alp),np.cos(alp),0],[0,0,1]])
