from datetime import datetime

def get_current_time() -> dict:
		"""
		Get the current time in a format YYYY-MM-DD HH:MM:SS.
		"""
		return {
			"current time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}