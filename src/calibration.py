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
    
    Raises:
        CalibrationError: If calibration confidence is below threshold (0.85)
    """
    # Simulate calibration process
    # In real implementation, this would interface with eye-tracker hardware
    import random
    confidence = random.uniform(0.7, 1.0)
    print(f"Calibration completed with confidence score: {confidence:.3f}")
    
    # Validation step: check confidence threshold
    threshold = 0.85
    if confidence < threshold:
        raise CalibrationError(
            "Calibration failed to meet the required accuracy threshold. Please try again."
        )
    else:
        print("Calibration validation passed. Proceeding with therapy session.")
    
    return confidence