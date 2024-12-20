import cv2


def main():
    cam = cv2.VideoCapture(1)

    while True:
        _, frame = cam.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
