import os
import shutil
import sys
import cv2

class FrameCapture:
    '''
        Class definition to capture frames
    '''
    def __init__(self, file_path):
        '''
            initializing directory where the captured frames will be stored.
            Also truncating the directory where captured frames are stored, if exists.
        '''
        self.directory = "captured_frames"
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    # def capture_frames(self):
    #     '''
    #         This method captures the frames from the video file provided.
    #         This program makes use of openCV library
    #     '''
    #     cv2_object = cv2.VideoCapture(self.file_path)
    #
    #     frame_number = 0
    #     frame_found = 1
    #
    #     while frame_found:
    #         frame_found, image = cv2_object.read()
    #         capture = f'{self.directory}/frame{frame_number}.jpg'
    #         cv2.imwrite(capture, image)
    #
    #         frame_number += 1

    def capture_frames(self):
        '''
            This method captures the frames from the video file provided.
            This program makes use of openCV library
        '''
        cv2_object = cv2.VideoCapture(self.file_path)

        frame_number = 0

        while True:
            frame_found, image = cv2_object.read()

            if not frame_found:
                break  # Exit loop if no more frames are found

            capture = f'{self.directory}/frame{frame_number}.jpg'
            cv2.imwrite(capture, image)

            frame_number += 1

        cv2_object.release()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Capture_video_frames.py <video_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    fc = FrameCapture(file_path)
    fc.capture_frames()
