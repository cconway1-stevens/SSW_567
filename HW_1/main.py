#Cameron Conway 10445293
# I pldge my honor that I have abided by the stevens honor system
import unittest
# import numpy as np

# def selection_sort(x):
#     for i in range(len(x)):
#         swap = i + np.argmin(x[i:])
#         (x[i], x[swap]) = (x[swap], x[i])
#     return x

def triDataValidation(arr):
    # selection_sort(arr)
    if len(arr) == 3 :
        return True
    else:
        return False

def classify_triangle(arr):
    print(arr)
    # sorts data and validates array for at 3 terms 
    if triDataValidation(arr) == True:
        #break into usable var after sort
        legA = arr[0]
        legB = arr[1]
        legC = arr[2]
        #will out put str of the type of triangle if any 
        if (legA < (legB + legC)) and (legB < (legA + legC)) and (legC < (legB + legA)):
            # simpliest case
            if legA == legB == legC:
                return "Equilateral"
            elif legA == legB or legA == legC or legB == legC:
                return "Isosceles"
            # Needs to be here logically because the cases above can be right triangles as well
            elif (legA ** 2 + legB ** 2 == legC ** 2) or (legC ** 2 + legB ** 2 == legA ** 2) or (legA ** 2 + legC ** 2 == legB ** 2):
                return "Right"
            elif legA != legB != legC:
                return "Scalene"
        else:
                return "NotATriangle"


def runClassify_triangle(arr):
    # selection_sort(arr)
    legA = arr[0]
    legB = arr[1]
    legC = arr[2]
    print('classify_triangle(', legA, ',', legB, ',', legC, ') = ',classify_triangle([legA,legB,legC]),sep="")
     
class TestTriangles(unittest.TestCase):
    def test_Equilateral(self):
        #test cases to check if the three points form an Equilateral triangle
        self.assertEqual(classify_triangle([5,5,5]), "Equilateral", "a = 5, b = 5, c = 5 is an Equilateral triangle")
        self.assertEqual(classify_triangle([2345,2345,2345]), "Equilateral", "a = 2345, b = 2345, c = 2345 is an Equilateral triangle")
        self.assertEqual(classify_triangle([34.5,34.5,34.5]), "Equilateral", "a = 34.5, b = 34.5, c = 34.5 is an Equilateral triangle")
    def test_Isosceles(self):
        #test cases to check if the three points form an Isosceles triangle
        self.assertEqual(classify_triangle([3,3,2]), "Isosceles", "a = 3, b = 3, c = 2 is an Isosceles triangle")
        self.assertEqual(classify_triangle([4.5,4.5,8]), "Isosceles", "a = 4.5, b = 4.5, c = 8 is an Isosceles triangle")
        self.assertEqual(classify_triangle([3,7,7]), "Isosceles", "a = 3, b = 7, c = 7 is an Isosceles triangle")
    def test_Right(self):
        #test cases to check if the three points form a Right triangle
        self.assertEqual(classify_triangle([3,4,5]), "Right", "a = 3, b = 4, c = 5 is a Right triangle")
        self.assertEqual(classify_triangle([7,24,25]), "Right", "a = 7, b = 24, c = 25 is a Right triangle")
        self.assertEqual(classify_triangle([5,12,13]), "Right", "a = 5, b = 12, c = 13 is a Right triangle")
    def test_Scalene(self):
    #test cases to check if the three points form a Scalene triangle
        self.assertEqual(classify_triangle([6,5,4]), "Scalene", "a = 6, b = 5, c = 4 is a Scalene triangle")
        self.assertEqual(classify_triangle([12,10,8]), "Scalene", "a = 12, b = 10, c = 8 is a Scalene triangle")
        self.assertEqual(classify_triangle([13,14,19]), "Scalene", "a = 13, b = 14, c = 19 is a Scalene triangle")
    def test_NotATriangle(self):
        #test cases to check if the three points form a triangle or not 
        self.assertEqual(classify_triangle([2,3,7]), "NotATriangle", "a = 2, b = 3, c = 7 is not a triangle")
        self.assertEqual(classify_triangle([4,6,14]), "NotATriangle", "a = 4, b = 6, c = 14 is not a triangle")
        self.assertEqual(classify_triangle([4.5,6.7,56]), "NotATriangle", "a = 4.5, b = 6.7, c = 56 is not a triangle")
        self.assertEqual(classify_triangle([67,1002,7999999999]), "NotATriangle", "a = 67, b = 1002, c = 7999999999 is not a triangle")
if __name__ == '__main__':
    #Sample numbers to input to test the program output 
    runClassify_triangle([5,5,5])
    runClassify_triangle([3,3,2])
    runClassify_triangle([3,4,5])
    runClassify_triangle([6,5,4])
    runClassify_triangle([2,3,7])

    unittest.main(exit=True)