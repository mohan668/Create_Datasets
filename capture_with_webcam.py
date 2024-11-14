import cv2
import os

if __name__ == "__main__":
    while True:
        # Ask for the class of the object (e.g., "wrapper", "specs", etc.)
        class_name = input("Enter the class name for the object (e.g., 'wrapper', 'specs', etc.): ").strip()

        # Define the directory path
        save_dir = f"./images/{class_name}"

        # Check if the directory already exists
        if os.path.exists(save_dir):
            # Prompt user about the existing class folder
            choice = input(f"The class '{class_name}' already exists. Do you want to add images to it? (y/n): ").strip().lower()
            if choice == 'y':
                break
            else:
                print("Please enter a different class name.")
        else:
            # Create a new directory if it doesn't exist
            os.makedirs(save_dir)
            break

    # Open connected mobile camera (camera index 1)
    cam = cv2.VideoCapture(1)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height

    # Prompt user to start capturing images
    capture_prompt = input("Press 'y' to start capturing images or 'n' to exit: ").strip().lower()

    if capture_prompt != 'y':
        print("Exiting program...")
        cam.release()
        cv2.destroyAllWindows()
        exit()

    print("\n[INFO] Capturing images... Press 'c' to capture, 'q' to stop.")

    count = 0
    while True:
        # Capture a frame from the webcam
        ret, img = cam.read()
        if not ret:
            print("[ERROR] Could not access the webcam.")
            break

        # Display the live video feed
        cv2.imshow('Capture - Press "c" to capture, "q" to quit', img)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):  # 'c' key to capture an image
            img_name = f"{save_dir}/{class_name}-{count}.jpg"
            cv2.imwrite(img_name, img)
            print(f"[INFO] Captured {img_name}")
            count += 1

        elif key == ord('q'):  # 'q' key to quit capturing
            break

    # Release the webcam and close all OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

    print("\n[INFO] Exiting program...")
