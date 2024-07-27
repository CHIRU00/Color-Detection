# Color-Detection
This project is live color filter using OpenCv
Real-Time Color Detection and Filtering
Project Overview
The Real-Time Color Detection and Filtering project involves using computer vision techniques to capture live video feed from a camera and apply color-based filtering. The project demonstrates the ability to detect and isolate specific colors in real-time, showcasing the practical application of image processing and computer vision.
Features
1.	Live Video Capture: The application captures live video feed from a connected camera (either default or external).
2.	Color Filtering: The system can detect and isolate three primary colors (Red, Green, and Blue) based on their HSV color space values.
3.	Real-Time Processing: The video feed is processed in real-time, displaying the original frame alongside the filtered frames for each color.
4.	User-Friendly Interface: Multiple resizable windows display the original and color-filtered frames, providing a clear visualization of the detected colors.
Technologies and Tools Used
•	OpenCV: For capturing video, converting color spaces, applying color masks, and displaying frames.
•	NumPy: For handling numerical operations and defining color masks.
•	Python: For integrating various libraries and implementing the core logic of the application.
Implementation Details
•	Video Capture: The application uses OpenCV to capture video feed from the default or external camera. The video feed is processed frame-by-frame in real-time.
•	Color Space Conversion: Each frame is converted from the BGR color space to the HSV color space, which is more suitable for color-based filtering.
•	Color Masks: The application defines specific HSV ranges for Red, Green, and Blue colors. Using these ranges, color masks are created to isolate the desired colors within the frame.
o	Red Mask: Defined by HSV ranges [161, 155, 84] to [179, 255, 255].
o	Blue Mask: Defined by HSV ranges [100, 150, 0] to [140, 255, 255].
o	Green Mask: Defined by HSV ranges [35, 52, 72] to [85, 255, 255].
•	Bitwise Operations: Bitwise operations are used to apply the color masks to the original frame, resulting in frames where only the specified colors are visible.
•	Displaying Frames: OpenCV is used to create resizable windows to display the original frame and the color-filtered frames for Red, Green, and Blue.
Skills Demonstrated
•	Computer Vision: Applying color-based filtering techniques to process and analyze video frames in real-time.
•	Image Processing: Using OpenCV to perform color space conversion and bitwise operations to isolate specific colors.
•	Python Programming: Writing efficient code to handle real-time video capture and processing.
•	Real-Time Systems: Developing an application that processes and displays video feed in real-time, demonstrating the ability to handle continuous data streams.
Conclusion
This project showcases the application of computer vision and image processing techniques to create a real-time color detection and filtering system. The ability to capture live video feed and apply color-based filtering in real-time demonstrates proficiency in using OpenCV and Python for practical computer vision tasks. This project can be further extended to include additional features such as detecting multiple colors simultaneously, applying different image processing techniques, and integrating with other systems for more complex applications.
