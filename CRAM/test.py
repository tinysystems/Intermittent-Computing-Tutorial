import unittest

from array import *
from params import *
from logic import AND, OR, NOT, BUFF, NAND, NOR, MAJ3, MAJ5, NMAJ3, NMAJ5
import MTJ as mtj

class TestMTJClass(unittest.TestCase):
    def setUp(self):
        self.resistance = True
        self.voltage = 550
        self.mtj_cell = mtj.MTJ(self.resistance, self.voltage)

    def test_constructor(self):
        self.assertTrue(self.mtj_cell.get_resistance())
        self.assertEqual(self.mtj_cell.get_voltage(), 550)

        self.assertEqual(self.mtj_cell.get_resistance_om(), RAP)
        self.mtj_cell.set_resistance(False)
        self.assertEqual(self.mtj_cell.get_resistance_om(), RP)

    def test_AND_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 400)
        src2_mtj = mtj.MTJ(True, 400)
        #with self.assertRaises(ValueError):
        #    AND(dest_mtj, src1_mtj, src2_mtj)
        
        src1_mtj.set_voltage(550)
        src2_mtj.set_voltage(550)
        #00->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        AND(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #01->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        AND(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #10->0
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(False)
        AND(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #11->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        AND(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
    
    def test_OR_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 300)
        src2_mtj = mtj.MTJ(True, 300)
        #with self.assertRaises(ValueError):
        #    OR(dest_mtj, src1_mtj, src2_mtj)
        
        src1_mtj.set_voltage(470)
        src2_mtj.set_voltage(470)
        #00->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        OR(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #01->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        OR(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #10->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(False)
        OR(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #11->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        OR(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())

    def test_NOT_logic(self):
        dest_mtj = mtj.MTJ(False, 0)
        src_mtj = mtj.MTJ(False, 200)
        #with self.assertRaises(ValueError):
        #    NOT(dest_mtj, src_mtj)
        
        src_mtj.set_voltage(350)
        #0->1
        src_mtj.set_resistance(False)
        NOT(dest_mtj, src_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #1->0
        src_mtj.set_resistance(True)
        NOT(dest_mtj, src_mtj)
        self.assertFalse(dest_mtj.get_resistance())

    def test_BUFF_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src_mtj = mtj.MTJ(False, 200)
        #with self.assertRaises(ValueError):
        #    BUFF(dest_mtj, src_mtj)
        
        src_mtj.set_voltage(600)
        #0->0
        src_mtj.set_resistance(False)
        BUFF(dest_mtj, src_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #1->1
        src_mtj.set_resistance(True)
        BUFF(dest_mtj, src_mtj)
        self.assertTrue(dest_mtj.get_resistance())

    def test_NAND_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 400)
        src2_mtj = mtj.MTJ(True, 400)
        with self.assertRaises(ValueError):
            NAND(dest_mtj, src1_mtj, src2_mtj)
        
        src1_mtj.set_voltage(300)
        src2_mtj.set_voltage(300)
        #00->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        NAND(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #01->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        NAND(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #10->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(False)
        NAND(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #11->0
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        NAND(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())

    def test_NOR_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 300)
        src2_mtj = mtj.MTJ(True, 300)
        with self.assertRaises(ValueError):
            NOR(dest_mtj, src1_mtj, src2_mtj)
        
        src1_mtj.set_voltage(250)
        src2_mtj.set_voltage(250)
        #00->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        NOR(dest_mtj, src1_mtj, src2_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #01->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        NOR(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #10->0
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(False)
        NOR(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #11->0
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        NOR(dest_mtj, src1_mtj, src2_mtj)
        self.assertFalse(dest_mtj.get_resistance())


    def test_vector_ALL(self):
        grid = [] #grid of MTJs
        rows = 6
        columns = 8
        for i in range(rows):
            grid.append([])
            for j in range(columns):
                grid[i].append(mtj.MTJ(False, 550))
        src1 = [1,1,0,1,1,1,1,1]
        src2 = [0,1,0,0,1,0,0,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[1][i].set_resistance(src2[i])
            AND(grid[2][i], grid[0][i], grid[1][i])
            dest.append(grid[2][i].get_resistance())
        self.assertEqual(dest, src2)

        src1 = [1,1,0,1,1,1,0,1]
        src2 = [0,1,0,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(470)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(470)
            OR(grid[2][i], grid[0][i], grid[1][i])
            dest.append(grid[2][i].get_resistance())
        expected = [1,1,0,1,1,1,1,1]
        self.assertEqual(dest, expected)

        src = [1,1,0,1,1,1,0,1]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src[i])
            grid[0][i].set_voltage(350)
            NOT(grid[2][i], grid[0][i])
            dest.append(grid[2][i].get_resistance())
        expected = [0,0,1,0,0,0,1,0]
        self.assertEqual(dest, expected)

        src = [1,1,0,1,1,1,0,1]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src[i])
            grid[0][i].set_voltage(600)
            BUFF(grid[2][i], grid[0][i])
            dest.append(grid[2][i].get_resistance())
        expected = [1,1,0,1,1,1,0,1]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,1,1]
        src2 = [0,1,0,0,1,0,0,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(300)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(300)
            t,e = NAND(grid[2][i], grid[0][i], grid[1][i])
            print(t,e)
            dest.append(grid[2][i].get_resistance())
        expected = [1,0,1,1,0,1,1,1]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,0,1]
        src2 = [0,1,0,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(250)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(250)
            NOR(grid[2][i], grid[0][i], grid[1][i])
            dest.append(grid[2][i].get_resistance())
        expected = [0,0,1,0,0,0,0,0]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,0,1]
        src2 = [0,1,0,0,1,1,1,0]
        src3 = [0,1,0,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(650)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(650)
            grid[2][i].set_resistance(src3[i])
            grid[2][i].set_voltage(650)
            MAJ3(grid[3][i], grid[0][i], grid[1][i], grid[2][i])
            dest.append(grid[3][i].get_resistance())
        expected = [0,1,0,0,1,1,1,0]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,0,0]
        src2 = [0,1,0,1,1,1,1,0]
        src3 = [0,1,0,1,0,0,1,0]
        src4 = [0,1,1,0,1,0,1,0]
        src5 = [0,1,1,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(4000)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(4000)
            grid[2][i].set_resistance(src3[i])
            grid[2][i].set_voltage(4000)
            grid[3][i].set_resistance(src4[i])
            grid[3][i].set_voltage(4000)
            grid[4][i].set_resistance(src5[i])
            grid[4][i].set_voltage(4000)
            MAJ5(grid[5][i], grid[0][i], grid[1][i], grid[2][i], grid[3][i], grid[4][i])
            dest.append(grid[5][i].get_resistance())
        expected = [0,1,0,1,1,0,1,0]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,0,1]
        src2 = [0,1,0,0,1,1,1,0]
        src3 = [0,1,0,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(450)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(450)
            grid[2][i].set_resistance(src3[i])
            grid[2][i].set_voltage(450)
            NMAJ3(grid[3][i], grid[0][i], grid[1][i], grid[2][i])
            dest.append(grid[3][i].get_resistance())
        expected = [1,0,1,1,0,0,0,1]
        self.assertEqual(dest, expected)

        src1 = [1,1,0,1,1,1,0,0]
        src2 = [0,1,0,1,1,1,1,0]
        src3 = [0,1,0,1,0,0,1,0]
        src4 = [0,1,1,0,1,0,1,0]
        src5 = [0,1,1,0,1,0,1,0]
        dest = []
        for i in range(columns):
            grid[0][i].set_resistance(src1[i])
            grid[0][i].set_voltage(4000)
            grid[1][i].set_resistance(src2[i])
            grid[1][i].set_voltage(4000)
            grid[2][i].set_resistance(src3[i])
            grid[2][i].set_voltage(4000)
            grid[3][i].set_resistance(src4[i])
            grid[3][i].set_voltage(4000)
            grid[4][i].set_resistance(src5[i])
            grid[4][i].set_voltage(4000)
            NMAJ5(grid[5][i], grid[0][i], grid[1][i], grid[2][i], grid[3][i], grid[4][i])
            dest.append(grid[5][i].get_resistance())
        expected = [1,0,1,0,0,1,0,1]
        self.assertEqual(dest, expected)


    def test_MAJ3_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 300)
        src2_mtj = mtj.MTJ(True, 300)
        src3_mtj = mtj.MTJ(True, 300)
        with self.assertRaises(ValueError):
            MAJ3(dest_mtj, src1_mtj, src2_mtj, src3_mtj)
        
        src1_mtj.set_voltage(650)
        src2_mtj.set_voltage(650)
        src3_mtj.set_voltage(650)
        #000->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(False)
        MAJ3(dest_mtj, src1_mtj, src2_mtj, src3_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #001->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(True)
        MAJ3(dest_mtj, src1_mtj, src2_mtj, src3_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #011->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        src3_mtj.set_resistance(True)
        MAJ3(dest_mtj, src1_mtj, src2_mtj, src3_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #111->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        src3_mtj.set_resistance(True)
        MAJ3(dest_mtj, src1_mtj, src2_mtj, src3_mtj)
        self.assertTrue(dest_mtj.get_resistance())

    def test_MAJ5_logic(self):
        dest_mtj = mtj.MTJ(True, 0)
        src1_mtj = mtj.MTJ(False, 300)
        src2_mtj = mtj.MTJ(True, 300)
        src3_mtj = mtj.MTJ(True, 300)
        src4_mtj = mtj.MTJ(True, 300)
        src5_mtj = mtj.MTJ(True, 300)
        with self.assertRaises(ValueError):
            MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        
        src1_mtj.set_voltage(4000)
        src2_mtj.set_voltage(4000)
        src3_mtj.set_voltage(4000)
        src4_mtj.set_voltage(4000)
        src5_mtj.set_voltage(4000)
        #00000->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(False)
        src4_mtj.set_resistance(False)
        src5_mtj.set_resistance(False)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #00001->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(False)
        src4_mtj.set_resistance(False)
        src5_mtj.set_resistance(True)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #00011->0
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(False)
        src4_mtj.set_resistance(True)
        src5_mtj.set_resistance(True)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertFalse(dest_mtj.get_resistance())
        #00111->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(False)
        src3_mtj.set_resistance(True)
        src4_mtj.set_resistance(True)
        src5_mtj.set_resistance(True)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #01111->1
        src1_mtj.set_resistance(False)
        src2_mtj.set_resistance(True)
        src3_mtj.set_resistance(True)
        src4_mtj.set_resistance(True)
        src5_mtj.set_resistance(True)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertTrue(dest_mtj.get_resistance())
        #11111->1
        src1_mtj.set_resistance(True)
        src2_mtj.set_resistance(True)
        src3_mtj.set_resistance(True)
        src4_mtj.set_resistance(True)
        src5_mtj.set_resistance(True)
        MAJ5(dest_mtj, src1_mtj, src2_mtj, src3_mtj, src4_mtj, src5_mtj)
        self.assertTrue(dest_mtj.get_resistance())

    def test_OP_voltage(self):
        print("AND", AND_OP.min_v, AND_OP.max_v)
        print("OR", OR_OP.min_v, OR_OP.max_v)
        print("NOT", NOT_OP.min_v, NOT_OP.max_v)
        print("BUFF", BUFF_OP.min_v, BUFF_OP.max_v)
        print("NAND", NAND_OP.min_v, NAND_OP.max_v)
        print("NOR", NOR_OP.min_v, NOR_OP.max_v)
        print("MAJ3", MAJ3_OP.min_v, MAJ3_OP.max_v)
        print("MAJ5", MAJ5_OP.min_v, MAJ5_OP.max_v)
        print("NMAJ3", NMAJ3_OP.min_v, NMAJ3_OP.max_v)
        print("NMAJ5", NMAJ5_OP.min_v, NMAJ5_OP.max_v)

    
if __name__ == '__main__':
    unittest.main()