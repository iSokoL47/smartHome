from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import threading

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo win1 setup
SERVO_W1_PIN = 4
GPIO.setup(SERVO_W1_PIN, GPIO.OUT)

# Rain sensor setup
RAIN_SENSOR_PIN = 23
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)

app = Flask(__name__)

# Global variable for the servo
servo = GPIO.PWM(SERVO_W1_PIN, 50)  # Initialize PWM with 50Hz frequency
servo.start(0)  # Start PWM with 0 duty cycle to avoid sudden movements

# Lock for thread safety
lock = threading.Lock()

def set_angle(angle):
    """Set the servo motor to the specified angle and stop PWM."""
    duty = 2.5 + (angle / 180.0) * 10.0
    with lock:  # Ensure exclusive access to the servo
        servo.ChangeDutyCycle(duty)
        time.sleep(1)  # Wait for the servo to reach the position
        servo.ChangeDutyCycle(0)  # Stop PWM signal

def monitor_rain_sensor():
    """Monitor the rain sensor and close the door if rain is detected."""
    while True:
        if GPIO.input(RAIN_SENSOR_PIN) == GPIO.LOW:  # Adjust if necessary based on sensor
            print("Rain detected! Closing the door.")
            set_angle(180)  # Close the door by moving servo to 180 degrees
        time.sleep(1)  # Check the sensor every second

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move_servo_windows", methods=["POST"])
def move_servo_windows():
    try:
        angle = int(request.form.get("angle"))
        threading.Thread(target=set_angle, args=(angle,)).start()  # Start a new thread to move the servo
        return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred"

if __name__ == "__main__":
    # Start the rain sensor monitoring thread
    threading.Thread(target=monitor_rain_sensor, daemon=True).start()
    
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        with lock:
            servo.stop()
        GPIO.cleanup()
