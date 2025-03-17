import cv2
import mediapipe as mp

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror the feed
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture_name = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get finger tip landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            # Get finger base landmarks for better detection
            index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            middle_base = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            ring_base = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
            pinky_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

            # Define conditions for each gesture

            # Thumbs Up (Thumb extended, other fingers curled)
            if thumb_tip.y < index_base.y and index_tip.y > index_base.y and middle_tip.y > middle_base.y:
                gesture_name = "Thumbs Up"

            # Peace Sign (Index and Middle fingers extended, others curled)
            elif index_tip.y < index_base.y and middle_tip.y < middle_base.y and ring_tip.y > ring_base.y:
                gesture_name = "Peace"

            # Open Palm (All fingers extended)
            elif (index_tip.y < index_base.y and middle_tip.y < middle_base.y and 
                  ring_tip.y < ring_base.y and pinky_tip.y < pinky_base.y and thumb_tip.y < index_base.y):
                gesture_name = "Open Palm"

    # Display gesture name
    if gesture_name:
        cv2.putText(frame, gesture_name, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.5, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
