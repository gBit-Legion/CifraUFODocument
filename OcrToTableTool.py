import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OcrToTableTool:
    def __init__(self, image_path):
        self.image_path = image_path
        self.recognized_texts = []
        self.min_contour_area = 50000 if "9_perspective_corrected_3.jpg" == self.image_path else 5000
        self.threshold = 50 if "9_perspective_corrected_3.jpg" == self.image_path else 10
        self.cleaned_text = []

    def execute(self):
        self.read_image()
        self.convert_image_to_grayscale()
        self.threshold_image()
        self.invert_image()
        self.find_contours()
        self.filter_contours_and_leave_only_rectangles()
        self.group_contours()
        self.recognize_texts()
        self.process_results()
        return self.cleaned_text

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

    def filter_contours_and_leave_only_rectangles(self):
        self.rectangular_contours = []
        for contour in self.contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
            if len(approx) == 4:
                area = cv2.contourArea(approx)
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                if abs(1 - aspect_ratio) < 10 and area > self.min_contour_area:
                    self.rectangular_contours.append(approx)
        if len(self.rectangular_contours) > 1:
            self.rectangular_contours = sorted(self.rectangular_contours, key=lambda c: cv2.contourArea(c), reverse=True)
            self.rectangular_contours = self.rectangular_contours[1:]
        self.rectangular_contours = sorted(self.rectangular_contours, key=lambda c: cv2.boundingRect(c)[0])

    def group_contours(self):
        self.grouped_contours = []
        current_group = []
        previous_x = None
        for contour in self.rectangular_contours:
            x = cv2.boundingRect(contour)[0]
            if previous_x is None:
                current_group.append(contour)
            elif abs(x - previous_x) <= self.threshold:
                current_group.append(contour)
            else:
                self.grouped_contours.append(current_group)
                current_group = [contour]
            previous_x = x
        if len(current_group) > 0:
            self.grouped_contours.append(current_group)

    def recognize_texts(self):
        self.grouped_contours = sorted(self.grouped_contours, key=lambda group: cv2.boundingRect(group[0])[1])

        self.result_lists = [[] for _ in range(len(self.grouped_contours))]

        for i, group in enumerate(self.grouped_contours):
            group = sorted(group, key=lambda c: cv2.boundingRect(c)[1])
            for contour in group:
                x, y, w, h = cv2.boundingRect(contour)
                cropped_image = self.grayscale_image[y:y + h, x:x + w]
                text = pytesseract.image_to_string(cropped_image, lang='rus')
                self.result_lists[i].append(text.strip())

    def process_results(self):
        for i, result_list in enumerate(self.result_lists):
            cleaned_text = [item.replace('\n', ' ') for item in result_list]
            cleaned_text = [item.replace("- ", "") for item in cleaned_text]
            cleaned_text = [item.replace("\\", "") for item in cleaned_text]
            cleaned_text = [item.replace("-| ", "") for item in cleaned_text]
            cleaned_text = [item.replace("_ ", "") for item in cleaned_text]
            cleaned_text = [item.replace("наименова-", "наименование") for item in cleaned_text]
            self.cleaned_text.append(cleaned_text)
        return self.cleaned_text

    def display_image(self):
        image_with_grouped_contours = self.image.copy()
        for i, group in enumerate(self.grouped_contours):
            for contour in group:
                cv2.drawContours(image_with_grouped_contours, [contour], -1, (0, 255, 0), 2)
                moments = cv2.moments(contour)
                x = int(moments["m10"] / moments["m00"])
                y = int(moments["m01"] / moments["m00"])
                cv2.putText(image_with_grouped_contours, str(i + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Image with Grouped Contours", image_with_grouped_contours)
        cv2.waitKey(0)
        cv2.destroyAllWindows()