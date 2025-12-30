"""
Eye-tracking calibration module for VR therapy.
"""

class CalibrationError(Exception):
    """Exception raised when calibration fails."""
    pass

def run_calibration():
    """
    Perform eye-tracking calibration.
    
    Returns:
        float: Confidence score of calibration (0.0 to 1.0)
    """
    # Simulate calibration process
    # In real implementation, this would interface with eye-tracker hardware
    import random
    confidence = random.uniform(0.7, 1.0)
    print(f"Calibration completed with confidence score: {confidence:.3f}")
    return confidence