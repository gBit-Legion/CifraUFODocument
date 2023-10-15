import cv2
import numpy as np

class TableExtractor:
    def __init__(self, image_path):
        self.image_path = image_path

    def execute(self):
        self.read_image()
#        self.store_process_image("0_original.jpg", self.image)
        self.convert_image_to_grayscale()
#        self.store_process_image("1_grayscaled.jpg", self.grayscale_image)
        self.threshold_image()
#        self.store_process_image("2_thresholded.jpg", self.thresholded_image)
        self.invert_image()
#        self.store_process_image("3_inverteded.jpg", self.inverted_image)
        self.find_contours()
#        self.store_process_image("4_all_contours.jpg", self.image_with_all_contours)
        self.filter_contours_and_leave_only_rectangles()
#        self.store_process_image("5_only_rectangular_contours.jpg", self.image_with_only_rectangular_contours)
        self.find_largest_contours(3)
#        self.store_process_image("6_contour_with_max_area.jpg", self.image_with_contours)
        self.order_points_in_the_contour_with_max_area_ex()
#        self.store_process_image("8_with_4_corner_points_plotted.jpg", self.image_with_points_plotted)
        self.calculate_new_width_and_height_of_image()
        self.apply_perspective_transform()

        self.file_names = ["9_perspective_corrected_1.jpg", "9_perspective_corrected_2.jpg", "9_perspective_corrected_3.jpg"]
        self.store_process_images(self.file_names, self.perspective_corrected_images)
#        return self.perspective_corrected_images

    def read_image(self):
        self.image = cv2.imread(self.image_path)

    def convert_image_to_grayscale(self):
        self.grayscale_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def threshold_image(self):
        self.thresholded_image = cv2.threshold(self.grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    def invert_image(self):
        self.inverted_image = cv2.bitwise_not(self.thresholded_image)

    def find_contours(self):
        self.contours, self.hierarchy = cv2.findContours(self.inverted_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.image_with_all_contours = self.image.copy()
        cv2.drawContours(self.image_with_all_contours, self.contours, -1, (0, 255, 0), 3)

    def filter_contours_and_leave_only_rectangles(self):
        self.rectangular_contours = []
        for contour in self.contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if len(approx) == 4:
                self.rectangular_contours.append(approx)
        self.image_with_only_rectangular_contours = self.image.copy()
        cv2.drawContours(self.image_with_only_rectangular_contours, self.rectangular_contours, -1, (0, 255, 0), 3)

    def find_largest_contours(self, num_contours):
        areas = []
        self.contours_with_max_area = []
        for contour in self.rectangular_contours:
            area = cv2.contourArea(contour)
            areas.append(area)
        areas.sort(reverse=True)
        for i in range(min(num_contours, len(areas))):
            max_area = areas[i]
            for contour in self.rectangular_contours:
                if cv2.contourArea(contour) == max_area:
                    self.contours_with_max_area.append(contour)
                    break
        self.image_with_contours = self.image.copy()
        cv2.drawContours(self.image_with_contours, self.contours_with_max_area, -1, (0, 255, 0), 3)

    def order_points_in_the_contour_with_max_area_ex(self):
        self.contour_with_max_area_ordered = []
        self.image_with_points_plotted = self.image.copy()
        for contour in self.contours_with_max_area:
            contour_ordered = self.order_points(contour)
            self.contour_with_max_area_ordered.append(contour_ordered)
            for point in contour_ordered:
                point_coordinates = (int(point[0]), int(point[1]))
                self.image_with_points_plotted = cv2.circle(self.image_with_points_plotted, point_coordinates, 10, (0, 0, 255), -1)

    def order_points(self, pts):
        pts = pts.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect

    def calculate_new_width_and_height_of_image(self):
        existing_image_width = self.image.shape[1]
        existing_image_width_reduced_by_10_percent = int(existing_image_width * 0.9)
        self.new_image_widths = []
        self.new_image_heights = []
        for contour_ordered in self.contour_with_max_area_ordered:
            distance_between_top_left_and_top_right = self.calculateDistanceBetween2Points(
                contour_ordered[0], contour_ordered[1])
            distance_between_top_left_and_bottom_left = self.calculateDistanceBetween2Points(
                contour_ordered[0], contour_ordered[3])
            aspect_ratio = distance_between_top_left_and_bottom_left / distance_between_top_left_and_top_right
            new_image_width = existing_image_width_reduced_by_10_percent
            new_image_height = int(new_image_width * aspect_ratio)
            self.new_image_widths.append(new_image_width)
            self.new_image_heights.append(new_image_height)

    def apply_perspective_transform(self):
        self.perspective_corrected_images = []
        for i, contour_ordered in enumerate(self.contour_with_max_area_ordered):
            new_image_width = self.new_image_widths[i]
            new_image_height = self.new_image_heights[i]
            pts1 = np.float32(contour_ordered)
            pts2 = np.float32([[0, 0], [new_image_width, 0], [new_image_width, new_image_height], [0, new_image_height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            perspective_corrected_image = cv2.warpPerspective(self.image, matrix, (new_image_width, new_image_height))
            self.perspective_corrected_images.append(perspective_corrected_image)

    def calculateDistanceBetween2Points(self, p1, p2):
        dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        return dis

    # Исправить! Сохранение в папку "./process_images/table_extractor/"
    def store_process_image(self, file_name, image):
        if not cv2.imwrite(file_name, image):
            raise Exception("Could not write image")

    # Исправить! Сохранение в папку "./process_images/table_extractor/"
    def store_process_images(self, file_names, images):
        if len(file_names) != len(images):
            raise ValueError("Number of file names doesn't match number of images")
        for file_name, image in zip(file_names, images):
            if not cv2.imwrite(file_name, image):
                raise Exception("Could not write image")