"""
Scripts responsible for image processing
"""
import numpy as np
import cv2
import random
from typing import List, Set


def divideImageIntoCells(image: np.ndarray, h: int, w: int) -> List[List[np.ndarray]]:
    """Divide image into cells, save it in List."""
    cells = []
    cell_height = image.shape[0] // h
    cell_width = image.shape[1] // w
    for i in range(h):
        row = []
        for j in range(w):
            cell = image[i*cell_height:(i+1)*cell_height, j*cell_width:(j+1)*cell_width]
            row.append(cell)
        cells.append(row)
    return cells

def generateRandomMatrix(h: int, w: int) -> Set[int]:
    """Generate random matrix for test, h and w being the size of cell matrix."""
    randint = random.randint(1, h*w)
    random_cell_matrix = set()
    while len(random_cell_matrix) < randint:
        random_cell = (random.randint(0, h-1), random.randint(0, w-1))
        random_cell_matrix.add(random_cell)
    return random_cell_matrix

def generateImageFromMatrix(inputImage: np.ndarray, 
                            cell_matrix: Set[int], 
                            cells: List[List[np.ndarray]]) -> np.ndarray:
    """
    Generate and return image from matrix. 
    
    inputImage - is given for creating new canvas the same size 
    cell_matrix - matrix of integers
    cells - matrix of small cell images from inputImage
    """
    image_h, image_w, image_ch = inputImage.shape
    outputImage = np.zeros((image_h, image_w, image_ch), dtype=np.uint8)
    
    cell_size = cells[0][0].shape[0]
    for i, j in cell_matrix:
        start_row, end_row = i * cell_size, (i+1) * cell_size
        start_col, end_col = j * cell_size, (j+1) * cell_size
    
        outputImage[start_row:end_row, start_col:end_col] = cells[i][j]

    return outputImage

def showMeTheImage(image: np.ndarray, scale_factor: int = 1) -> None:
    """Show input image, scale if necessary."""
    if scale_factor != 1:
        image = cv2.resize(outputImage, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    
    cv2.imshow('testWindow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def processImageRandomly(inputImage: np.ndarray) -> np.ndarray:
    """Process image using random generaed matrix"""
    cells = divideImageIntoCells(inputImage, 15, 20)
    cell_matrix = generateRandomMatrix(15, 20)
    outputImage = generateImageFromMatrix(inputImage, cell_matrix, cells)

    return outputImage


if __name__ == '__main__':
    inputImage = cv2.imread('testImage.jpg')

    outputImage = processImageRandomly(inputImage)
    showMeTheImage(outputImage, scale_factor=0.5)