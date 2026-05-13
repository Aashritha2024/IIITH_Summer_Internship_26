Week 05 - Task 02
Image Scaling using FFmpeg
Objective:
The extracted dataset images were originally of high resolution.
Before training the YOLO model, all images were resized to lower dimensions to reduce computation time and improve training efficiency.

The resizing process was performed while preserving the original aspect ratio of the images. Since YOLO annotations are stored in normalized format, preserving aspect ratio ensures that the existing bounding box label files remain valid and do not require modification.

Tool Used:
FFmpeg

Scaling Configuration:
Target Width: 384 pixels
Height: Automatically adjusted using -1
Aspect Ratio: Preserved

Scaling format used:
scale=384:-1
