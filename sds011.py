#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial


se = serial.Serial()
se.port = '/dev/serial0'
se.baudrate = 9600


def start():
    se.open()
    se.flushInput()


def end():
    se.close()


def getParticle():
    byte = 0

    # read until we meet message header
    while byte != '\xaa':
        byte = se.read(size=1)

    # read a 9-byte packet
    data = se.read(size=9)

    if data[0] == '\xc0' and data[8] == '\xab':
        checksum = sum([ord(x) for x in data[1:7]]) % 256

        if checksum == ord(data[7]):
            pm25 = float(ord(data[2]) * 256 + ord(data[1])) / 10
            pm10 = float(ord(data[4]) * 256 + ord(data[3])) / 10
            return pm25, pm10
