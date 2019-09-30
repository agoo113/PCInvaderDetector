# PCInvaderDetector
Punish those who do pranks to your unlocked PC!

If culprit is caught, it will
- Automatically lock your PC to prevent further malicious activities.
- Play the alarm audio (remember to connect your PC to a loud loud loud speaker).
- capture the face of the culprit and automatically email it to the email group.

Steps:
1. Deploy the server side code to any server. It hosts a web server that just contains a switch for this detection system. You need to figure out a way to alter the server's boolean variable switch.
2. Train the facial recognizer from OpenCV with your faces, so the system can differentiate you from others (Well, it only works to some extent).
3. Run client/main.py. If you switch on the system from the browser webpage managed by the server, it will detect the face and mouse & keyboard activity and fire the alarm.
4. Have fun!
