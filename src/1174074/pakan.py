# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:42:07 2019

@author: Aspire E15
"""

class pakan:
    jumlahpakan = 0
    def __init__(self, kode, jenis):
        self.kode = kode
        self.jenis = jenis
        pakan.jumlahpakan +=12
    def DataPakan(self):
        print("Kode pakan :", self.kode)
        print("jenis pakan :", self.jenis)
        print()
pakan1 = pakan("P001", "Berkonsentrat")
pakan2 = pakan("P002", "Tidak Berkonsentrat")
pakan1.DataPakan()
pakan2.DataPakan()
print("Total Pemesanan Pakan Sebanyak:", pakan.jumlahpakan, "pakan")
